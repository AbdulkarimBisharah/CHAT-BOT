"""
============================================================================
ITS67404 IoT COURSEWORK ASSISTANT - Streamlit app
Run locally:   streamlit run app.py
============================================================================
"""

import csv
import datetime as _dt
from pathlib import Path

import streamlit as st

from knowledge_base import KNOWLEDGE_BASE
from engine import ChatEngine

# ---- Page config ----------------------------------------------------------
st.set_page_config(
    page_title="ITS67404 IoT Coursework Assistant",
    page_icon="🎓",
    layout="centered",
)

# ---- Styling (Taylor's red accent, light + dark aware) --------------------
st.markdown("""
<style>
  :root {
    --tu-red: #E31E24;
    --tu-border: #e6e8ec;
    --tu-title: #1a1c20;
    --tu-sub: #4a4f57;
    --tu-source: #6b7280;
    --tu-source-border: #ececf0;
    --tu-chip-bg: #fdecec;
    --tu-chip-border: #f6d5d6;
  }
  @media (prefers-color-scheme: dark) {
    :root {
      --tu-border: #33363d;
      --tu-title: #f0f2f6;
      --tu-sub: #b7bcc5;
      --tu-source: #a3a9b3;
      --tu-source-border: #33363d;
      --tu-chip-bg: #3a1e1f;
      --tu-chip-border: #5a2b2c;
    }
  }
  .block-container { padding-top: 3.5rem; max-width: 780px; }
  .tu-header {
    display: flex; align-items: center; gap: 14px; padding-bottom: 6px;
    border-bottom: 1px solid var(--tu-border); margin-bottom: 4px;
  }
  .tu-mark {
    width: 42px; height: 42px; border-radius: 10px; flex: none; display: grid;
    place-items: center; color: #fff; font-weight: 800; font-size: 19px;
    background: linear-gradient(135deg, #E31E24, #B31419);
    box-shadow: 0 2px 8px rgba(227,30,36,.3);
  }
  .tu-title { font-weight: 700; font-size: 16px; line-height: 1.2; color: var(--tu-title); }
  .tu-sub { font-size: 12px; color: var(--tu-sub); }
  .tu-pill {
    margin-left: auto; font-size: 12px; color: #16794a; background: #e8f7ee;
    border: 1px solid #bfe6cf; padding: 4px 11px; border-radius: 999px;
  }
  .tu-source {
    margin-top: 6px; font-size: 12px; color: var(--tu-source);
    border-top: 1px solid var(--tu-source-border); padding-top: 6px;
  }
  .stButton>button {
    background: var(--tu-chip-bg); color: var(--tu-red); border: 1px solid var(--tu-chip-border);
    border-radius: 999px; font-size: 13px; padding: 6px 12px;
  }
  .stButton>button:hover { border-color: var(--tu-red); color: var(--tu-red); }
</style>
""", unsafe_allow_html=True)

# ---- Header ---------------------------------------------------------------
st.markdown("""
<div class="tu-header">
  <div class="tu-mark">T</div>
  <div>
    <div class="tu-title">IoT Coursework Assistant</div>
    <div class="tu-sub">ITS67404 · Internet of Things · Taylor's University</div>
  </div>
  <div class="tu-pill">● Online 24/7</div>
</div>
""", unsafe_allow_html=True)

# ---- Engine (built once, cached) ------------------------------------------
@st.cache_resource
def get_engine():
    return ChatEngine(KNOWLEDGE_BASE)

engine = get_engine()

SUGGESTIONS = [
    "When is Assignment 1 due?",
    "Is Assignment 1 individual or group?",
    "How much is Assignment 2 worth?",
    "When is Assignment 3 due?",
    "What tools can I use for the proof of concept?",
    "What's the plagiarism policy?",
]

# ---- Lightweight logging (helps the lecturer spot gaps) -------------------
# Best-effort only: on read-only hosts these simply no-op.
LOG_DIR = Path(__file__).parent


def _append_csv(filename: str, header, row):
    try:
        path = LOG_DIR / filename
        new = not path.exists()
        with path.open("a", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            if new:
                w.writerow(header)
            w.writerow(row)
    except Exception:
        pass  # never let logging break the chat


def log_unanswered(question: str):
    _append_csv("unanswered_log.csv", ["timestamp", "question"],
                [_dt.datetime.now().isoformat(timespec="seconds"), question])


def log_feedback(question: str, answer_id, rating: str):
    _append_csv("feedback_log.csv", ["timestamp", "rating", "answer_id", "question"],
                [_dt.datetime.now().isoformat(timespec="seconds"), rating,
                 answer_id or "", question])


# ---- Session state --------------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []
if "fb_logged" not in st.session_state:
    st.session_state.fb_logged = set()


def handle(question: str):
    st.session_state.messages.append({"role": "user", "content": question})
    result = engine.answer(question)
    if result.get("type") == "unknown":
        log_unanswered(question)
    st.session_state.messages.append({
        "role": "assistant",
        "content": result["text"],
        "source": result.get("source"),
        "id": result.get("id"),
        "question": question,
    })


# ---- Welcome + suggestion chips (only before first message) ---------------
if not st.session_state.messages:
    st.markdown(
        "#### Hi 👋 I'm your IoT coursework assistant\n"
        "Ask me about deadlines, weightage, formats, tools, or what each assignment "
        "needs. I answer from the official ITS67404 briefs (Assignments 1, 2 & 3) and "
        "always show the source."
    )
    st.write("")
    cols = st.columns(2)
    for i, q in enumerate(SUGGESTIONS):
        if cols[i % 2].button(q, key=f"sug_{i}", use_container_width=True):
            handle(q)
            st.rerun()
else:
    # Start-over control once a conversation is under way.
    _, right = st.columns([4, 1])
    if right.button("🗑️ Start over", key="reset", use_container_width=True):
        st.session_state.messages = []
        st.session_state.fb_logged = set()
        st.rerun()

# ---- Render chat history --------------------------------------------------
for idx, msg in enumerate(st.session_state.messages):
    with st.chat_message(msg["role"], avatar="🎓" if msg["role"] == "assistant" else "🧑‍💻"):
        st.markdown(msg["content"])
        if msg.get("source"):
            st.markdown(f'<div class="tu-source">📄 Source: {msg["source"]}</div>',
                        unsafe_allow_html=True)
        # Thumbs feedback under each assistant answer that has a real source.
        if msg["role"] == "assistant" and msg.get("source"):
            rating = st.feedback("thumbs", key=f"fb_{idx}")
            if rating is not None and idx not in st.session_state.fb_logged:
                log_feedback(msg.get("question", ""), msg.get("id"),
                             "up" if rating == 1 else "down")
                st.session_state.fb_logged.add(idx)

# ---- Input ----------------------------------------------------------------
prompt = st.chat_input("Ask about the IoT coursework…")
if prompt:
    handle(prompt)
    st.rerun()

st.caption("Guidance only · always confirm final details with your lecturer or MyTIMeS")
