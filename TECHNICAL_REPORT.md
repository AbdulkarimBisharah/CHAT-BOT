# ITS67404 IoT Coursework Assistant — Technical Report

*A 24/7 rule-based + retrieval chatbot that answers student questions about the
ITS67404 Internet of Things coursework — strictly from the official assignment
briefs, always citing its source, and honestly saying "I'm not sure" rather than
guessing.*

**No LLM · No API key · No paid services · Free to run and deploy.**

---

## 1. Executive summary

The assistant is a small, fully deterministic Python application (~1,190 lines
across four files). It replaces "when is this due / how much is it worth / what do
I submit" emails to the lecturer with an always-on chatbot. Every answer is drawn
from a hand-curated **knowledge base** of 42 verified facts and is shown together
with the exact brief section it came from.

Crucially, it uses **no generative AI at inference time**. Matching is done with a
transparent rule layer plus classic **TF-IDF cosine similarity** in pure Python.
This makes every answer traceable, reproducible, and free of hallucination risk —
important for an academic-integrity context where a wrong "acceptable similarity %"
or "% of AI allowed" could mislead a student.

| Metric | Value |
|---|---|
| Knowledge-base entries | 42 |
| — Assignment 1 / 2 / 3 | 6 / 6 / 14 |
| — Student FAQ / General | 15 / 1 |
| Verified vs. unverified facts | 41 verified · 1 deferred-to-lecturer |
| Total student-phrasing keywords | 438 |
| Retrieval vocabulary (unique terms) | 757 |
| Automated test assertions | 36 (all passing) |
| Runtime dependencies | 1 (`streamlit`) |
| Lines of code | app 198 · engine 246 · KB 642 · tests 101 |

---

## 2. System architecture

```
                          ┌──────────────────────────────┐
   Student question  ──►  │            app.py            │   Streamlit UI
                          │  (chat UI, chips, feedback)  │
                          └───────────────┬──────────────┘
                                          │ engine.answer(question)
                                          ▼
                          ┌──────────────────────────────┐
                          │           engine.py          │   ChatEngine
                          │  normalise → tokenise →       │
                          │  small-talk → priority rules  │
                          │  → rule layer → assignment    │
                          │  scoping → TF-IDF cosine →    │
                          │  confidence gate → pack       │
                          └───────────────┬──────────────┘
                                          │ reads at startup
                                          ▼
                          ┌──────────────────────────────┐
                          │       knowledge_base.py      │   42 fact dicts
                          │  {id, source, keywords,      │   (the only file a
                          │   question, answer, verified}│    lecturer edits)
                          └──────────────────────────────┘

   test_engine.py  ──►  36 assertions locking rule/retrieval/gate behaviour
```

**Separation of concerns is the core design principle:**

| File | Responsibility | Who edits it |
|---|---|---|
| `knowledge_base.py` | The *facts* — data only, no logic | The **lecturer** (copy a block, edit fields) |
| `engine.py` | The *matching logic* — no content | A developer, rarely |
| `app.py` | The *presentation* — UI, logging, theming | A developer, rarely |
| `test_engine.py` | Behavioural safety net | A developer, on change |

A non-programmer lecturer can add or correct any answer by editing one dict in
`knowledge_base.py`; nothing in the engine or UI needs to change.

---

## 3. Data model — the knowledge base

Each fact is a Python dict with a fixed six-field schema:

```python
{
    "id":       "a3-deadline",                      # unique slug, no spaces
    "source":   "Assignment 3 brief, cover sheet",  # shown under the answer
    "keywords": ["deadline", "due", "hand in", ...], # words students might type
    "question": "When is Assignment 3 due?",         # example (used for matching + chips)
    "answer":   "The report hand-in date is Week 15, 27th July 2026...",
    "verified": True,   # True = confirmed from brief · False = defer to lecturer
}
```

**The `verified` flag is a first-class safety feature.** When `verified` is
`False`, the engine automatically appends:

> ⚠️ Note: this detail hasn't been confirmed from a final brief yet — please
> double-check with your lecturer.

One entry is intentionally `verified: False` — `faq-submission-mechanics` (MyTIMeS
resubmit behaviour), which isn't stated in the briefs. The other lecturer-confirmed
policies are now loaded as verified facts (no exam; AI allowed but must be declared
and capped at 20%; group submissions made by the group leader only). This directly
implements the FAQ document's instruction: *"the chatbot should answer only from your
university/module's approved policy … it shouldn't invent an acceptable similarity
percentage."*

