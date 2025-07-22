import streamlit as st
import re
from datetime import datetime
import time

# --- Page Config ---
st.set_page_config(
    page_title="Generate Email Username",
    page_icon="📧",
    layout="centered"
)

# --- Function to Validate Email ---
def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

# --- Function to Extract Username ---
def extract_username(email):
    return email.split("@")[0]

# --- Live Clock Display ---
clock_placeholder = st.empty()

# --- Start Real-Time Clock ---
def update_clock():
    while True:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        clock_placeholder.markdown(
            f"<div style='position: absolute; top: 20px; right: 25px; color: gray; font-size: 16px;'>{now}</div>",
            unsafe_allow_html=True
        )
        time.sleep(1)

# --- Use Streamlit Autorefresh instead of while loop ---
st_autorefresh = st.experimental_data_editor if hasattr(st, "experimental_data_editor") else None
st_autorefresh = st_autorefresh or (lambda *a, **k: None)
st_autorefresh(interval=1000, key="refresh")

now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
clock_placeholder.markdown(
    f"<div style='position: absolute; top: 20px; right: 25px; color: gray; font-size: 16px;'>{now}</div>",
    unsafe_allow_html=True
)

# --- Header ---
st.markdown(
    """
    <h1 style='text-align: center; color: #0066cc;'>📧 Generate Email Username</h1>
    <p style='text-align: center; font-size:18px; color: #444;'>Enter an email address and get the username before @</p>
    """,
    unsafe_allow_html=True
)
st.markdown("---")

# --- Input ---
email = st.text_input("Enter your email address", placeholder="e.g., prakash@email.com")

# --- Process ---
if email:
    if is_valid_email(email):
        username = extract_username(email)

        st.success(f"👤 Username Extracted: **{username}**")

        # 🎉 Optional Animation
        st.balloons()

        # 📋 Copy to clipboard feature
        st.code(username, language="text")
        st.markdown(
            f"<button onclick='navigator.clipboard.writeText(\"{username}\")'>📋 Copy Username</button>",
            unsafe_allow_html=True
        )
    else:
        st.error("❌ Invalid email format. Please enter a valid email.")

# --- Footer ---
st.markdown(
    """
    <br><br>
    <p style='text-align: center; color: gray; font-size:14px;'>Built by Prakash Seshadri</p>
    """,
    unsafe_allow_html=True
)
