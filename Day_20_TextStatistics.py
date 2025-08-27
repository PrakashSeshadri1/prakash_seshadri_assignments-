# Day_20_TextStatistics.py

import streamlit as st
from datetime import datetime
import pandas as pd
import re
from io import StringIO
import PyPDF2

# App Header
st.set_page_config(page_title="Text Statistics", layout="centered")
st.title("📊 Text Statistics App")

# Show current date and time
now = datetime.now()
formatted_time = now.strftime("%A, %d %B %Y | %I:%M:%S %p")
st.markdown(f"🕒 **Current Time:** `{formatted_time}`")
st.markdown("---")

# File uploader
uploaded_file = st.file_uploader("📂 Upload a `.txt` or `.pdf` file", type=["txt", "pdf"])

# Text input area
text_input = st.text_area("Or type/paste your paragraph below 👇", height=200)

# Function to extract text from PDF
def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

# Function to calculate statistics
def text_stats(text):
    num_chars = len(text)
    num_chars_no_space = len(text.replace(" ", ""))
    words = text.split()
    num_words = len(words)
    sentences = re.split(r'[.!?]+', text)
    sentences = [s for s in sentences if s.strip()]
    num_sentences = len(sentences)
    return num_words, num_sentences, num_chars, num_chars_no_space

# Load text from file or input
if uploaded_file is not None:
    if uploaded_file.name.endswith(".txt"):
        text = StringIO(uploaded_file.getvalue().decode("utf-8")).read()
    elif uploaded_file.name.endswith(".pdf"):
        text = extract_text_from_pdf(uploaded_file)
else:
    text = text_input

# Analyze button
if text:
    st.markdown("### 📈 Results:")

    # Calculate statistics
    words, sentences, chars, chars_no_space = text_stats(text)

    # Display stats
    st.write(f"📝 Total **Words**: `{words}`")
    st.write(f"📚 Total **Sentences**: `{sentences}`")
    st.write(f"🔤 Total **Characters** (with spaces): `{chars}`")
    st.write(f"🔡 Total **Characters** (without spaces): `{chars_no_space}`")

    # Word frequency
    st.markdown("### 🔠 Word Frequency")
    word_list = re.findall(r'\b\w+\b', text.lower())
    word_freq = pd.Series(word_list).value_counts().head(10)
    st.bar_chart(word_freq)

    # Summary
    st.markdown("### 🧠 Text Summary")
    if words < 50:
        st.info("This is a short paragraph.")
    elif words < 150:
        st.success("This is a moderate-length paragraph.")
    else:
        st.warning("This is a long paragraph.")

    # Download report
    report = f"""Text Analysis Report
-------------------------
Date & Time : {formatted_time}

Words       : {words}
Sentences   : {sentences}
Characters  : {chars}
No Spaces   : {chars_no_space}

Top 10 Words:
{word_freq.to_string()}
"""
    st.download_button("📥 Download Report (.txt)", report, file_name="text_statistics_report.txt")

st.markdown("---")
st.markdown("<p style='text-align: center;'>App created by Prakash Seshadri</p>", unsafe_allow_html=True)
