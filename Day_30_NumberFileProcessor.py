# NumberFileProcessor.py
import streamlit as st
import os
from datetime import datetime

FILE_PATH = "numbers.txt"

# Load numbers from file
def load_numbers():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            try:
                return [float(line.strip()) for line in f if line.strip()]
            except ValueError:
                st.error("⚠ File contains non-numeric values.")
                return []
    return []

# Save numbers to file
def save_number(num):
    with open(FILE_PATH, "a", encoding="utf-8") as f:
        f.write(str(num) + "\n")

# Overwrite file with new list
def overwrite_numbers(numbers):
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        for num in numbers:
            f.write(str(num) + "\n")

# Evaluate numeric expressions safely
def safe_eval(expr):
    try:
        return float(eval(expr, {"__builtins__": None}, {}))
    except:
        return None

st.title("📊 Number File Processor")

# Input section
st.subheader("➕ Add a Number")
new_number = st.text_input("Enter a number or expression (e.g., 8232 + 385)")

if st.button("Save Number"):
    if not new_number.strip():
        st.warning("⚠ Please enter a number.")
    else:
        num = safe_eval(new_number.strip())
        if num is None:
            st.error("⚠ Please enter a valid number or expression.")
        else:
            save_number(num)
            st.success(f"✅ Number {num} saved!")

# Display numbers and stats
st.subheader("📜 Numbers from File")
numbers = load_numbers()

if numbers:
    st.table(
        {"S.No": list(range(1, len(numbers) + 1)),
         "Number": numbers}
    )

    st.markdown(f"**📌 Total Count:** {len(numbers)}")
    st.markdown(f"**🧮 Sum:** {sum(numbers)}")
    st.markdown(f"**📈 Average:** {sum(numbers) / len(numbers):.2f}")

    # Delete number option
    delete_index = st.selectbox("Select index to delete", list(range(1, len(numbers) + 1)))
    if st.button("Delete Selected Number"):
        numbers.pop(delete_index - 1)
        overwrite_numbers(numbers)
        st.success("✅ Number deleted!")

    st.caption(f"🕒 Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

else:
    st.info("No numbers saved yet.")

# File reset option
if st.button("🗑 Clear All Numbers"):
    open(FILE_PATH, "w").close()
    st.success("✅ All numbers cleared.")
