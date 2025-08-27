# DateFunctions.py

import streamlit as st
from datetime import datetime, date
import calendar

# --- Functions ---
def is_leap_year(year: int) -> (bool, str):
    """Check if a given year is a leap year, with explanation"""
    if year % 400 == 0:
        return True, f"{year} is divisible by 400 → Leap Year ✅"
    elif year % 100 == 0:
        return False, f"{year} is divisible by 100 but not 400 → NOT Leap Year ❌"
    elif year % 4 == 0:
        return True, f"{year} is divisible by 4 but not 100 → Leap Year ✅"
    else:
        return False, f"{year} is not divisible by 4 → NOT Leap Year ❌"

def leap_years_in_range(start: int, end: int):
    """Return all leap years in a given range"""
    return [year for year in range(start, end + 1) if is_leap_year(year)[0]]

def calculate_age(birthdate: date):
    """Calculate precise age in years, months, days"""
    today = date.today()
    if birthdate > today:
        return None, "Birthdate is in the future! ❌"

    years = today.year - birthdate.year
    months = today.month - birthdate.month
    days = today.day - birthdate.day

    if days < 0:
        months -= 1
        days += (date(today.year, today.month, 1) - date(today.year, today.month - 1, 1)).days

    if months < 0:
        years -= 1
        months += 12

    return (years, months, days), None

def days_until_next_birthday(birthdate: date):
    """Days left until next birthday"""
    today = date.today()
    next_birthday = date(today.year, birthdate.month, birthdate.day)
    if next_birthday < today:
        next_birthday = date(today.year + 1, birthdate.month, birthdate.day)
    return (next_birthday - today).days

def day_of_week(any_date: date) -> str:
    """Return day of week"""
    return any_date.strftime("%A")

def days_between(d1: date, d2: date) -> int:
    """Number of days between two dates"""
    return abs((d2 - d1).days)


# --- Streamlit App ---
def main():
    st.title("📅 Date Functions App")
    st.write("Check leap years, calculate age, and explore date utilities.")

    # Sidebar with date/time
    now = datetime.now().strftime("%A, %d %B %Y - %I:%M %p")
    st.sidebar.info(f"📅 {now}")

    option = st.radio(
        "Choose an option:",
        ["Check Leap Year", "Calculate Age", "Day of the Week", "Days Between Dates"]
    )

    # --- Leap Year Check ---
    if option == "Check Leap Year":
        mode = st.radio("Choose Mode:", ["Single Year", "Range of Years"])

        if mode == "Single Year":
            year = st.number_input("Enter a year:", min_value=1, step=1)
            if st.button("Check Leap Year"):
                leap, explanation = is_leap_year(year)
                st.info(explanation)

        elif mode == "Range of Years":
            start = st.number_input("Start Year:", min_value=1, step=1)
            end = st.number_input("End Year:", min_value=1, step=1, value=start+10)
            if st.button("Find Leap Years"):
                if start > end:
                    st.error("Start year must be less than or equal to end year!")
                else:
                    years = leap_years_in_range(start, end)
                    if years:
                        st.success(f"Leap Years between {start} and {end}: {years}")
                    else:
                        st.warning(f"No leap years found between {start} and {end}")

    # --- Age Calculator ---
    elif option == "Calculate Age":
        birthdate = st.date_input("Select your Date of Birth:")
        if st.button("Calculate Age"):
            (result, error) = calculate_age(birthdate)
            if error:
                st.error(error)
            else:
                years, months, days = result
                st.success(f"🎂 Your age is {years} years, {months} months, {days} days.")
                st.info(f"⏳ Days until next birthday: {days_until_next_birthday(birthdate)} days")

    # --- Day of Week ---
    elif option == "Day of the Week":
        any_date = st.date_input("Pick a Date:")
        if st.button("Find Day"):
            st.success(f"{any_date} was a **{day_of_week(any_date)}**")

    # --- Days Between Two Dates ---
    elif option == "Days Between Dates":
        col1, col2 = st.columns(2)
        with col1:
            d1 = st.date_input("Select First Date:")
        with col2:
            d2 = st.date_input("Select Second Date:")

        if st.button("Calculate Days"):
            diff = days_between(d1, d2)
            st.success(f"📅 Difference between {d1} and {d2} is {diff} days.")


if __name__ == "__main__":
    main()
