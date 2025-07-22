import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Simple Cipher",
    page_icon="🔐",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- Theme Toggle ---
theme = st.selectbox("Choose Theme Mode", ["🌞 Day Mode", "🌙 Dark Mode"])

# --- Theme Styling ---
if theme == "🌞 Day Mode":
    bg_color = "#F5F5F5"
    text_color = "#333333"
    highlight_color = "#4B0082"
    header_color = "#8A2BE2"
    box_color = "#FFFFFF"
else:
    bg_color = "#1e1e1e"
    text_color = "#DDDDDD"
    highlight_color = "#00d4ff"
    header_color = "#00c0ff"
    box_color = "#2e2e2e"

# --- Custom CSS ---
st.markdown(
    f"""
    <style>
        .stApp {{
            background-color: {bg_color};
            color: {text_color};
        }}
        .stTextInput > div > div > input {{
            background-color: {box_color};
            color: {text_color};
        }}
        .stTextInput > label {{
            color: {text_color};
        }}
        .report-box {{
            border: 1px solid {highlight_color};
            padding: 15px;
            border-radius: 10px;
            background-color: rgba(0, 0, 0, 0.05);
            margin-top: 20px;
        }}
        .highlight {{
            color: {highlight_color};
            font-weight: bold;
        }}
    </style>
    """,
    unsafe_allow_html=True
)

# --- Header Section ---
st.markdown(
    f"""
    <h1 style='text-align: center; color: {header_color};'>🔐 Simple Cipher</h1>
    <p style='text-align: center; font-size:18px; color: {text_color};'>
        Encode your message by shifting each letter by 1 in the alphabet!
    </p>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# --- Cipher Function ---
def shift_cipher(text):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + 1) % 26 + base)
        else:
            result += char
    return result

# --- Input Section ---
st.markdown(f"### <span style='color:{text_color};'>Enter a message to encrypt:</span>", unsafe_allow_html=True)
user_input = st.text_input("Your Message", placeholder="e.g., Hello World")

if user_input:
    ciphered = shift_cipher(user_input)

    st.markdown(
        f"""
        <div class='report-box'>
            <p><strong>Original Text:</strong> {user_input}</p>
            <p><strong>Encrypted Text:</strong> <span class='highlight'>{ciphered}</span></p>
        </div>
        """,
        unsafe_allow_html=True
    )

# --- Footer ---
st.markdown(
    f"""
    <br><br>
    <p style='text-align: center; color: gray; font-size:20px;'>Built by Prakash Seshadri</p>
    """,
    unsafe_allow_html=True
)
