# NameStorage.py

import streamlit as st
import os
import json
from datetime import datetime
import pandas as pd

# File path to store names
FILE_PATH = "contacts.json"

# Load contacts from file
def load_contacts():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

# Save contacts to file
def save_contacts(contacts):
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(contacts, f, indent=4)

# Initialize
contacts = load_contacts()

st.title("📇 Name & Contact Storage")

# --- Input Section ---
st.subheader("➕ Add New Contact")
name = st.text_input("Enter Name")
mobile = st.text_input("Enter Mobile Number (10 digits)", max_chars=10)

if st.button("Save Contact"):
    if not name.strip():
        st.warning("⚠ Please enter a name.")
    elif not (mobile.isdigit() and len(mobile) == 10):
        st.warning("⚠ Mobile number must be exactly 10 digits.")
    else:
        # Check for duplicate name
        if any(c["name"].lower() == name.strip().lower() for c in contacts):
            st.warning("⚠ This name already exists.")
        else:
            contacts.append({
                "name": name.strip(),
                "mobile": mobile,
                "date_added": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
            save_contacts(contacts)
            st.success(f"✅ Contact '{name}' saved!")

# --- Display Section ---
st.subheader("📜 Saved Contacts")
if contacts:
    # Create DataFrame for display
    df = pd.DataFrame(contacts)
    df.index = range(1, len(df) + 1)  # S.No starting from 1
    df.index.name = "S.No"
    df.columns = ["Name", "Mobile", "Date Added"]
    st.dataframe(df, use_container_width=True)
else:
    st.info("No contacts saved yet.")

# --- Edit/Delete Section ---
st.subheader("✏️ Edit / ❌ Delete Contact")
if contacts:
    selected_name = st.selectbox("Select contact to edit/delete", [c["name"] for c in contacts])
    contact_data = next(c for c in contacts if c["name"] == selected_name)

    new_name = st.text_input("Edit Name", value=contact_data["name"])
    new_mobile = st.text_input("Edit Mobile Number (10 digits)", value=contact_data["mobile"], max_chars=10)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Update Contact"):
            if not new_name.strip():
                st.warning("⚠ Please enter a name.")
            elif not (new_mobile.isdigit() and len(new_mobile) == 10):
                st.warning("⚠ Mobile number must be exactly 10 digits.")
            else:
                contact_data["name"] = new_name.strip()
                contact_data["mobile"] = new_mobile
                save_contacts(contacts)
                st.success("✅ Contact updated!")

    with col2:
        if st.button("Delete Contact"):
            contacts = [c for c in contacts if c["name"] != selected_name]
            save_contacts(contacts)
            st.success("🗑 Contact deleted!")
else:
    st.info("No contacts available to edit or delete.")
