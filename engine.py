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

import difflib
import math
import re

STOPWORDS = set((
    "a an the is are was were be been being do does did of to in on for with and or "
    "as at by from it this that these those i you my our we they he she what when "
    "where which who how why can could should would will shall may might need want "
    "about into if then than"
).split())

# Query-side synonym expansion: map the many ways a student phrases something to the
# canonical word the knowledge base actually uses. Applied ONLY to the retrieval query
# (never to the rule layer or the index), so it can widen a match but never mis-fire a
# rule. Each key, if present in the question, ADDS its canonical term to the query.
SYNONYMS = {
    # marks / weightage
    "grade": "marks", "grades": "marks", "mark": "marks", "scoring": "marks",
    "worth": "weightage", "weighting": "weightage", "weighted": "weightage",
    # submission
    "submitting": "submit", "submitted": "submit", "submissions": "submit",
    "upload": "submit", "uploading": "submit", "uploaded": "submit", "handing": "submit",
    # deadlines
    "due": "deadline", "duedate": "deadline", "deadlines": "deadline",
    "when": "deadline",  # harmless: 'when' is a stopword for tokens but helps intent
    # referencing
    "cite": "citation", "citing": "citation", "citations": "references",
    "reference": "references", "referencing": "references",
    # AI
    "chatgpt": "ai", "gpt": "ai", "llm": "ai", "generative": "ai", "copilot": "ai",
    "gemini": "ai",
    # groups
    "team": "group", "teammate": "group", "teammates": "group", "groupmate": "group",
    "members": "group",
    # presentation
    "present": "presentation", "presenting": "presentation", "slides": "presentation",
    "slide": "presentation", "demo": "presentation",
    # plagiarism
    "copying": "plagiarism", "copied": "plagiarism", "plagiarise": "plagiarism",
    "plagiarizing": "plagiarism", "turnitin": "plagiarism", "similarity": "plagiarism",
    # misc morphology
    "pages": "page", "wordcount": "words", "wordlimit": "words", "format": "formatting",
    "individually": "individual", "requirements": "requirement",
}


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

# Priority rules: topic-based FAQs that must win BEFORE the "student named another
# assignment" skip below, and before TF-IDF (whose score gets diluted by the long
# keyword lists on these entries). Matched on EXACT tokens only (no substring), so a
# short trigger like "ai" can't accidentally fire on words such as "email"/"detail".
PRIORITY_RULES = [
    ("faq-ai-usage",   [["ai"], ["chatgpt"], ["gpt"], ["generative"], ["copilot"],
                        ["gemini"], ["llm"]]),
    ("faq-continuous", [["continuous"], ["continuation"], ["continue"]]),
]

OTHER_ASSIGNMENT = re.compile(r"\b(a2|assignment 2|task 2|a1|assignment 1|task 1|a4|assignment 4)\b")

# When a student explicitly names one assignment, scope retrieval to that
# assignment's entries. This stops questions like "how much is assignment 1
# worth?" leaking to the heavily-keyworded Assignment 3 answers.
ASSIGNMENT_PATTERNS = {
    "a1": re.compile(r"\b(a1|assignment 1|task 1|assessment task 1)\b"),
    "a2": re.compile(r"\b(a2|assignment 2|task 2|assessment task 2)\b"),
    "a3": re.compile(r"\b(a3|assignment 3|task 3|assessment task 3)\b"),
}


def target_assignment(raw_text: str):
    """Return 'a1'/'a2'/'a3' if exactly one assignment is named, else None."""
    norm = normalise(raw_text)
    hits = [key for key, pat in ASSIGNMENT_PATTERNS.items() if pat.search(norm)]
    return hits[0] if len(hits) == 1 else None

# Small talk: greetings / thanks. If a message is ONLY these words, answer warmly
# instead of running retrieval (which would otherwise return "I'm not sure").
GREETINGS = {"hi", "hello", "hey", "hiya", "yo", "howdy", "greetings", "morning",
             "afternoon", "evening", "salam", "assalamualaikum", "hai", "helo"}
