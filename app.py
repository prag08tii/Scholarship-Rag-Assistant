import streamlit as st
import time
import pyperclip

from rag_engine import ask_question
from semantic_cache import search_cache, store_if_liked

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(page_title="Scholarship AI Assistant", page_icon="🎓", layout="centered")

# -----------------------------
# CSS (CLEAN DARK UI)
# -----------------------------
st.markdown("""
<style>
body {
    background-color: #0e1117;
    color: white;
}

.icon-btn {
    cursor: pointer;
    width: 18px;
    height: 18px;
    fill: gray;
}

.icon-btn:hover {
    fill: #00adb5;
    transform: scale(1.2);
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# HEADER
# -----------------------------
st.title("🎓 Scholarship AI Assistant")
st.caption("Ask questions about scholarships and student schemes")

# -----------------------------
# SESSION STATE
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------
# DISPLAY CHAT HISTORY
# -----------------------------
for i, msg in enumerate(st.session_state.messages):

    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

        if msg["role"] == "assistant":

            cols = st.columns([1,1,1,10])

            with cols[0]:
                if st.button("👍", key=f"like_{i}"):
                    store_if_liked(msg["question"], msg["content"])
                    st.toast("Saved!")

            with cols[1]:
                if st.button("📋", key=f"copy_{i}"):
                    pyperclip.copy(msg["content"])
                    st.toast("Copied!")

            with cols[2]:
                if st.button("🔄", key=f"regen_{i}"):
                    new_ans, new_src = ask_question(msg["question"])
                    msg["content"] = new_ans
                    msg["sources"] = new_src
                    st.rerun()

        if msg.get("sources"):
            with st.expander("📄 Sources"):
                for s in msg["sources"]:
                    st.write(s)

# -----------------------------
# USER INPUT
# -----------------------------
question = st.chat_input("Ask your scholarship question...")

if question:

    # USER MESSAGE
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.markdown(question)

    # ASSISTANT RESPONSE
    with st.chat_message("assistant"):

        status = st.empty()

        # -----------------------------
        # STEP 1: CACHE SEARCH
        # -----------------------------
        with st.spinner("🔎 Searching cache..."):
            time.sleep(0.5)
            cache = search_cache(question)

        if cache:
            answer = cache["answer"]
            sources = ["⚡ From Cache"]
            status.success("⚡ Answer from Cache")

        else:
            # -----------------------------
            # STEP 2: RETRIEVAL
            # -----------------------------
            with st.spinner("📚 Retrieving documents..."):
                time.sleep(0.7)

            # -----------------------------
            # STEP 3: GENERATION
            # -----------------------------
            with st.spinner("🧠 Generating answer..."):
                answer, sources = ask_question(question)

            status.success("📄 Answer from RAG")

        time.sleep(0.5)
        status.empty()

        # -----------------------------
        # STREAMING RESPONSE
        # -----------------------------
        placeholder = st.empty()
        full = ""

        for word in answer.split():
            full += word + " "
            placeholder.markdown(full + "▌")
            time.sleep(0.015)

        placeholder.markdown(full)

        # -----------------------------
        # ACTION BUTTONS (LEFT)
        # -----------------------------
        cols = st.columns([1,1,1,10])

        with cols[0]:
            if st.button("👍", key="like_new"):
                store_if_liked(question, full)
                st.toast("Saved to memory!")

        with cols[1]:
            if st.button("📋", key="copy_new"):
                pyperclip.copy(full)
                st.toast("Copied!")

        with cols[2]:
            if st.button("🔄", key="regen_new"):
                with st.spinner("Regenerating..."):
                    new_ans, new_src = ask_question(question)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": new_ans,
                    "question": question,
                    "sources": new_src
                })

                st.rerun()

        # -----------------------------
        # SAVE MESSAGE
        # -----------------------------
        st.session_state.messages.append({
            "role": "assistant",
            "content": full,
            "question": question,
            "sources": sources
        })

        # -----------------------------
        # SOURCES
        # -----------------------------
        with st.expander("📄 Sources"):
            for s in sources:
                st.write(s)