# EvenOddChecker.py

import streamlit as st

st.title("Even or Odd Checker")

# Check single number
st.header("Check a Single Number")
number = st.number_input("Enter a number to check:", value=0, step=1)
if st.button("Check Number"):
    if number % 2 == 0:
        st.success(f"{number} is Even")
    else:
        st.success(f"{number} is Odd")

# Check a list of numbers
st.header("Check a List of Numbers")
number_list = st.text_input("Enter numbers separated by commas (e.g., 5, 8, 13, 21):")

if st.button("Check List"):
    if number_list.strip() == "":
        st.warning("Please enter some numbers.")
    else:
        try:
            # Convert string input to list of integers
            numbers = [int(num.strip()) for num in number_list.split(',')]
            for num in numbers:
                if num % 2 == 0:
                    st.write(f"{num} is Even")
                else:
                    st.write(f"{num} is Odd")
        except ValueError:
            st.error("Please enter valid integers separated by commas.")
