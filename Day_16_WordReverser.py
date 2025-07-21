import streamlit as st

st.set_page_config(page_title="Word Reverser", layout="centered")

# Title
st.title("🔄 Word Reverser")

# Short description
st.markdown("""
Enter a sentence and this app will **reverse each word individually**,  
while keeping the original word order intact.
""")

# --- Input ---
sentence = st.text_input("Enter a sentence")

# --- Function to reverse individual words ---
def reverse_words(text):
    words = text.split()
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)

# --- Output ---
if sentence:
    result = reverse_words(sentence)
    st.success(f"🔁 Reversed Sentence: {result}")

# --- Footer centered at bottom ---
st.markdown(
    """
    <div style='text-align: center; margin-top: 100px; color: grey;'>
        App created by Prakash Seshadri
    </div>
    """,
    unsafe_allow_html=True
)
