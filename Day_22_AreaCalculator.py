# File: Day_22_AreaCalculator.py
import streamlit as st
import math
from datetime import datetime

# --- Area Functions ---
def area_circle(radius):
    return math.pi * radius**2

def area_rectangle(length, width):
    return length * width

def area_triangle(base, height):
    return 0.5 * base * height

def area_square(side):
    return side**2

def area_parallelogram(base, height):
    return base * height

def area_trapezium(base1, base2, height):
    return 0.5 * (base1 + base2) * height

def area_ellipse(a, b):
    return math.pi * a * b


# --- Streamlit App ---
def main():
    st.title("📐 Area Calculator")
    st.write("Calculate the area of different shapes easily!")

    # Show current date and time
    st.sidebar.info(f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # Select shape
    shape = st.selectbox(
        "Choose a shape",
        ["Circle", "Rectangle", "Triangle", "Square", "Parallelogram", "Trapezium", "Ellipse"]
    )

    # Unit selection
    unit = st.selectbox("Select units", ["cm", "m", "inch", "ft"])

    result = None
    formula = ""

    # --- Circle ---
    if shape == "Circle":
        radius = st.number_input("Enter radius", min_value=0.0, format="%.2f")
        formula = "Area = π × r²"
        if radius > 0:
            result = area_circle(radius)

    # --- Rectangle ---
    elif shape == "Rectangle":
        length = st.number_input("Enter length", min_value=0.0, format="%.2f")
        width = st.number_input("Enter width", min_value=0.0, format="%.2f")
        formula = "Area = length × width"
        if length > 0 and width > 0:
            result = area_rectangle(length, width)

    # --- Triangle ---
    elif shape == "Triangle":
        base = st.number_input("Enter base", min_value=0.0, format="%.2f")
        height = st.number_input("Enter height", min_value=0.0, format="%.2f")
        formula = "Area = ½ × base × height"
        if base > 0 and height > 0:
            result = area_triangle(base, height)

    # --- Square ---
    elif shape == "Square":
        side = st.number_input("Enter side", min_value=0.0, format="%.2f")
        formula = "Area = side²"
        if side > 0:
            result = area_square(side)

    # --- Parallelogram ---
    elif shape == "Parallelogram":
        base = st.number_input("Enter base", min_value=0.0, format="%.2f")
        height = st.number_input("Enter height", min_value=0.0, format="%.2f")
        formula = "Area = base × height"
        if base > 0 and height > 0:
            result = area_parallelogram(base, height)

    # --- Trapezium ---
    elif shape == "Trapezium":
        base1 = st.number_input("Enter base1", min_value=0.0, format="%.2f")
        base2 = st.number_input("Enter base2", min_value=0.0, format="%.2f")
        height = st.number_input("Enter height", min_value=0.0, format="%.2f")
        formula = "Area = ½ × (base1 + base2) × height"
        if base1 > 0 and base2 > 0 and height > 0:
            result = area_trapezium(base1, base2, height)

    # --- Ellipse ---
    elif shape == "Ellipse":
        a = st.number_input("Enter semi-major axis (a)", min_value=0.0, format="%.2f")
        b = st.number_input("Enter semi-minor axis (b)", min_value=0.0, format="%.2f")
        formula = "Area = π × a × b"
        if a > 0 and b > 0:
            result = area_ellipse(a, b)

    # Display result
    if result:
        st.success(f"✅ {formula}")
        st.write(f"**Result:** {result:.2f} {unit}²")


if __name__ == "__main__":
    main()
