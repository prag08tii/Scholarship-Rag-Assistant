import streamlit as st
import time
import pyperclip
from app import get_answer, store_if_liked

QUICK_QUESTIONS = [
    "Scholarships for SC students?",
    "OBC scholarship income limit",
    "Engineering scholarships Maharashtra",
    "Documents for post-matric scholarship",
]

def render():
    # ── All CSS inline so it works on deployment too ──────────
    st.markdown("""
<style>
/* ── Page wrapper — centers everything ── */
.chat-page{max-width:780px;margin:0 auto;padding:2rem 1.5rem 6rem;margin-top:68px}

/* ── Header ── */
.chat-header{text-align:center;margin-bottom:2rem}
.chat-header h2{font-family:var(--font-display);font-size:2.4rem;font-weight:300;color:var(--text)}
.chat-header h2 em{font-style:italic;color:var(--gold2)}
.chat-header p{color:var(--muted2);font-size:.95rem;margin-top:.5rem}

/* ── Outer card that holds all messages ── */
.chat-card{background:var(--card);border:.5px solid var(--border);border-radius:16px;padding:1.5rem;display:flex;flex-direction:column;gap:1.25rem;margin-bottom:1rem}

/* ── Individual message row ── */
.sp-msg{display:flex;gap:.75rem;align-items:flex-start}
.sp-msg.user{flex-direction:row-reverse}

/* ── Avatars ── */
.sp-av{width:34px;height:34px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:.72rem;font-weight:600;flex-shrink:0;font-family:var(--font-display)}
.sp-av.bot{background:var(--goldF);border:.5px solid var(--border2);color:var(--gold2)}
.sp-av.usr{background:rgba(79,142,247,.15);border:.5px solid rgba(79,142,247,.3);color:var(--blue)}

/* ── Bubbles ── */
.sp-bubble{background:var(--card2);border:.5px solid var(--border);border-radius:12px;padding:.9rem 1.1rem;font-size:.92rem;line-height:1.7;color:var(--text);max-width:85%}
.sp-msg.user .sp-bubble{background:var(--goldF);border-color:var(--border2)}

/* ── Source / cache badge ── */
.sp-src-pill{display:inline-block;margin-top:.5rem;font-size:.72rem;color:var(--teal);border:.5px solid rgba(45,212,191,.25);border-radius:999px;padding:.2rem .75rem}
.sp-cache-pill{display:inline-block;margin-top:.5rem;font-size:.72rem;color:var(--gold2);border:.5px solid var(--border2);border-radius:999px;padding:.2rem .75rem}

/* ── Quick chip buttons ── */
div.stButton > button{
  background:var(--card2) !important;
  border:.5px solid var(--border) !important;
  color:var(--muted2) !important;
  border-radius:999px !important;
  font-family:var(--font-body) !important;
  font-size:.78rem !important;
  padding:.4rem .9rem !important;
  transition:color .2s,border-color .2s !important;
  white-space:nowrap !important;
}
div.stButton > button:hover{
  color:var(--gold2) !important;
  border-color:var(--gold) !important;
  background:var(--goldF) !important;
}

/* ── Action buttons (like/dislike/copy/regen) ── */
.act-row{display:flex;gap:.35rem;margin-top:.5rem;flex-wrap:wrap}
.act-pill{font-size:.78rem;padding:.25rem .55rem;border-radius:6px;background:var(--card2);border:.5px solid var(--border);color:var(--muted);cursor:pointer}

/* ── Streamlit chat input ── */
[data-testid="stChatInput"]{background:var(--card) !important;border:.5px solid var(--border) !important;border-radius:12px !important}
[data-testid="stChatInput"] textarea{background:transparent !important;color:var(--text) !important;font-family:var(--font-body) !important}
[data-testid="stChatInput"] button{background:var(--gold) !important;border-radius:8px !important}

/* ── Streamlit expander ── */
[data-testid="stExpander"]{background:var(--card) !important;border:.5px solid var(--border) !important;border-radius:8px !important}
[data-testid="stExpander"] summary{color:var(--teal) !important;font-size:.82rem !important}
</style>
""", unsafe_allow_html=True)

    # ── Session state ─────────────────────────────────────────
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": "Namaste! 🙏 I'm ScholarPath AI.\n\nI can help you find scholarships based on your **category** (SC/ST/OBC/EWS), **income**, **state**, **course**, and more.\n\nWhat would you like to know?",
                "question": "",
                "sources": [],
                "source_type": "rag",
            }
        ]

    # ── Page header ───────────────────────────────────────────
    st.markdown("""
<div class="chat-page">
  <div class="chat-header">
    <h2>ScholarPath <em>AI</em></h2>
    <p>Ask about eligibility, amounts, deadlines, documents — in plain language.</p>
  </div>
</div>
""", unsafe_allow_html=True)

    # ── Quick chips (centered, pill style) ───────────────────
    cols = st.columns(len(QUICK_QUESTIONS))
    for col, question in zip(cols, QUICK_QUESTIONS):
        with col:
            if st.button(question, key=f"chip__{question}"):
                st.session_state["_prefill"] = question
                st.rerun()

    # ── Chat messages inside a card ───────────────────────────
    st.markdown('<div style="max-width:780px;margin:1rem auto 0;padding:0 1.5rem"><div class="chat-card">', unsafe_allow_html=True)

    for i, msg in enumerate(st.session_state.messages):
        if msg["role"] == "user":
            st.markdown(f"""
<div class="sp-msg user">
  <div class="sp-av usr">U</div>
  <div class="sp-bubble">{msg["content"]}</div>
</div>""", unsafe_allow_html=True)

        else:
            st.markdown(f"""
<div class="sp-msg bot">
  <div class="sp-av bot">SP</div>
  <div>
    <div class="sp-bubble">{msg["content"]}</div>
    {'<span class="sp-cache-pill">&#9889; From Semantic Cache</span>' if msg.get("source_type") == "cache" else '<span class="sp-src-pill">&#128196; Sources cited via RAG</span>' if msg.get("sources") else ""}
  </div>
</div>""", unsafe_allow_html=True)

            # Action buttons for non-welcome messages
            if i > 0:
                btn_cols = st.columns([1, 1, 1, 1, 12])
                with btn_cols[0]:
                    if st.button("👍", key=f"like_{i}", help="Save to cache"):
                        store_if_liked(msg.get("question", ""), msg["content"])
                        st.toast("✅ Saved to cache!")
                with btn_cols[1]:
                    if st.button("👎", key=f"dislike_{i}", help="Not helpful"):
                        st.toast("Feedback noted!")
                with btn_cols[2]:
                    if st.button("📋", key=f"copy_{i}", help="Copy"):
                        try:
                            pyperclip.copy(msg["content"])
                            st.toast("📋 Copied!")
                        except Exception:
                            st.toast("Copy not supported here")
                with btn_cols[3]:
                    if st.button("🔄", key=f"regen_{i}", help="Regenerate"):
                        with st.spinner("Regenerating..."):
                            new_ans, new_src, new_type = get_answer(msg.get("question", ""))
                        msg["content"] = new_ans
                        msg["sources"] = new_src
                        msg["source_type"] = new_type
                        st.rerun()

            # Sources expander
            if msg.get("sources") and msg["sources"] != ["⚡ From Semantic Cache"]:
                with st.expander("📄 View Sources"):
                    for s in msg["sources"]:
                        st.write(s)

    st.markdown('</div></div>', unsafe_allow_html=True)  # close chat-card + wrapper

    # ── Handle chip prefill ───────────────────────────────────
    prefill = st.session_state.pop("_prefill", "")

    # ── Chat input ────────────────────────────────────────────
    # Wrap in a centered container
    st.markdown('<div style="max-width:780px;margin:0 auto;padding:0 1.5rem">', unsafe_allow_html=True)
    user_input = st.chat_input("Ask your scholarship question...")
    st.markdown('</div>', unsafe_allow_html=True)

    query = prefill or user_input

    if query:
        st.session_state.messages.append({
            "role": "user",
            "content": query,
            "question": query,
            "sources": [],
            "source_type": "",
        })

        with st.spinner("🔎 Searching cache..."):
            time.sleep(0.4)
        with st.spinner("📚 Retrieving & generating answer..."):
            answer, sources, source_type = get_answer(query)

        # Streaming effect
        placeholder = st.empty()
        streamed = ""
        for word in answer.split():
            streamed += word + " "
            placeholder.markdown(
                f'<div style="max-width:780px;margin:0 auto;padding:0 1.5rem">'
                f'<div class="sp-bubble">{streamed}&#9646;</div></div>',
                unsafe_allow_html=True
            )
            time.sleep(0.015)
        placeholder.empty()

        st.session_state.messages.append({
            "role": "assistant",
            "content": streamed.strip(),
            "question": query,
            "sources": sources,
            "source_type": source_type,
        })

        st.rerun()