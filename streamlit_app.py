import streamlit as st
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client()

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Aditi's Chatbot",
    page_icon="✨",
    layout="centered"
)

# ---------------- STYLING ---------------- #

st.markdown("""
<style>

/* ---------- MAIN BACKGROUND ---------- */

.stApp {
    background: linear-gradient(-45deg,
        #1f2937,
        #2b2b38,
        #3b2a5a,
        #202030
    );
    background-size: 400% 400%;
    animation: gradientBG 18s ease infinite;
    font-family: 'Segoe UI', sans-serif;
}

/* Animated gradient */

@keyframes gradientBG {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

/* ---------- GLOBAL TEXT ---------- */

h1, h2, h3, p, div, span, label {
    color: #f1f1f1 !important;
}

/* Title styling */

h1 {
    text-align: center;
    font-weight: 600;
    letter-spacing: 1px;
}

/* Caption */

.css-1kyxreq {
    text-align: center;
    color: #cfcfe6 !important;
}

/* ---------- CHAT BUBBLES ---------- */

[data-testid="stChatMessage"] {
    padding: 14px;
    border-radius: 16px;
    backdrop-filter: blur(6px);
}

/* User bubble */

[data-testid="stChatMessage"]:nth-child(even) {
    background: rgba(120, 100, 255, 0.15);
    border: 1px solid rgba(120, 100, 255, 0.3);
}

/* Bot bubble */

[data-testid="stChatMessage"]:nth-child(odd) {
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,255,255,0.1);
}

/* ---------- INPUT BOX ---------- */

textarea {
    border-radius: 12px !important;
    background-color: #0b0b12 !important;
    border: 1px solid #3c2b6e !important;
    color: white !important;
}

/* Placeholder */

textarea::placeholder {
    color: #aaaaaa !important;
}

/* ---------- BUTTON ---------- */

button {
    border-radius: 10px !important;
}

/* ---------- WELCOME CARD ---------- */

.welcome-card {
    background: rgba(255,255,255,0.05);
    padding: 28px;
    border-radius: 18px;
    border: 1px solid rgba(255,255,255,0.1);
    backdrop-filter: blur(12px);
    box-shadow: 0px 10px 35px rgba(0,0,0,0.6);
    margin-bottom: 30px;
}

/* Hover */

.welcome-card:hover {
    transform: translateY(-4px);
    transition: 0.25s ease;
}

/* ---------- SCROLLBAR ---------- */

::-webkit-scrollbar {
    width: 6px;
}

::-webkit-scrollbar-thumb {
    background: #6b4eff;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ---------------- #

st.title("Aditi's AI Assistant")
st.caption("A calm space for conversations")

# ---------------- WELCOME CARD ---------------- #

st.markdown("""
<div class="welcome-card">

### Welcome ✨

Ask anything, explore ideas, or simply chat.

Your AI assistant is ready.

</div>
""", unsafe_allow_html=True)

# ---------------- CHAT MEMORY ---------------- #

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display messages

for msg in st.session_state.messages:

    avatar = "👤" if msg["role"] == "user" else "✨"

    with st.chat_message(msg["role"], avatar=avatar):
        st.markdown(msg["content"])

# ---------------- USER INPUT ---------------- #

user_input = st.chat_input("Ask something...")

if user_input:

    with st.chat_message("user", avatar="👤"):
        st.markdown(user_input)

    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("assistant", avatar="✨"):

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