### Knowledge-base coverage

- **Assignment 1** (individual, MLO1, 30%): overview, weightage, deadline,
  requirements, deliverables, rubric.
- **Assignment 2** (group, MLO2, 30%): overview, weightage, deadline, Part 1
  (architecture/tech stack), Part 2 (algorithms/implementation), deliverables.
- **Assignment 3** (group, MLO3, 40%): overview, weightage, deadline, group size,
  A3.1–A3.4 sub-parts, tools, IEEE format, deliverables, plagiarism, rubric, MLO.
- **Student FAQ** (15, from `FAQ21.docx`): referencing, formatting/fonts, page &
  word limits, individual-vs-group, late submission, resubmit mechanics, AI usage,
  high-mark guidance, group contribution / peer review, changing groups, A2↔A3
  continuity, who submits, lecturer contact, exam, presentation details.

---

## 4. The retrieval engine (`engine.py`)

`ChatEngine.answer(question)` runs a deterministic pipeline. The first stage that
produces a confident hit wins.

### 4.1 Text normalisation & tokenisation

```
normalise():  lowercase → strip punctuation (keep [a-z0-9 .]) → collapse whitespace
tokenise():   split → drop stopwords → KEEP single digits → drop 1-char tokens
```

Keeping single digits is deliberate and important: it means **"assignment 2"** and
**"assignment 3"** tokenise differently (`2` vs `3` are preserved), so questions
about one assignment don't leak into another's answer.

A ~90-word **stopword list** removes noise words (*the, is, how, when, can, …*) so
matching focuses on content words.

### 4.2 Stage 0 — Small talk

If the *entire* message is only greetings/thanks (`hi`, `hello`, `salam`, `thanks`,
`thank you`, …), the bot replies warmly instead of running retrieval (which would
otherwise return "I'm not sure"). A greeting *plus* a real question still answers
the question.

### 4.3 Stage 1 — Priority rules (exact-token)

A small set of topic rules that must win **before** assignment scoping and before
TF-IDF, matched on exact tokens only:

| Trigger tokens | Routes to |
|---|---|
| `ai`, `chatgpt`, `gpt`, `generative`, `copilot`, `gemini`, `llm` | `faq-ai-usage` |
| `continuous`, `continuation`, `continue` | `faq-continuous` |

*Why this exists:* these two entries have long keyword lists and dilute under
TF-IDF, and the "continuous" question names *assignment 2 and 3* (which would
otherwise trigger the disambiguation skip). Exact-token matching is used here so a
short trigger like `ai` can never fire on words such as *email* or *detail*.

### 4.4 Stage 2 — Rule layer (intent patterns)

High-confidence intent patterns for the most common questions. A rule fires if
**all** words in **any** group are present:

```python
("a3-deadline",   [["deadline"], ["due"], ["when","due"], ["hand","in","date"], ...]),
("a3-weightage",  [["weightage"], ["worth"], ["how","much"], ["percent"], ...]),
("a3-plagiarism", [["plagiarism"], ["turnitin"], ["similarity"], ["copy","paste"], ...]),
...
```

**Disambiguation guard:** if the student explicitly names *another* assignment
(`a1`, `assignment 1`, `a2`, …), the generic A3 rules are skipped and the query
falls through to scoped retrieval — so "how much is **assignment 1** worth?" is not
answered by the heavily-keyworded A3 weightage entry.

### 4.5 Stage 3 — TF-IDF retrieval

The fallback for everything the rules don't catch. Standard vector-space model,
implemented from scratch (no scikit-learn):

- **Indexing (once, at startup).** Each entry becomes a document built as
  `keywords + keywords + question + answer` — i.e. **keywords are weighted double**
  so a lecturer's chosen trigger words dominate the match.
- **IDF:** `idf(t) = log((N + 1) / (df(t) + 1)) + 1` — smoothed, never zero.
- **Vector:** `weight(t) = tf(t) × idf(t)`.
- **Score:** cosine similarity between the question vector and each document vector:
  `cos(q, d) = (q · d) / (‖q‖ · ‖d‖)`.

**Assignment scoping:** if exactly one assignment is named, retrieval is restricted
to that assignment's entries (`a1-*`, `a2-*`, or `a3-*`) — a second safeguard
against cross-assignment leakage.

### 4.6 Stage 4 — Confidence gate

Two thresholds convert a raw cosine score into an honest response type:

