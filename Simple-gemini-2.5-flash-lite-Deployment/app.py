import streamlit as st
import google.generativeai as genai
import os

# ----------------------------
# Page Config
# ----------------------------
st.set_page_config(
    page_title="Linuxandk8s",
    page_icon="🚀",
    layout="centered"
)

# ----------------------------
# Custom CSS Styling
# ----------------------------
st.markdown("""
<style>
/* Main background */
.stApp {
    background: linear-gradient(135deg, #0f172a, #1e293b, #111827);
    color: white;
}

/* Title */
.main-title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: #38bdf8;
    margin-bottom: 5px;
}

/* Subtitle */
.sub-text {
    text-align: center;
    font-size: 16px;
    color: #cbd5e1;
    margin-bottom: 25px;
}

/* Footer */
.footer {
    text-align: center;
    font-size: 14px;
    color: #94a3b8;
    margin-top: 40px;
}

/* Text area */
textarea {
    background-color: #1e293b !important;
    color: white !important;
    border-radius: 10px !important;
}

/* Buttons */
.stButton > button {
    width: 100%;
    border-radius: 10px;
    background: #38bdf8;
    color: black;
    font-weight: bold;
    height: 45px;
    border: none;
}

.stButton > button:hover {
    background: #0ea5e9;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# ----------------------------
# Header
# ----------------------------
st.markdown('<div class="main-title">🚀 Linuxandk8s</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-text">Production Grade GenAI Web App on GCP</div>', unsafe_allow_html=True)

# ----------------------------
# API Key
# ----------------------------
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    st.error("GOOGLE_API_KEY not found")
    st.stop()

genai.configure(api_key=api_key)

# Cost Optimized Model
model = genai.GenerativeModel("gemini-2.5-flash-lite")

# ----------------------------
# Input
# ----------------------------
prompt = st.text_area("Enter your prompt", height=180)

# ----------------------------
# Generate Button
# ----------------------------
if st.button("Generate Response"):
    if prompt.strip():
        with st.spinner("Generating..."):
            response = model.generate_content(prompt)
            st.success("Response Generated Successfully!")
            st.write(response.text)
    else:
        st.warning("Please enter a prompt")

# ----------------------------
# Footer
# ----------------------------
st.markdown(
    '<div class="footer">Created by: <b>Mudassiruddin Qazi</b></div>',
    unsafe_allow_html=True
)