THANKS = {"thanks", "thank", "thankyou", "thx", "ty", "cheers", "appreciate",
          "appreciated", "great", "awesome", "nice", "ok", "okay", "cool"}

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
        # Vocabulary of known terms, used to fuzzy-correct typos in a student's question.
        self.vocab = [t for t in self.idf if not t.isdigit() and len(t) >= 4]

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

    def _expand_query(self, tokens):
        """Widen the retrieval query: keep the student's words, then ADD canonical
        synonyms and fuzzy-corrected spellings of any word not already known. This
        only affects TF-IDF scoring, never the rule layer."""
        expanded = list(tokens)
        for t in tokens:
            if t in SYNONYMS:
                expanded.append(SYNONYMS[t])
            if t not in self.idf and len(t) >= 4:
                # typo? snap to the closest known vocabulary term.
                near = difflib.get_close_matches(t, self.vocab, n=1, cutoff=0.82)
                if near:
                    expanded.append(near[0])
        return expanded

    def related(self, entry_id, n=3):
        """Suggested follow-up questions: siblings from the same assignment first,
        then a couple of others. Used for 'related question' chips in the UI."""
        if not entry_id:
            return []
        prefix = entry_id.split("-")[0]
        same, other = [], []
        for entry, _ in self.docs:
            if entry["id"] == entry_id or not entry.get("question"):
                continue
            (same if entry["id"].startswith(prefix + "-") else other).append(entry["question"])
        return (same + other)[:n]

    @staticmethod
    def _split_candidates(question):
        """Break a possibly-compound question into parts on '?', ' and ', ';'."""
        parts = re.split(r"\?+|\band\b|;|&", question, flags=re.IGNORECASE)
        return [p.strip() for p in parts if len(tokenise(p)) >= 1]

    def answer_all(self, question):
        """Answer a compound question ('when is A2 due and how much is it worth?') as a
        list of results - one per distinct sub-answer. Falls back to a single answer
        when the split doesn't yield two genuinely different, confident answers."""
        whole = self.answer(question)
        parts = self._split_candidates(question)
        if len(parts) < 2:
            return [whole]
        # If the whole question names one assignment ("assignment 2 ... and ..."),
        # carry that context into any sub-part that doesn't name one itself.
        whole_target = target_assignment(question)
        results, seen = [], set()
        for part in parts:
            scoped = part
            if whole_target and not target_assignment(part):
                scoped = f"{whole_target} {part}"
            r = self.answer(scoped)
            if (r["id"] and r["type"] in ("rule", "retrieval", "retrieval-lowconf")
                    and r["id"] not in seen):
                seen.add(r["id"])
                results.append(r)
        return results if len(results) >= 2 else [whole]

    def _check_rules(self, tokens, raw_text):
        joined = " ".join(tokens)
        token_set = set(tokens)
        # Priority rules first (exact-token match), even when another assignment is named.
        for entry_id, groups in PRIORITY_RULES:
            for words in groups:
                if all(w in token_set for w in words):
                    return entry_id
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

        # 0) Small talk: greeting / thanks (only if the whole message is small talk)
        token_set = set(tokens)
        if token_set and token_set <= (GREETINGS | THANKS):
            if token_set & THANKS and not (token_set & GREETINGS):
                text = ("You're welcome! Ask me anything else about the ITS67404 IoT "
                        "coursework - deadlines, weightage, formats, tools, or what each "
                        "assignment needs.")
            else:
                text = ("Hi! I'm your IoT coursework assistant. Ask me about deadlines, "
                        "weightage, formats, tools, or what each of Assignments 1, 2 and 3 "
                        "needs - I answer from the official ITS67404 briefs and show the source.")
            return {"type": "smalltalk", "text": text,
                    "source": None, "confidence": 1.0, "id": None}

        # 1) Rule layer
        rule_id = self._check_rules(tokens, question)
        if rule_id:
            entry = self._find(rule_id)
            if entry:
                return self._pack(entry, "rule", 1.0)

        # 2) Retrieval layer (with synonym + typo expansion)
        qtf = {}
        for t in self._expand_query(tokens):
            qtf[t] = qtf.get(t, 0) + 1
        qvec = self._vectorise(qtf)

        # Scope to a single named assignment when the student names one.
        target = target_assignment(question)
        candidates = self.docs
        if target:
            scoped = [(e, tf) for e, tf in self.docs if e["id"].startswith(target + "-")]
            if scoped:
                candidates = scoped

        best, best_score = None, 0.0
        for entry, tf in candidates:
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
