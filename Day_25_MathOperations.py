import streamlit as st
import math
from datetime import datetime

# ------------------------------
# Math Operation Functions
# ------------------------------
def calculate_factorial(n: int) -> int:
    """Return factorial of n."""
    try:
        return math.factorial(n)
    except ValueError:
        return "Factorial not defined for negative numbers."

def calculate_power(base: float, exp: float) -> float:
    """Return base raised to exp."""
    return math.pow(base, exp)

def calculate_square_root(n: float):
    """Return square root of n."""
    if n < 0:
        return "Square root not defined for negative numbers."
    return math.sqrt(n)

def calculate_logarithm(n: float, base: float = math.e):
    """Return logarithm of n with given base (default = natural log)."""
    if n <= 0:
        return "Logarithm not defined for zero or negative numbers."
    return math.log(n, base)

def calculate_absolute(n: float) -> float:
    """Return absolute value of n."""
    return abs(n)

def calculate_cube_root(n: float) -> float:
    """Return cube root of n."""
    return n ** (1/3)

# ------------------------------
# Streamlit App
# ------------------------------
st.set_page_config(page_title="Math Operations", layout="centered")

# App Header
st.title("🔢 Math Operations App")
st.write("Perform various mathematical operations.")

# Show current date & time
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
st.sidebar.success(f"📅 Current Date & Time: {current_time}")

# Select operation
operation = st.selectbox(
    "Choose a math operation:",
    ["Factorial", "Power", "Square Root", "Logarithm", "Absolute Value", "Cube Root"]
)

# ------------------------------
# Operation Handling
# ------------------------------
if operation == "Factorial":
    num = st.number_input("Enter a non-negative integer:", min_value=0, step=1)
    if st.button("Calculate Factorial"):
        result = calculate_factorial(int(num))
        st.success(f"✅ Factorial of {int(num)} is: {result}")

elif operation == "Power":
    base = st.number_input("Enter the base:", value=2.0)
    exp = st.number_input("Enter the exponent:", value=2.0)
    if st.button("Calculate Power"):
        result = calculate_power(base, exp)
        st.success(f"✅ {base} raised to {exp} is: {result}")

elif operation == "Square Root":
    num = st.number_input("Enter a number:", value=0.0)
    if st.button("Calculate Square Root"):
        result = calculate_square_root(num)
        st.success(f"✅ Square root of {num} is: {result}")

elif operation == "Logarithm":
    num = st.number_input("Enter a positive number:", value=1.0)
    base = st.number_input("Enter base (default e = 2.718):", value=math.e)
    if st.button("Calculate Logarithm"):
        result = calculate_logarithm(num, base)
        st.success(f"✅ Logarithm of {num} with base {base} is: {result}")

elif operation == "Absolute Value":
    num = st.number_input("Enter a number:", value=0.0)
    if st.button("Calculate Absolute Value"):
        result = calculate_absolute(num)
        st.success(f"✅ Absolute value of {num} is: {result}")

elif operation == "Cube Root":
    num = st.number_input("Enter a number:", value=0.0)
    if st.button("Calculate Cube Root"):
        result = calculate_cube_root(num)
        st.success(f"✅ Cube root of {num} is: {result}")
