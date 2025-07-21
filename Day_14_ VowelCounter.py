import streamlit as st

st.set_page_config(page_title="Vowel Counter", layout="centered")

# Title with symbol
st.title("🔤 Vowel Counter")

# Short description
st.markdown("""
Enter a word to count how many vowels (A, E, I, O, U) it contains — case-insensitive.
""")

# Footer
st.markdown("<p style='color: grey; font-size: 14px;'>App created by Prakash Seshadri</p>", unsafe_allow_html=True)

# --- Input field ---
word = st.text_input("Enter a word")

# --- Vowel counting function ---
def count_vowels(text):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in text if char in vowels)

# --- Output ---
if word:
    vowel_count = count_vowels(word)
    st.success(f"🔍 The word **{word}** has **{vowel_count}** vowel(s).")
