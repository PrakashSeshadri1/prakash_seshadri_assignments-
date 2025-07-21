import streamlit as st

st.set_page_config(page_title="Name Formatter", layout="centered")

# Title with symbol
st.title("📝 Name Formatter")

# Short description
st.markdown("""
Enter your full name, and the app will format it in styles like **Last, First** and **Initials**.
""")

# Credit
st.markdown("<p style='color: grey; font-size: 14px;'>App created by Prakash Seshadri</p>", unsafe_allow_html=True)

# --- Input field ---
full_name = st.text_input("Enter your full name (e.g., John David Smith)")

# --- Format functions ---
def format_name(name):
    parts = name.strip().split()
    if len(parts) < 2:
        return None, None, None

    first = parts[0]
    last = parts[-1]
    first_last = f"{first} {last}"
    last_first = f"{last}, {first}"
    initials = '.'.join([p[0].upper() for p in parts]) + '.'

    return first_last, last_first, initials

# --- Output display ---
if full_name:
    first_last, last_first, initials = format_name(full_name)

    if first_last:
        st.subheader("Formatted Versions:")
        st.write(f"➡️ **First Last:** {first_last}")
        st.write(f"➡️ **Last, First:** {last_first}")
        st.write(f"➡️ **Initials:** {initials}")
    else:
        st.warning("Please enter at least a first and last name.")
