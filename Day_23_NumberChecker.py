import streamlit as st
import math
import random

# ---------------------------
# Helper Functions
# ---------------------------
def number_sign(n: int) -> str:
    """Check if a number is Positive, Negative, or Zero."""
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    return "Zero"

def is_even(n: int) -> bool:
    """Check if a number is even."""
    return n % 2 == 0

def is_prime_with_reason(n: int):
    """Check if number is prime and explain why."""
    if n <= 1:
        return False, "Numbers <= 1 are not prime."
    if n <= 3:
        return True, f"{n} is prime (special case ≤ 3)."
    if n % 2 == 0:
        return False, f"{n} is divisible by 2."
    if n % 3 == 0:
        return False, f"{n} is divisible by 3."

    iterations = 0
    for i in range(5, int(math.sqrt(n)) + 1, 2):
        iterations += 1
        if n % i == 0:
            return False, f"{n} is divisible by {i}. Checked {iterations} iterations."
    return True, f"{n} is a prime number. Checked {iterations} iterations."


# ---------------------------
# Streamlit App
# ---------------------------
st.title("🔢 Number Checker Functions")
st.write("Check if a number is positive, even, or prime (with explanation).")

# Mode selection
mode = st.radio("Choose Mode:", ["Single Number", "Multiple Numbers", "Random Number Practice"])

if mode == "Single Number":
    number = st.number_input("Enter a number:", step=1, format="%d")

    if st.button("Check Number"):
        st.subheader("Results")
        st.write(f"**Number Sign:** {number_sign(number)}")
        st.write(f"**Even/Odd:** {'Even' if is_even(number) else 'Odd'}")

        prime, reason = is_prime_with_reason(number)
        st.write(f"**Prime Check:** {'Yes ✅' if prime else 'No ❌'} - {reason}")

elif mode == "Multiple Numbers":
    nums_input = st.text_area("Enter numbers (comma-separated):", "2, 5, 10, 17, 20")
    
    if st.button("Check Numbers"):
        try:
            nums = [int(x.strip()) for x in nums_input.split(",")]
            st.subheader("Results Table")
            results = []
            for n in nums:
                prime, reason = is_prime_with_reason(n)
                results.append({
                    "Number": n,
                    "Sign": number_sign(n),
                    "Even/Odd": "Even" if is_even(n) else "Odd",
                    "Prime?": "Yes ✅" if prime else "No ❌",
                    "Explanation": reason
                })
            st.dataframe(results)
        except:
            st.error("⚠️ Please enter valid comma-separated integers.")

elif mode == "Random Number Practice":
    if st.button("Generate Random Number"):
        number = random.randint(1, 100)
        st.success(f"Your random number is: **{number}**")

        st.subheader("Results")
        st.write(f"**Number Sign:** {number_sign(number)}")
        st.write(f"**Even/Odd:** {'Even' if is_even(number) else 'Odd'}")

        prime, reason = is_prime_with_reason(number)
        st.write(f"**Prime Check:** {'Yes ✅' if prime else 'No ❌'} - {reason}")
