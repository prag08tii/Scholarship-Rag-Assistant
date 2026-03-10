import streamlit as st
import time
from rag_engine import ask_question

st.set_page_config(page_title="Scholarship AI Assistant", page_icon="🎓")

st.title("🎓 Scholarship AI Assistant")
st.caption("Ask questions about scholarships and student schemes")

# chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# show previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])


question = st.chat_input("Ask your scholarship question...")

if question:

    st.session_state.messages.append({"role": "user", "content": question})

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):

        status = st.empty()

        status.info("🔎 Searching your question...")
        time.sleep(1)

        status.info("📚 Looking for related scholarship documents...")
        time.sleep(1)

        status.info("🧠 Gathering relevant information...")
        time.sleep(1)

        status.info("⚡ Generating AI response...")
        
        answer, sources = ask_question(question)

        status.empty()

        # Typing animation
        message_placeholder = st.empty()
        full_response = ""

        words = answer.split()

        for word in words:
            full_response += word + " "
            message_placeholder.markdown(full_response + "▌")
            time.sleep(0.03)

        message_placeholder.markdown(full_response)

        # Sources
        with st.expander("📄 Sources"):
            for s in sources:
                st.write(s)

    st.session_state.messages.append({"role": "assistant", "content": full_response})