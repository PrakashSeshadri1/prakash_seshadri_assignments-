import streamlit as st

# App Configuration
st.set_page_config(
    page_title="Extract Initials",
    page_icon="🔤",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- App Header ---
st.markdown(
    """
    <h1 style='text-align: center; color: #4B8BBE;'>🔤 Extract Initials</h1>
    <p style='text-align: center; font-size:18px; color: #306998;'>A simple app to extract initials from your full name.</p>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# --- Main Input Area ---
with st.container():
    st.markdown("### Enter Your Full Name Below:")
    full_name = st.text_input("Full Name", placeholder="e.g., Prakash Seshadri")

    if full_name:
        # Extract initials from each word in the full name
        words = full_name.strip().split()
        initials = ".".join([word[0].upper() for word in words]) + "."

        st.success(f"✅ Initials: **{initials}**")

# --- Footer ---
st.markdown("""
    <br><br><br>
    <p style='text-align: center; color: gray; font-size:14px;'>Built by Prakash Seshadri</p>
    """, unsafe_allow_html=True)
