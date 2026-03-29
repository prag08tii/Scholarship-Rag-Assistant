# ============================================================
# pages/ai_chat.py
# PURPOSE : Chat UI — uses YOUR exact backend from app.py
#
# What it imports from app.py:
#   get_answer(question)  → (answer, sources, source_type)
#   store_if_liked(question, answer)  → saves to qa_cache
#
# Your original logic (search_cache → ask_question → streaming)
# is all preserved inside app.py → get_answer()
# ============================================================

import streamlit as st
import time
import pyperclip

# ── Import YOUR backend functions ────────────────────────────
from app import get_answer, store_if_liked


# Quick-question chips shown above the input
QUICK_QUESTIONS = [
    "Scholarships for SC students?",
    "OBC scholarship income limit",
    "Engineering scholarships Maharashtra",
    "Documents for post-matric scholarship",
]


def render():
    """Renders the full AI Chat page — gold UI + your real RAG backend."""

    # ── Page header ───────────────────────────────────────────
    st.markdown("""
    <div class="chat-wrap">
      <div class="chat-top">
        <h2>ScholarPath <em style="font-style:italic;color:var(--gold2);">AI</em></h2>
        <p>Ask about eligibility, amounts, deadlines, documents — in plain language.</p>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Session state — keeps chat history across reruns ──────
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": (
                    "Namaste! 🙏 I'm ScholarPath AI.\n\n"
                    "I can help you find scholarships based on your **category** "
                    "(SC/ST/OBC/EWS), **income**, **state**, **course**, and more.\n\n"
                    "What would you like to know?"
                ),
                "question": "",
                "sources": [],
                "source_type": "rag",
            }
        ]

    # ── Quick-question chips ───────────────────────────────────
    # Shown as pill-style buttons above the chat
    cols = st.columns(len(QUICK_QUESTIONS))
    for col, question in zip(cols, QUICK_QUESTIONS):
        with col:
            if st.button(question, key=f"chip__{question}"):
                st.session_state["_prefill"] = question
                st.rerun()

    # ── Render full chat history ───────────────────────────────
    # We render each message as custom HTML bubbles (gold style)
    # but use Streamlit widgets for action buttons (they need to be real widgets)
    st.markdown('<div class="sp-chat-box">', unsafe_allow_html=True)

    for i, msg in enumerate(st.session_state.messages):

        if msg["role"] == "user":
            # ── User bubble (right side) ──
            st.markdown(f"""
            <div class="sp-msg user">
              <div class="sp-av usr">U</div>
              <div class="sp-bubble">{msg["content"]}</div>
            </div>
            """, unsafe_allow_html=True)

        else:
            # ── Assistant bubble (left side) ──
            st.markdown(f"""
            <div class="sp-msg bot">
              <div class="sp-av bot">SP</div>
              <div>
                <div class="sp-bubble">{msg["content"]}</div>
            """, unsafe_allow_html=True)

            # Source badge: cache ⚡ or RAG 📄
            if msg.get("source_type") == "cache":
                st.markdown('<span class="sp-cache-pill">⚡ From Semantic Cache</span>', unsafe_allow_html=True)
            elif msg.get("sources"):
                st.markdown('<span class="sp-src-pill">📄 Sources cited via RAG</span>', unsafe_allow_html=True)

            # Action buttons (real Streamlit widgets so they actually work)
            if i > 0:  # skip the welcome message
                btn_cols = st.columns([1, 1, 1, 1, 12])

                with btn_cols[0]:
                    if st.button("👍", key=f"like_{i}", help="Save to cache"):
                        store_if_liked(msg.get("question", ""), msg["content"])
                        st.toast("✅ Saved to cache!")

                with btn_cols[1]:
                    if st.button("👎", key=f"dislike_{i}", help="Not helpful"):
                        st.toast("Feedback noted!")

                with btn_cols[2]:
                    if st.button("📋", key=f"copy_{i}", help="Copy answer"):
                        try:
                            pyperclip.copy(msg["content"])
                            st.toast("📋 Copied!")
                        except Exception:
                            st.toast("Copy not supported in this environment")

                with btn_cols[3]:
                    if st.button("🔄", key=f"regen_{i}", help="Regenerate answer"):
                        with st.spinner("🔄 Regenerating..."):
                            new_ans, new_src, new_type = get_answer(msg.get("question", ""))
                        msg["content"]     = new_ans
                        msg["sources"]     = new_src
                        msg["source_type"] = new_type
                        st.rerun()

            # Sources expander
            if msg.get("sources") and msg["sources"] != ["⚡ From Semantic Cache"]:
                with st.expander("📄 View Sources"):
                    for s in msg["sources"]:
                        st.write(s)

            st.markdown("</div></div>", unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)  # close sp-chat-box

    # ── Handle prefill from chip click ────────────────────────
    prefill = st.session_state.pop("_prefill", "")

    # ── Chat input (native Streamlit widget — styled by CSS) ──
    user_input = st.chat_input("Ask your scholarship question...")

    query = prefill or user_input

    if query:
        # 1. Add user message to history
        st.session_state.messages.append({
            "role": "user",
            "content": query,
            "question": query,
            "sources": [],
            "source_type": "",
        })

        # 2. Show status spinners exactly like your original app.py
        col_status = st.empty()

        with st.spinner("🔎 Searching cache..."):
            time.sleep(0.4)

        with st.spinner("📚 Retrieving documents & 🧠 Generating answer..."):
            answer, sources, source_type = get_answer(query)  # ← YOUR BACKEND

        col_status.empty()

        # 3. Streaming word-by-word effect (just like your original app.py)
        placeholder = st.empty()
        streamed = ""
        for word in answer.split():
            streamed += word + " "
            placeholder.markdown(
                f'<div class="sp-bubble" style="max-width:85%;background:var(--card2);'
                f'border:0.5px solid var(--border);border-radius:12px;'
                f'padding:0.9rem 1.1rem;font-size:0.92rem;line-height:1.7;">'
                f'{streamed}▌</div>',
                unsafe_allow_html=True
            )
            time.sleep(0.015)
        placeholder.empty()

        # 4. Save complete message to session
        st.session_state.messages.append({
            "role": "assistant",
            "content": streamed.strip(),
            "question": query,
            "sources": sources,
            "source_type": source_type,
        })

        # 5. Rerun to render everything cleanly
        st.rerun()