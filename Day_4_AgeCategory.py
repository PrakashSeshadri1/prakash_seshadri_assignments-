import streamlit as st

# Title of the app
st.title("Age Category Detector")

# Input: Age
age = st.number_input("Enter your age:", min_value=0, max_value=150, step=1)

# Determine the category
if age == 0:
    st.write("Please enter a valid age.")
elif age < 13:
    st.success("You are a Child.")

elif age < 17:
    st.success("You are an Adolescent.")    
elif age < 20:
    st.success("You are a Teenager.")
elif age < 60:
    st.success("You are an Adult.")
elif age < 80:
    st.success("You are a Senior Citizen.")
else:
    st.success("You are a Senior.")

# Optional: Display image or emoji
st.write("🙂")
