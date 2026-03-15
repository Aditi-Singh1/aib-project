import streamlit as st
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client()

st.title("Gemini AI Chatbot")

# store conversation
if "messages" not in st.session_state:
    st.session_state.messages = []

# display previous messages
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# user input
user_input = st.chat_input("Ask something...")

if user_input:
    # show user message
    st.chat_message("user").write(user_input)

    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    # get response from Gemini
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=user_input
    )

    bot_reply = response.text

    st.chat_message("assistant").write(bot_reply)

    st.session_state.messages.append({
        "role": "assistant",
        "content": bot_reply
    })