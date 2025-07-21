import streamlit as st

st.set_page_config(page_title="List Maximum Finder", layout="centered")

# Title with symbol
st.title("📈 List Maximum Finder")

# Short description
st.markdown("""
Enter any 5 numbers (including decimals and negatives) to find the **largest value**  
— without using Python’s built-in `max()` function.
""")

# Credit line
st.markdown("<p style='color: grey; font-size: 14px;'>App created by Prakash Seshadri</p>", unsafe_allow_html=True)

# --- Input fields ---
num1 = st.number_input("Enter number 1", value=0.0, format="%.4f")
num2 = st.number_input("Enter number 2", value=0.0, format="%.4f")
num3 = st.number_input("Enter number 3", value=0.0, format="%.4f")
num4 = st.number_input("Enter number 4", value=0.0, format="%.4f")
num5 = st.number_input("Enter number 5", value=0.0, format="%.4f")

numbers = [num1, num2, num3, num4, num5]

# --- Find maximum manually ---
def find_max(numbers):
    largest = numbers[0]
    for n in numbers[1:]:
        if n > largest:
            largest = n
    return largest

# --- Button and result ---
if st.button("Find Maximum"):
    maximum = find_max(numbers)
    st.success(f"✅ The largest number is: **{maximum}**")
