import streamlit as st

from src.chatbot import ChatbotError, get_bot_reply
from src.prompts import PROMPT_MODES


st.set_page_config(
    page_title="Mental Health Support Chatbot",
    page_icon="",
    layout="centered",
)

st.title("Mental Health Support Chatbot")
st.caption(
    "This chatbot provides general emotional support. It does not diagnose, "
    "prescribe medicine, or replace professional care."
)

if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar:
    st.header("Settings")
    prompt_mode = st.selectbox(
        "Prompt style",
        options=list(PROMPT_MODES.keys()),
        format_func=lambda mode: PROMPT_MODES[mode]["label"],
    )
    model_name = st.text_input("Ollama model", value="mistral")
    st.caption("Run locally with: streamlit run app.py")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_question = st.chat_input("Ask a mental-health-related question")

if user_question:
    st.session_state.messages.append({"role": "user", "content": user_question})

    with st.chat_message("user"):
        st.write(user_question)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                answer = get_bot_reply(
                    user_question=user_question,
                    prompt_mode=prompt_mode,
                    model_name=model_name,
                )
            except ChatbotError as exc:
                answer = str(exc)

        st.write(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})
