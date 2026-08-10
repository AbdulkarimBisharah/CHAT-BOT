# ITS67404 IoT Coursework Assistant (Streamlit / Python)

A 24/7 student chatbot that answers questions about the ITS67404 Internet of Things
coursework — deadlines, weightage, formats, tools, and what each assignment needs.
It answers **only** from the official assignment briefs and always shows the source.
When it isn't sure, it says so instead of guessing.

**No API key. No paid services. Free to run and deploy.**

## How it works (rule + retrieval, no LLM)

- **Rule layer** — common questions (deadlines, weightage, group size, plagiarism,
  tools) are matched directly for instant, exact answers.
- **Retrieval layer** — anything else is matched against the knowledge base using
  TF-IDF cosine similarity, in pure Python (no ML libraries).
- **Confidence gate** — if nothing matches well, it returns an honest "I'm not sure"
  and points the student to the lecturer / MyTIMeS.

## Files

| File | What it is |
|------|-----------|
| `app.py` | The Streamlit app (UI) |
| `knowledge_base.py` | **The knowledge base — this is the only file you edit** |
| `engine.py` | The matching engine (no need to touch) |
| `requirements.txt` | Python dependency (Streamlit) |

## Run it locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

It opens at http://localhost:8501

## Deploy for free (Streamlit Community Cloud)

1. Put this folder in a **GitHub repo** (public or private).
2. Go to https://share.streamlit.io and sign in with GitHub.
3. Click **New app**, pick your repo, set the main file to `app.py`, and Deploy.
4. You get a public link like `https://your-app.streamlit.app`. Done.

To update later: edit `knowledge_base.py`, push to GitHub — the app redeploys
automatically.

## How to add or change answers (lecturer guide)

Open `knowledge_base.py`. Each answer is a small block like this:

```python
{
    "id": "a3-deadline",
    "source": "Assignment 3 brief, cover sheet",
    "keywords": ["deadline", "due", "when due", "hand in"],
    "question": "When is Assignment 3 due?",
    "answer": "The report hand-in date is Week 15, 27th July 2026...",
    "verified": True,
},
```

- To **change** an answer: edit the `"answer"` text.
- To **add** a new assignment: copy any block, paste it, give it a new `"id"`, and
  fill in the fields. Set `"verified": False` until you've confirmed it from the real
  brief — the bot then shows a "please double-check" note automatically.
- `"keywords"` are the words students might type. More keywords = easier to find.

Save the file (and push to GitHub if deployed). Nothing else needs to change.

## What's already loaded

- **Assignment 3** — fully loaded and verified from the official brief.
- **Assignment 2** — partial (from the template only); marked unverified.
- **Assignment 1 and others** — not yet added (placeholder block is in the file).
