"""
============================================================================
ITS67404 IoT COURSEWORK ASSISTANT - Streamlit app
Run locally:   streamlit run app.py
============================================================================
"""

import streamlit as st
from knowledge_base import KNOWLEDGE_BASE
from engine import ChatEngine

# ---- Page config ----------------------------------------------------------
st.set_page_config(
    page_title="ITS67404 IoT Coursework Assistant",
    page_icon="🎓",
    layout="centered",
)

# ---- Styling (Taylor's red accent) ----------------------------------------
st.markdown("""
<style>
  :root { --tu-red: #E31E24; }
  .block-container { padding-top: 3.5rem; max-width: 780px; }
  .tu-header {
    display: flex; align-items: center; gap: 14px; padding-bottom: 6px;
    border-bottom: 1px solid #e6e8ec; margin-bottom: 4px;
  }
  .tu-mark {
    width: 42px; height: 42px; border-radius: 10px; flex: none; display: grid;
    place-items: center; color: #fff; font-weight: 800; font-size: 19px;
    background: linear-gradient(135deg, #E31E24, #B31419);
    box-shadow: 0 2px 8px rgba(227,30,36,.3);
  }
  .tu-title { font-weight: 700; font-size: 16px; line-height: 1.2; color: #1a1c20; }
  .tu-sub { font-size: 12px; color: #4a4f57; }
  .tu-pill {
    margin-left: auto; font-size: 12px; color: #16794a; background: #e8f7ee;
    border: 1px solid #bfe6cf; padding: 4px 11px; border-radius: 999px;
  }
  .tu-source {
    margin-top: 6px; font-size: 12px; color: #6b7280;
    border-top: 1px solid #ececf0; padding-top: 6px;
  }
  .stButton>button {
    background: #fdecec; color: #b31419; border: 1px solid #f6d5d6;
    border-radius: 999px; font-size: 13px; padding: 6px 12px;
  }
  .stButton>button:hover { background: #fbdede; border-color: #f0bcbd; color: #b31419; }
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
    "When is Assignment 3 due?",
    "How much is Assignment 3 worth?",
    "What format does the manuscript need?",
    "What tools can I use for the proof of concept?",
    "How many students per group?",
    "What's the plagiarism policy?",
]

# ---- Session state --------------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

def handle(question: str):
    st.session_state.messages.append({"role": "user", "content": question})
    result = engine.answer(question)
    st.session_state.messages.append({
        "role": "assistant",
        "content": result["text"],
        "source": result.get("source"),
    })

# ---- Welcome + suggestion chips (only before first message) ---------------
if not st.session_state.messages:
    st.markdown(
        "#### Hi 👋 I'm your IoT coursework assistant\n"
        "Ask me about deadlines, weightage, formats, tools, or what each assignment "
        "needs. I answer from the official ITS67404 briefs and always show the source."
    )
    st.write("")
    cols = st.columns(2)
    for i, q in enumerate(SUGGESTIONS):
        if cols[i % 2].button(q, key=f"sug_{i}", use_container_width=True):
            handle(q)
            st.rerun()

# ---- Render chat history --------------------------------------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"], avatar="🎓" if msg["role"] == "assistant" else "🧑‍💻"):
        st.markdown(msg["content"])
        if msg.get("source"):
            st.markdown(f'<div class="tu-source">📄 Source: {msg["source"]}</div>',
                        unsafe_allow_html=True)

# ---- Input ----------------------------------------------------------------
prompt = st.chat_input("Ask about the IoT coursework…")
if prompt:
    handle(prompt)
    st.rerun()

st.caption("Guidance only · always confirm final details with your lecturer or MyTIMeS")
