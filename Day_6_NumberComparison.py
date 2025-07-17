import streamlit as st

st.title("🔢 Number Comparison Tool")

st.markdown("Enter two numbers below to compare them:")

# User input
num1 = st.number_input("Enter the first number:", key="num1")
num2 = st.number_input("Enter the second number:", key="num2")

# Compare on button click
if st.button("Compare"):
    if num1 > num2:
        st.success(f"{num1} is greater than {num2}")
    elif num1 < num2:
        st.success(f"{num1} is smaller than {num2}")
    else:
        st.info("Both numbers are equal.")

# Optional emoji
st.write("🤖 Happy Comparing!")
