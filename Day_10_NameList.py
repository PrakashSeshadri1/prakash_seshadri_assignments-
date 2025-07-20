import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(page_title="Day 10 - Name List", page_icon="📛")

# Title and description
st.markdown("# 📛 Day 10: Name List Assignment")
st.write("Enter 5 names below. After submitting, the app will show each name with its character count.")

# Input fields for 5 names
with st.form("name_form"):
    name1 = st.text_input("Enter Name 1")
    name2 = st.text_input("Enter Name 2")
    name3 = st.text_input("Enter Name 3")
    name4 = st.text_input("Enter Name 4")
    name5 = st.text_input("Enter Name 5")

    submitted = st.form_submit_button("Click here to see the list")

# Process and show report
if submitted:
    names = [name1, name2, name3, name4, name5]

    if all(name.strip() for name in names):  # Ensure no empty names
        # Create report as DataFrame
        report = pd.DataFrame({
            "Name": names,
            "Characters": [len(name) for name in names]
        })

        st.subheader("📋 Name and Character Report")
        st.table(report)
    else:
        st.error("❌ Please enter all 5 names.")
