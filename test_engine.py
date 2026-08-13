"""
============================================================================
Tests for the retrieval engine. No pytest needed - just run:

    python test_engine.py

Every check prints PASS/FAIL and the script exits non-zero if anything fails,
so it also works in CI. These lock the behaviour of the rule layer, the
retrieval layer, the confidence gate, small talk, and the unverified note.
============================================================================
"""

import sys

from knowledge_base import KNOWLEDGE_BASE
from engine import ChatEngine, tokenise

engine = ChatEngine(KNOWLEDGE_BASE)

_failures = []


def check(name, condition, detail=""):
    status = "PASS" if condition else "FAIL"
    print(f"[{status}] {name}" + (f" - {detail}" if detail and not condition else ""))
    if not condition:
        _failures.append(name)


def ans(q):
    return engine.answer(q)


# ---- Knowledge base integrity ---------------------------------------------
ids = [e["id"] for e in KNOWLEDGE_BASE]
check("KB ids are unique", len(ids) == len(set(ids)), f"dupes: {[i for i in ids if ids.count(i) > 1]}")
check("every entry has answer+source", all(e.get("answer") and e.get("source") for e in KNOWLEDGE_BASE))
check("every entry has keywords", all(e.get("keywords") for e in KNOWLEDGE_BASE))

# ---- Tokeniser: single digits are kept so "2" != "3" ----------------------
check("tokeniser keeps single digits", "2" in tokenise("assignment 2"))
check("tokeniser drops stopwords", "the" not in tokenise("what is the deadline"))

# ---- Rule layer: high-confidence direct hits (A3 defaults) ----------------
r = ans("When is Assignment 3 due?")
check("A3 deadline via rule", r["type"] == "rule" and r["id"] == "a3-deadline")
check("A3 answer mentions 27th July", "27th July" in r["text"])

check("weightage rule hits A3", ans("How much is it worth?")["id"] == "a3-weightage")
check("group size rule", ans("How many students per group?")["id"] == "a3-groupsize")
check("plagiarism rule", ans("What is the turnitin similarity limit?")["id"] == "a3-plagiarism")
check("tools rule", ans("What tools can I use?")["id"] == "a3-2-tools")

# ---- Assignment disambiguation: naming a1/a2 skips generic A3 rules --------
check("A1 due routes to A1 (not A3)", ans("When is assignment 1 due?")["id"] == "a1-deadline")
check("A2 due routes to A2 (not A3)", ans("When is assignment 2 due?")["id"] == "a2-deadline")
check("A1 weightage routes to A1", ans("How much is assignment 1 worth?")["id"] == "a1-weightage")
check("A2 weightage routes to A2", ans("How much is assignment 2 worth?")["id"] == "a2-weightage")

# ---- Verified content facts -----------------------------------------------
check("A1 is individual", "INDIVIDUAL" in ans("Is assignment 1 individual or group?")["text"])
check("A1 due date correct", "3rd June 2026" in ans("assignment 1 deadline")["text"])
check("A2 is 30 percent", "30%" in ans("assignment 2 weightage")["text"])
check("A2 due week 12", "Week 12" in ans("assignment 2 due date")["text"])

# ---- Confidence gate: off-topic returns honest "unknown" ------------------
u = ans("How do I bake a chocolate cake?")
check("off-topic -> unknown", u["type"] == "unknown" and u["id"] is None)
check("empty input -> empty", ans("   ")["type"] == "empty")

# ---- Small talk -----------------------------------------------------------
check("greeting -> smalltalk", ans("hello")["type"] == "smalltalk")
check("thanks -> smalltalk", ans("thanks!")["type"] == "smalltalk")
check("greeting+question still answers", ans("hi when is assignment 3 due")["id"] == "a3-deadline")

# ---- Student FAQ (from FAQ21.docx) ----------------------------------------
check("ChatGPT -> AI policy", ans("Can I use ChatGPT for this assignment?")["id"] == "faq-ai-usage")
check("AI grammar -> AI policy", ans("Can I use AI to improve my grammar?")["id"] == "faq-ai-usage")
check("AI allowed but declared", "declare" in ans("what is the % of AI allowed?")["text"].lower())
check("AI cap is 20 percent", "20%" in ans("how much AI is allowed?")["text"])
check("A2/A3 continuous -> faq", ans("Is assignment 2 and 3 continuous?")["id"] == "faq-continuous")
check("continuous answer says yes", ans("are assignment 2 and 3 continuous?")["text"].lower().startswith("yes"))
check("referencing style routes", ans("Which referencing style should I use?")["id"] == "faq-referencing")
check("lecturer email surfaced", "Sumathi.balakrishnan@taylors.edu.my" in ans("What is your email?")["text"])
check("non-contributing -> peer review", "peer" in ans("What if my group member is not contributing?")["text"].lower())
check("change groups -> cannot", "cannot" in ans("Can I change groups next assignment?")["text"].lower())
check("no exam confirmed", ans("Do we have an exam for this module?")["text"].lower().startswith("no"))
check("only group leader submits", "leader" in ans("Who should submit the final assignment?")["text"].lower())

# ---- Tier 1: synonyms, typo tolerance, compound questions, related chips ---
check("typo 'deadlne' still finds deadline", ans("what is the deadlne for a3")["id"] == "a3-deadline")
check("synonym 'grade' -> high-mark", ans("how do i get a good grade")["id"] == "faq-high-mark")
check("synonym 'copying' -> plagiarism", ans("who checks my work for copying")["id"] == "a3-plagiarism")
check("typo 'referance' -> referencing", ans("how do i referance my sources")["id"] == "faq-referencing")

_c = engine.answer_all("how much is assignment 3 worth and when is it due?")
check("compound returns two answers", len(_c) == 2)
check("compound keeps A3 context", {r["id"] for r in _c} == {"a3-weightage", "a3-deadline"})
_c2 = engine.answer_all("when is assignment 2 due and how much is it worth?")
check("compound propagates named assignment", {r["id"] for r in _c2} == {"a2-deadline", "a2-weightage"})
check("non-compound stays single", len(engine.answer_all("When is Assignment 3 due?")) == 1)

_rel = engine.related("a3-deadline")
check("related returns suggestions", 1 <= len(_rel) <= 3)
check("related excludes the source question", "When is Assignment 3 due?" not in _rel)

# ---- Unverified note: only verified=False entries warn ----------------------
warned = any("double-check" in engine.answer(e["question"]).get("text", "")
             for e in KNOWLEDGE_BASE if e.get("verified"))
check("verified entries carry no warning", not warned)
check("unverified entries do warn",
      "double-check" in engine.answer("Can I replace my submitted file?")["text"])


print("\n" + "=" * 60)
if _failures:
    print(f"{len(_failures)} FAILED: {_failures}")
    sys.exit(1)
print("All tests passed.")
