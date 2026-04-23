import os, tempfile
import streamlit as st
from dotenv import load_dotenv
from utils.parser import extract_text
from utils.chunker import chunk_text
from utils.vectorstore import build_index, search_index
from utils.llm import ask_gemini
load_dotenv()

st.set_page_config(page_title='Mudassir Qazi GenAI', layout='wide')
st.title('🤖 GenAI Document Assistant')

if 'index' not in st.session_state:
    st.session_state.index = None
if 'chunks' not in st.session_state:
    st.session_state.chunks = []

uploaded = st.file_uploader('Upload PDF/DOCX/TXT', type=['pdf','docx','txt'])
if uploaded:
    text = extract_text(uploaded)
    chunks = chunk_text(text)
    index = build_index(chunks)
    st.session_state.index = index
    st.session_state.chunks = chunks
    st.success('Document processed successfully')

q = st.text_input('Ask question about document')
if q and st.session_state.index is not None:
    docs = search_index(st.session_state.index, st.session_state.chunks, q)
    answer = ask_gemini(q, docs)
    st.write(answer)
