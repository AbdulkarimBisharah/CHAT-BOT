"""
============================================================================
RETRIEVAL ENGINE - hybrid rule-based + TF-IDF retrieval (pure Python)
No API key, no external ML libraries. Runs anywhere Python runs.
============================================================================
Pipeline for each student question:
  1) Normalise the text.
  2) RULE LAYER: high-confidence intent patterns (deadline, weightage,
     group size, plagiarism, tools...). A hit returns a direct answer.
  3) RETRIEVAL LAYER: TF-IDF + cosine similarity across the knowledge base.
  4) CONFIDENCE GATE: if the best score is too low, return an honest
     "I'm not sure" fallback instead of guessing.
============================================================================
"""

import math
import re

STOPWORDS = set((
    "a an the is are was were be been being do does did of to in on for with and or "
    "as at by from it this that these those i you my our we they he she what when "
    "where which who how why can could should would will shall may might need want "
    "about into if then than"
).split())


def normalise(text: str) -> str:
    text = (text or "").lower()
    text = re.sub(r"[^a-z0-9\s.]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def tokenise(text: str):
    tokens = []
    for w in normalise(text).split(" "):
        w = w.rstrip(".")
        if not w or w in STOPWORDS:
            continue
        if re.fullmatch(r"[0-9]", w):   # keep single digits (assignment/part numbers)
            tokens.append(w)
        elif len(w) > 1:
            tokens.append(w)
    return tokens


# ---- Rule layer: high-confidence intent patterns --------------------------
# Each rule: if ALL words in ANY group are present, jump to that entry id.
RULES = [
    ("a3-deadline",     [["deadline"], ["due"], ["when", "due"], ["when", "submit"],
                         ["hand", "in", "date"], ["when", "a3"]]),
    ("a3-weightage",    [["weightage"], ["worth"], ["how", "much"], ["percentage"], ["percent"]]),
    ("a3-groupsize",    [["group", "size"], ["how", "many", "students"],
                         ["how", "many", "members"], ["how", "many", "people"], ["team", "size"]]),
    ("a3-plagiarism",   [["plagiarism"], ["turnitin"], ["similarity"], ["copy", "paste"], ["cheating"]]),
    ("a3-2-tools",      [["what", "tools"], ["which", "tools"], ["tools", "use"], ["wokwi"], ["tinkercad"]]),
    ("a3-4-ieee",       [["ieee"], ["how", "many", "pages"], ["page", "limit"], ["manuscript", "format"]]),
    ("a3-deliverables", [["what", "submit"], ["deliverables"], ["what", "hand", "in"], ["what", "do", "submit"]]),
    ("a3-rubric",       [["rubric"], ["how", "graded"], ["how", "marked"],
                         ["marking", "scheme"], ["how", "is", "graded"]]),
    ("a3-1",            [["a3.1"], ["a31"], ["resource", "risk"]]),
    ("a3-2",            [["a3.2"], ["a32"], ["proof", "concept"]]),
    ("a3-3",            [["a3.3"], ["a33"], ["presentation"]]),
    ("a3-4",            [["a3.4"], ["a34"], ["manuscript"]]),
]

OTHER_ASSIGNMENT = re.compile(r"\b(a2|assignment 2|task 2|a1|assignment 1|task 1|a4|assignment 4)\b")

HIGH = 0.28   # confident retrieval threshold
LOW = 0.12    # below this = don't guess


class ChatEngine:
    def __init__(self, knowledge_base):
        self.kb = knowledge_base
        self.docs = []      # list of (entry, term_freq_dict)
        self.idf = {}
        self._build_index()

    def _build_index(self):
        self.docs = []
        for entry in self.kb:
            # keywords weighted twice, then question + answer
            kw = " ".join(entry.get("keywords", []))
            doc_text = f"{kw} {kw} {entry.get('question','')} {entry.get('answer','')}"
            tokens = tokenise(doc_text)
            tf = {}
            for t in tokens:
                tf[t] = tf.get(t, 0) + 1
            self.docs.append((entry, tf))

        df = {}
        for _, tf in self.docs:
            for t in tf:
                df[t] = df.get(t, 0) + 1
        n = len(self.docs)
        self.idf = {t: math.log((n + 1) / (c + 1)) + 1 for t, c in df.items()}

    def _vectorise(self, tf):
        return {t: f * self.idf[t] for t, f in tf.items() if t in self.idf}

    @staticmethod
    def _cosine(a, b):
        dot = sum(v * b[t] for t, v in a.items() if t in b)
        mag_a = math.sqrt(sum(v * v for v in a.values()))
        mag_b = math.sqrt(sum(v * v for v in b.values()))
        if mag_a == 0 or mag_b == 0:
            return 0.0
        return dot / (mag_a * mag_b)

    def _find(self, entry_id):
        for entry, _ in self.docs:
            if entry["id"] == entry_id:
                return entry
        return None

    def _check_rules(self, tokens, raw_text):
        joined = " ".join(tokens)
        token_set = set(tokens)
        # If the student explicitly names another assignment, skip generic A3 rules.
        if OTHER_ASSIGNMENT.search(normalise(raw_text)):
            return None
        for entry_id, groups in RULES:
            for words in groups:
                if all((w in token_set) or (w in joined) for w in words):
                    return entry_id
        return None

    def _pack(self, entry, kind, confidence):
        text = entry["answer"]
        if entry.get("verified") is False:
            text += ("\n\n\u26A0\uFE0F Note: this detail hasn't been confirmed from a final "
                     "brief yet - please double-check with your lecturer.")
        if kind == "retrieval-lowconf":
            text = ("I think this is what you're asking about:\n\n" + text +
                    "\n\nIf that's not it, try rephrasing your question.")
        return {
            "type": kind,
            "text": text,
            "source": entry.get("source"),
            "confidence": confidence,
            "id": entry["id"],
        }

    def answer(self, question: str):
        tokens = tokenise(question)
        if not tokens:
            return {
                "type": "empty",
                "text": ("Ask me anything about the ITS67404 IoT coursework - deadlines, "
                         "weightage, formats, tools, or what each assignment needs."),
                "source": None, "confidence": 0.0, "id": None,
            }

        # 1) Rule layer
        rule_id = self._check_rules(tokens, question)
        if rule_id:
            entry = self._find(rule_id)
            if entry:
                return self._pack(entry, "rule", 1.0)

        # 2) Retrieval layer
        qtf = {}
        for t in tokens:
            qtf[t] = qtf.get(t, 0) + 1
        qvec = self._vectorise(qtf)

        best, best_score = None, 0.0
        for entry, tf in self.docs:
            score = self._cosine(qvec, self._vectorise(tf))
            if score > best_score:
                best_score, best = score, entry

        # 3) Confidence gate
        if not best or best_score < LOW:
            return {
                "type": "unknown",
                "text": ("I'm not sure about that one - I couldn't find it in the coursework "
                         "briefs I have. Please check with your lecturer or on MyTIMeS. You can "
                         "also try rephrasing, or ask about deadlines, weightage, formats, tools, "
                         "or what each assignment needs."),
                "source": None, "confidence": best_score, "id": None,
            }

        kind = "retrieval" if best_score >= HIGH else "retrieval-lowconf"
        return self._pack(best, kind, best_score)
