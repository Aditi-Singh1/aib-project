import streamlit as st
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client()

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Let's Chat",
    page_icon="✨",
    layout="centered"
)

# ---------------- ANIMATED CSS ---------------- #

st.markdown("""
<style>

/* Animated gradient background */

.stApp {
    background: linear-gradient(-45deg, #ffffff, #ffd6eb, #fff0f7, #ffc2e2);
    background-size: 400% 400%;
    animation: gradientBG 12s ease infinite;
    font-family: 'Segoe UI', sans-serif;
}

/* Force ALL text to black */

body, p, div, span, label {
    color: black !important;
}

/* Titles */

h1, h2, h3 {
    color: black !important;
    text-align: center;
}

/* Caption */

.css-1kyxreq {
    text-align: center;
    color: black !important;
}

/* Chat messages */

[data-testid="stChatMessage"] {
    padding: 12px;
    border-radius: 14px;
    color: black !important;
}

/* User bubble */

[data-testid="stChatMessage"]:nth-child(even) {
    background-color: #eef3ff;
}

/* Assistant bubble */

[data-testid="stChatMessage"]:nth-child(odd) {
    background-color: #fffaf2;
}

/* Input box */

textarea {
    border-radius: 12px !important;
    border: 1px solid #dddddd !important;
    color: black !important;
}

/* Chat input placeholder */

input {
    color: black !important;
}

/* Buttons */

button {
    border-radius: 10px !important;
    color: black !important;
}

/* Welcome card */

.welcome-card {
    background: white;
    padding: 28px;
    border-radius: 16px;
    border: 1px solid #eeeeee;
    box-shadow: 0px 6px 20px rgba(0,0,0,0.05);
    margin-bottom: 25px;
    color: black;
}

/* Hover effect */

.welcome-card:hover {
    transform: translateY(-3px);
    transition: 0.25s;
}

/* Gradient animation */

@keyframes gradientBG {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ---------------- #

st.title("Let's Chat")
st.caption("Tell me all about you! I'll listen")

# ---------------- WELCOME CARD ---------------- #

st.markdown("""
<div class="welcome-card">

### Welcome 👋

Start your conversation below.

</div>
""", unsafe_allow_html=True)

# ---------------- CHAT MEMORY ---------------- #

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages

for msg in st.session_state.messages:

    avatar = "👤" if msg["role"] == "user" else "🤖"

    with st.chat_message(msg["role"], avatar=avatar):
        st.markdown(msg["content"])

# ---------------- USER INPUT ---------------- #

user_input = st.chat_input("   Ask something...")

if user_input:

    with st.chat_message("user", avatar="👤"):
        st.markdown(user_input)

    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("assistant", avatar="🤖"):

        with st.spinner("Thinking..."):

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=user_input
            )

            bot_reply = response.text
            st.markdown(bot_reply)

    st.session_state.messages.append({
        "role": "assistant",
        "content": bot_reply
    })