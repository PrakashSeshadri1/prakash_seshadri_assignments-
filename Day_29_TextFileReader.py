import streamlit as st
import PyPDF2
import docx
import os

st.set_page_config(page_title="Text File Reader", page_icon="📄", layout="centered")

st.title("📄 Text File Reader")

# Function to count lines and words from text
def count_lines_words(text):
    lines = text.strip().split("\n")
    line_count = len(lines)
    word_count = len(text.split())
    return line_count, word_count

# --- Section 1: File Upload ---
st.subheader("📂 Upload a File")
uploaded_file = st.file_uploader("Choose a text, Word, or PDF file", type=["txt", "docx", "pdf"])

if uploaded_file is not None:
    text = ""

    # Read text file
    if uploaded_file.name.endswith(".txt"):
        text = uploaded_file.read().decode("utf-8")

    # Read Word file
    elif uploaded_file.name.endswith(".docx"):
        doc = docx.Document(uploaded_file)
        text = "\n".join([para.text for para in doc.paragraphs])

    # Read PDF file
    elif uploaded_file.name.endswith(".pdf"):
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        for page in pdf_reader.pages:
            text += page.extract_text() + "\n"

    if text:
        lines, words = count_lines_words(text)
        st.success(f"**Total Lines:** {lines} | **Total Words:** {words}")

# --- Section 2: Manual Text Input ---
st.subheader("✍️ Paste or Write Text Below")
manual_text = st.text_area("Enter your text here...")

if manual_text.strip():
    lines, words = count_lines_words(manual_text)
    st.info(f"**Total Lines:** {lines} | **Total Words:** {words}")
