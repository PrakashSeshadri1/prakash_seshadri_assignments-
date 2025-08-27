# File: Day_21_PhoneFormatter.py

import streamlit as st
import re
import pandas as pd

st.set_page_config(page_title="📞 Phone Number Formatter", layout="centered")

# ---------- Helper Function ----------
def format_phone_number(number: str) -> str:
    """
    Format a phone number string into (XXX) XXX-XXXX.
    Handles +91 and 1 country codes if present.
    """
    # Remove all non-digits
    digits = re.sub(r"\D", "", number)

    # Handle country codes
    if digits.startswith("91") and len(digits) == 12:  # +91XXXXXXXXXX
        digits = digits[2:]
    elif digits.startswith("1") and len(digits) == 11:  # 1XXXXXXXXXX
        digits = digits[1:]

    # Now must be exactly 10 digits
    if len(digits) != 10:
        return None

    return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"


# ---------- Streamlit UI ----------
st.title("📞 Phone Number Formatter")
st.write("Format numbers into (XXX) XXX-XXXX style with optional country code handling.")


tab1, tab2 = st.tabs(["➤ Single Number", "➤ Bulk Processing"])

# --- Single Number Mode ---
with tab1:
    phone = st.text_input("Enter phone number", placeholder="e.g., +91 9876543210 or 9876543210")

    if st.button("Format Number"):
        formatted = format_phone_number(phone)
        if formatted:
            st.success(f"✅ Formatted Number: {formatted}")

            # Copy-to-clipboard
            st.code(formatted, language="text")
            st.button("📋 Copy to Clipboard", on_click=lambda: st.toast("Copied!", icon="✅"))
        else:
            st.error("❌ Invalid phone number. Please enter a valid 10-digit number.")


# --- Bulk Mode ---
with tab2:
    st.write("Upload a **CSV/TXT file** or paste multiple numbers below (one per line).")

    uploaded_file = st.file_uploader("Upload file", type=["txt", "csv"])

    numbers = []
    if uploaded_file is not None:
        if uploaded_file.type == "text/plain":
            numbers = uploaded_file.read().decode("utf-8").splitlines()
        elif uploaded_file.type == "text/csv":
            df = pd.read_csv(uploaded_file, header=None)
            numbers = df.iloc[:, 0].astype(str).tolist()

    text_numbers = st.text_area("Or paste numbers here:", height=150)
    if text_numbers:
        numbers.extend(text_numbers.splitlines())

    if st.button("Process Numbers"):
        results = []
        for num in numbers:
            formatted = format_phone_number(num)
            results.append({
                "Input": num,
                "Formatted": formatted if formatted else "❌ Invalid",
                "Valid": bool(formatted)
            })

        df_results = pd.DataFrame(results)

        # Show styled results
        st.write("### Results")
        st.dataframe(df_results, use_container_width=True)

        # Download cleaned CSV
        csv = df_results.to_csv(index=False).encode("utf-8")
        st.download_button("⬇ Download Results (CSV)", data=csv, file_name="formatted_numbers.csv", mime="text/csv")

