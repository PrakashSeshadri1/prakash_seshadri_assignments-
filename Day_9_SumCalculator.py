import streamlit as st

# Page configuration
st.set_page_config(page_title="Day 9 - Sum Calculator", page_icon="➕")

# Title and description
st.markdown("# ➕ Day 9: Sum Calculator Assignment")
st.write("This app calculates the sum of all numbers from 1 to **n** using a loop.")

# User input
n = st.number_input("Enter a positive integer (n):", min_value=1, step=1, format="%d")

# Submit button
if st.button("Submit"):
    total_sum = 0
    breakdown = ""

    for i in range(1, n + 1):
        total_sum += i
        breakdown += f"{i} + " if i != n else f"{i}"

    # Display result
    st.subheader("🧮 Calculation Breakdown")
    st.code(breakdown, language="python")

    st.subheader("✅ Final Result")
    st.success(f"Sum of numbers from 1 to {n} is: {total_sum}")
