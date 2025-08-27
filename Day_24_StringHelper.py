import streamlit as st

def capitalize_text(text):
    return text.capitalize()

def reverse_text(text):
    return text[::-1]

def count_characters(text):
    return len(text)

def count_words(text):
    return len(text.split())

def remove_spaces(text):
    return text.replace(" ", "")

def is_palindrome(text):
    return text == text[::-1]

st.title("📚 String Helper Functions")

text_input = st.text_area("Enter your text:", "")

# Select which operations to perform
options = st.multiselect(
    "Choose operations:",
    ["Capitalize", "Reverse", "Count Characters", "Count Words", "Remove Spaces", "Check Palindrome"]
)

# ✅ Fix: Only create tabs if at least one option is selected
if options:
    tabs = st.tabs(options)
    for i, option in enumerate(options):
        with tabs[i]:
            if option == "Capitalize":
                st.write("✅ Result:", capitalize_text(text_input))
            elif option == "Reverse":
                st.write("✅ Result:", reverse_text(text_input))
            elif option == "Count Characters":
                st.write("✅ Result:", count_characters(text_input))
            elif option == "Count Words":
                st.write("✅ Result:", count_words(text_input))
            elif option == "Remove Spaces":
                st.write("✅ Result:", remove_spaces(text_input))
            elif option == "Check Palindrome":
                st.write("✅ Result:", "Yes, it's a palindrome!" if is_palindrome(text_input) else "No, not a palindrome")
else:
    st.info("👉 Please select at least one operation from above.")
