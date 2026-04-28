import os
import requests
import streamlit as st
from dotenv import load_dotenv
from google import genai

# Load .env
load_dotenv()

# Environment Variables
FIREBASE_API_KEY = os.getenv("FIREBASE_API_KEY")
GCP_PROJECT_ID = os.getenv("GCP_PROJECT_ID", "lustrous-drake-412814")
GCP_REGION = os.getenv("GCP_REGION", "us-central1")

FIREBASE_SIGNUP = f"https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={FIREBASE_API_KEY}"
FIREBASE_LOGIN = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={FIREBASE_API_KEY}"

# Gemini Client
client = genai.Client(
    vertexai=True,
    project=GCP_PROJECT_ID,
    location=GCP_REGION
)

# Page Config
st.set_page_config(
    page_title="LinuxandK8s",
    page_icon="🤖",
    layout="wide"
)

# Session Defaults
if "user" not in st.session_state:
    st.session_state.user = None

# ---------- AUTH FUNCTIONS ----------
def signup(email, password):
    payload = {
        "email": email,
        "password": password,
        "returnSecureToken": True
    }
    return requests.post(FIREBASE_SIGNUP, json=payload).json()

def login(email, password):
    payload = {
        "email": email,
        "password": password,
        "returnSecureToken": True
    }
    return requests.post(FIREBASE_LOGIN, json=payload).json()

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>
.main {background-color:#0f172a;}
.block-container {padding-top:2rem;}
h1,h2,h3 {color:#22d3ee;}
.stButton>button {
    background:#06b6d4;
    color:white;
    border-radius:10px;
    padding:0.5rem 1rem;
}
</style>
""", unsafe_allow_html=True)

# ---------- LOGIN SCREEN ----------
if not st.session_state.user:
    st.title("🔐 LinuxandK8s GenAI Portal")

    tab1, tab2 = st.tabs(["Login", "Signup"])

    with tab1:
        email = st.text_input("Email", key="login_email")
        password = st.text_input("Password", type="password", key="login_password")

        if st.button("Login"):
            if not email or not password:
                st.warning("Enter email and password")
            else:
                data = login(email, password)
                if "email" in data:
                    st.session_state.user = data["email"]
                    st.success("Login successful")
                    st.rerun()
                else:
                    st.error(data.get("error", {}).get("message", "Login failed"))

    with tab2:
        email2 = st.text_input("Email", key="signup_email")
        password2 = st.text_input("Password", type="password", key="signup_password")

        if st.button("Signup"):
            if not email2 or not password2:
                st.warning("Enter email and password")
            else:
                data = signup(email2, password2)
                if "email" in data:
                    st.success("Signup successful. Please login.")
                else:
                    st.error(data.get("error", {}).get("message", "Signup failed"))

# ---------- MAIN APP ----------
else:
    st.sidebar.title("👤 User Panel")
    st.sidebar.success(st.session_state.user)

    if st.sidebar.button("Logout"):
        st.session_state.user = None
        st.rerun()

    st.title("🤖 LinuxandK8s AI Assistant")
    st.caption("Powered by Gemini 2.5 Flash Lite")

    prompt = st.text_area("Enter your prompt", height=200)

    if st.button("Generate Response"):
        if not prompt.strip():
            st.warning("Please enter a prompt.")
        else:
            with st.spinner("Thinking..."):
                try:
                    response = client.models.generate_content(
                        model="gemini-2.5-flash-lite",
                        contents=prompt
                    )
                    st.success("Completed")
                    st.write(response.text)
                except Exception as e:
                    st.error(str(e))
