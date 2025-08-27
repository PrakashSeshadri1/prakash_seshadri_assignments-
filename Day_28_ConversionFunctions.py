# ConversionFunctions.py

import streamlit as st
from datetime import datetime

# Conversion dictionaries
conversions = {
    "Length": {
        "Feet": 0.3048,       # base = meters
        "Meters": 1,
        "Inches": 0.0254,
        "Centimeters": 0.01
    },
    "Weight": {
        "Pounds": 0.453592,   # base = kg
        "Kilograms": 1,
        "Tons": 1000          # metric ton
    },
    "Temperature": {},  # handled separately
    "Volume": {
        "Liters": 1,          # base = liters
        "Gallons": 3.78541
    }
}

# Helper functions
def convert_units(category, from_unit, to_unit, value):
    """Generic conversion except temperature"""
    if category == "Temperature":
        return convert_temperature(from_unit, to_unit, value)

    base_value = value * conversions[category][from_unit]  # convert to base
    result = base_value / conversions[category][to_unit]   # convert to target
    return result

def convert_temperature(from_unit, to_unit, value):
    """Temperature conversions"""
    if from_unit == to_unit:
        return value

    # Convert to Celsius first
    if from_unit == "Celsius":
        c = value
    elif from_unit == "Fahrenheit":
        c = (value - 32) * 5/9
    elif from_unit == "Kelvin":
        c = value - 273.15
    else:
        return None

    # Convert from Celsius to target
    if to_unit == "Celsius":
        return c
    elif to_unit == "Fahrenheit":
        return (c * 9/5) + 32
    elif to_unit == "Kelvin":
        return c + 273.15
    else:
        return None


# Streamlit App
def main():
    st.title("🔄 Universal Unit Converter")

    # 📅 Date and Time
    now = datetime.now().strftime("%A, %d %B %Y - %I:%M %p")
    st.sidebar.info(f"📅 {now}")

    # Select category
    category = st.selectbox("Select Category:", list(conversions.keys()))

    # Select units
    if category == "Temperature":
        units = ["Celsius", "Fahrenheit", "Kelvin"]
    else:
        units = list(conversions[category].keys())

    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From Unit:", units)
    with col2:
        to_unit = st.selectbox("To Unit:", units)

    value = st.number_input(f"Enter value in {from_unit}:", min_value=0.0, format="%.4f")
    precision = st.slider("Select decimal precision:", 1, 6, 4)

    # Buttons
    col3, col4 = st.columns([1,1])
    with col3:
        convert_btn = st.button("Convert")
    with col4:
        clear_btn = st.button("Clear History")

    # Session state for history
    if "history" not in st.session_state:
        st.session_state.history = []

    if convert_btn:
        result = convert_units(category, from_unit, to_unit, value)
        if result is not None:
            st.success(f"{value} {from_unit} = {round(result, precision)} {to_unit}")
            st.session_state.history.append(
                f"{value} {from_unit} → {round(result, precision)} {to_unit}"
            )
        else:
            st.error("Conversion not supported!")

    if clear_btn:
        st.session_state.history = []

    # Show history
    if st.session_state.history:
        st.subheader("📝 Conversion History")
        for h in st.session_state.history[-10:]:  # show last 10
            st.write("•", h)


if __name__ == "__main__":
    main()