| Best cosine score | Response type | Behaviour |
|---|---|---|
| `≥ 0.28` (**HIGH**) | `retrieval` | Answer shown directly |
| `0.12 – 0.28` | `retrieval-lowconf` | Prefixed *"I think this is what you're asking about…"* |
| `< 0.12` (**LOW**) | `unknown` | Honest fallback → "check with your lecturer / MyTIMeS"; the question is logged for the lecturer |

Every returned object is a uniform dict: `{type, text, source, confidence, id}`.

---

## 5. User interface (`app.py`)

A single-page **Streamlit** chat app:

- **Branded header** — Taylor's University red (`#E31E24`) mark, module code, and a
  green "● Online 24/7" pill.
- **Light & dark aware** — all colours are CSS variables switched via
  `@media (prefers-color-scheme: dark)`, so it's legible in either theme.
- **Suggestion chips** — six clickable starter questions shown before the first
  message, spanning all three assignments.
- **Source line** — every real answer renders a `📄 Source: …` line beneath it.
- **👍 / 👎 feedback** — `st.feedback("thumbs")` under each sourced answer, logged
  once per message.
- **🗑️ Start over** — clears the conversation.
- **Cached engine** — `@st.cache_resource` builds the TF-IDF index once per server
  process, not per message.
- **Session state** — chat history and feedback state live in `st.session_state`.

### Lightweight logging (best-effort)

Two CSV logs help the lecturer improve coverage over time, written defensively so
they can never break the chat (and silently no-op on read-only hosts):

- `unanswered_log.csv` — every question that hit the "I'm not sure" gate → reveals
  gaps to fill in the knowledge base.
- `feedback_log.csv` — timestamp, 👍/👎 rating, answer id, question.

Both are git-ignored (they are runtime data, not source).

---

## 6. Testing (`test_engine.py`)

A dependency-free test runner (`python test_engine.py`, non-zero exit on failure)
with **36 assertions** that lock the system's behaviour:

- **KB integrity** — unique ids, every entry has answer/source/keywords.
- **Tokeniser** — single digits kept, stopwords dropped.
- **Rule layer** — deadline / weightage / group-size / plagiarism / tools route
  correctly.
- **Disambiguation** — A1/A2 questions never leak to A3.
- **Content facts** — e.g. A1 is individual, A2 is 30%, A2 due Week 12.
- **Confidence gate** — off-topic → `unknown`; blank → `empty`.
- **Small talk** — greeting/thanks handled; greeting+question still answers.
- **Student FAQ** — ChatGPT → AI policy; A2/A3 continuity; referencing; lecturer
  email surfaced; non-contribution → peer review; change-groups → "cannot".
- **Honesty invariant** — verified entries never warn; unverified ones always do.

---

## 7. Deployment

Zero-cost, GitHub-driven:

1. Code lives in the GitHub repo **`AbdulkarimBisharah/CHAT-BOT`** (branch `main`).
2. **Streamlit Community Cloud** deploys `app.py` and installs `requirements.txt`.
3. Any push to `main` **auto-redeploys** the live app — so updating an answer is
   just: edit `knowledge_base.py` → commit → push.

The result is a public `https://<name>.streamlit.app` link to share with students.

---

## 8. Design trade-offs & limitations

**Why no LLM?** Determinism, zero cost, zero API keys, and — most importantly —
**zero hallucination**. In an academic-integrity setting, an invented similarity
threshold or AI policy is worse than "I don't know." The `verified` flag makes that
honesty explicit.

**Known limitations (and mitigations):**

- *Keyword/lexical matching* — no semantic understanding of synonyms the lecturer
  didn't list. *Mitigation:* rich keyword lists (438 total) + the `unanswered_log`
  feedback loop.
- *English-centric tokeniser.*
- *Facts are only as current as the briefs entered.* The `verified: False`
  mechanism keeps unconfirmed facts clearly flagged.

**Future work:** synonym expansion / light stemming; a small semantic-embedding
fallback (still local, still free); a lecturer dashboard over the two CSV logs;
multi-language support.

---

## 9. Outstanding items needing lecturer input

The lecturer has confirmed the previously-open policy questions, now loaded as
verified facts:

- **Exam:** none — the module is 100% coursework (A1/A2/A3).
- **AI use:** allowed, **but must be declared** and kept to a **maximum of 20%**.
- **Group submission:** the **group leader** submits on the group's behalf.

One item still defers to the lecturer because it isn't stated in the briefs:

1. **MyTIMeS resubmit** rules — is replacing a submitted file allowed before the
   deadline?

---

*Generated as project documentation for the ITS67404 IoT Coursework Assistant.*
