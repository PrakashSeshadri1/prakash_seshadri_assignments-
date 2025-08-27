# ListHelper.py

import streamlit as st
from datetime import datetime

# --- Functions ---
def find_max(numbers):
    return max(numbers) if numbers else None

def find_min(numbers):
    return min(numbers) if numbers else None

def find_sum(numbers):
    return sum(numbers) if numbers else 0

def find_average(numbers):
    return sum(numbers) / len(numbers) if numbers else None


# --- Streamlit App ---
def main():
    st.title("📊 List Helper Functions")
    st.write("Find maximum, minimum, sum, and average of a list of numbers.")

    # Sidebar with date/time
    now = datetime.now().strftime("%A, %d %B %Y - %I:%M %p")
    st.sidebar.info(f"📅 {now}")

    # User input for list
    user_input = st.text_area(
        "Enter numbers separated by commas:",
        placeholder="e.g., 10, 20, 30, 40"
    )

    numbers = []
    if user_input.strip():
        try:
            numbers = [float(x.strip()) for x in user_input.split(",")]
        except ValueError:
            st.error("⚠️ Please enter only numbers separated by commas.")

    col1, col2 = st.columns([1,1])
    with col1:
        calc_btn = st.button("Calculate")
    with col2:
        clear_btn = st.button("Clear")

    if clear_btn:
        st.session_state.clear()
        st.experimental_rerun()

    if calc_btn and numbers:
        st.subheader("✅ Results")
        st.write(f"🔼 **Maximum:** {find_max(numbers)}")
        st.write(f"🔽 **Minimum:** {find_min(numbers)}")
        st.write(f"➕ **Sum:** {find_sum(numbers)}")
        st.write(f"📉 **Average:** {round(find_average(numbers), 2)}")

    elif calc_btn and not numbers:
        st.warning("⚠️ Please enter a valid list of numbers.")


if __name__ == "__main__":
    main()
