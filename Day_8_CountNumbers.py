import streamlit as st

# Page config
st.set_page_config(page_title="Day 8 - Count Numbers", page_icon="🔢")

# Title & description
st.markdown("# 🔢 Day 8: Count Numbers Assignment")
st.write("Enter a list of numbers (integers or decimals) to count how many are positive, negative, or neutral (zero).")

# Input
input_numbers = st.text_area("Enter numbers separated by commas", placeholder="Example: -1, 4.5, 0, -3.2, 0.0, 7")

# Process input
if input_numbers:
    try:
        # Convert string to list of floats
        number_list = [float(x.strip()) for x in input_numbers.split(',')]

        # Count types
        count_positive = sum(1 for x in number_list if x > 0)
        count_negative = sum(1 for x in number_list if x < 0)
        count_zero = sum(1 for x in number_list if x == 0)

        # Show input report
        st.subheader("📋 Numbers You Entered")
        st.write(number_list)

        # Show result report
        st.subheader("📊 Count Report")
        st.success(f"✅ Positive Numbers: {count_positive}")
        st.warning(f"⚠️ Negative Numbers: {count_negative}")
        st.info(f"🔘 Neutral (Zero) Numbers: {count_zero}")

    except ValueError:
        st.error("❌ Please enter only valid numbers separated by commas.")
else:
    st.info("Please enter numbers to analyze.")
