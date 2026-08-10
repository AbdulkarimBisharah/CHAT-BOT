# How to build this with Claude Code

You have two ways to use these files with Claude Code. Pick whichever you prefer.

---

## Option A — Use the files as-is (fastest)

The project is already complete and tested. Just:

1. Put all the files (`app.py`, `engine.py`, `knowledge_base.py`, `requirements.txt`)
   in a folder.
2. Open that folder in Claude Code.
3. Tell Claude Code:

   > Run this Streamlit app locally so I can see it. Then help me deploy it free to
   > Streamlit Community Cloud via GitHub.

Claude Code will run `streamlit run app.py`, open it, and walk you through deploy.

---

## Option B — Have Claude Code build it from scratch (to learn / customise)

Paste this prompt into Claude Code in an empty folder:

---

**PROMPT TO PASTE:**

> Build a Streamlit chatbot in Python called the "ITS67404 IoT Coursework Assistant".
> It is a rule-based + retrieval chatbot for university students — NO LLM, NO API key,
> completely free to run and deploy. It answers questions about IoT course assignments
> strictly from a knowledge base, and always cites the source of each answer.
>
> Create these files:
>
> 1. `knowledge_base.py` — a Python list called `KNOWLEDGE_BASE` of dicts. Each dict has:
>    `id` (str), `source` (str), `keywords` (list of lowercase str), `question` (str),
>    `answer` (str), `verified` (bool). Add clear comments explaining how a
>    non-programmer lecturer edits it (copy a block, change fields, set verified=False
>    for unconfirmed facts).
>
> 2. `engine.py` — a `ChatEngine` class with an `answer(question)` method. Pipeline:
>    (a) normalise + tokenise the text, dropping stopwords but KEEPING single digits
>    (so "assignment 2" isn't confused with "assignment 3");
>    (b) a RULE layer of intent patterns for common questions (deadline, weightage,
>    group size, plagiarism, tools, IEEE format, deliverables, and the A3.1–A3.4
>    subsections) that returns a direct answer on a match — BUT if the question mentions
>    another assignment (a1/a2/a4), skip the generic rules and fall through to retrieval;
>    (c) a RETRIEVAL layer using TF-IDF + cosine similarity in pure Python (no sklearn),
>    with keywords weighted double;
>    (d) a CONFIDENCE gate: below a low threshold, return an honest "I'm not sure — check
>    with your lecturer/MyTIMeS" instead of guessing; between low and high thresholds,
>    prefix with "I think this is what you're asking about".
>    If an entry has verified=False, append a ⚠️ "please double-check" note to its answer.
>    Return a dict: {type, text, source, confidence, id}.
>
> 3. `app.py` — a Streamlit app: a header styled with Taylor's University red (#E31E24)
>    showing the module code; a welcome message with clickable suggestion-question
>    buttons; `st.chat_message` history; `st.chat_input`; and under each bot answer, a
>    small "Source: ..." line. Cache the engine with `@st.cache_resource`. Keep chat
>    history in `st.session_state`.
>
> 4. `requirements.txt` — just `streamlit>=1.39,<1.50`.
>
> Then run it locally and show me. After I confirm it works, help me deploy it free to
> Streamlit Community Cloud.
>
> Seed the knowledge base with this VERIFIED content from the ITS67404 Assignment 3 brief:
> - Assignment 3 is a group assignment, worth 40%, split into A3.1/A3.2/A3.3/A3.4 (10% each).
> - Report due Week 15, 27th July 2026; presentations from 10th July; handed out 29th May 2026; late = mark deductions.
> - Groups of 3–5 students; cover sheet with names + IDs + group leader is the first page.
> - A3.1 (10%): manage resources & potential risks of the A2 IoT idea; expandability, risk reduction, with citations.
> - A3.2 (10%): proof of concept; attach a working Tinkercad/Wokwi link; demo in presentation; photos + slides folder.
> - A3.2 tools: Tinkercad, Wokwi, Cisco Packet Tracer, Figma, Grafana, ThingSpeak, Google Cloud, Google Colab.
> - A3.3 (10%): presentation in PowerPoint/Canva; all members present; 20–30 min (30 incl. demo); standard outline.
> - A3.4 (10%): IEEE-format manuscript, max 6 pages; Turnitin similarity below 20%; marks lost for wrong formatting.
> - Deliverables: PDF to MyTIMeS — manuscript, assignment with cover page, Turnitin report (<20%); slides to slides folder.
> - Plagiarism forbidden; copy-paste = plagiarism; min penalty loss of marks, can be 0 and cause course failure.
> - Rubric: 4 criteria × 10 marks (Outstanding 9–10 / Mastering 6–8 / Developing 4–5 / Beginning 0–3).
> - MLO3: construct an IoT system with appropriate tools while cooperating in a group.
>
> Mark this Assignment 2 content as verified=False (from template only, needs confirmation):
> - Assignment 2 is a group assignment (MLO2): design IoT architecture + algorithms. Part 1 architecture/tech stack, Part 2 algorithms/implementation. Template lists 30% (15%+15%), hand-in Week 12 Friday.

---

## Adding your other assignments later

Once you have the Assignment 1 brief (and a confirmed Assignment 2 brief), either edit
`knowledge_base.py` yourself (copy a block, fill it in), or tell Claude Code:

> Add these assignment details to knowledge_base.py as new verified entries: [paste the
> brief details].
