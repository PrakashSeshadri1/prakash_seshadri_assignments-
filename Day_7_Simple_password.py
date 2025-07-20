import streamlit as st
import re

st.title("🔐 Day 7 - Simple Password Checker")

# Input field
password = st.text_input("Enter your password", type="password")

# Check when user enters a password
if password:
    # Define requirements
    min_length = 8
    has_uppercase = re.search(r'[A-Z]', password)
    has_digit = re.search(r'\d', password)
    has_special = re.search(r'[^A-Za-z0-9]', password)

    if len(password) >= min_length and has_uppercase and has_digit and has_special:
        st.success("✅ Password is valid")
    else:
        st.error("❌ Password must have:\n- At least 8 characters\n- One uppercase letter\n- One number\n- One special character")
