import streamlit as st
import time

st.set_page_config(page_title="Countdown Timer", layout="centered")

st.title("⏱️ Countdown Timer")

st.markdown("""
This is a simple interactive countdown timer that starts from 10 and goes down to 0.  
You can control it using **Start**, **Pause**, **Stop**, and **Reset** buttons.
""")
st.markdown("<p style='color: grey; font-size: 20px;'>App created by Prakash Seshadri</p>", unsafe_allow_html=True)

# --- Session state setup ---
if "time_left" not in st.session_state:
    st.session_state.time_left = 10
if "is_running" not in st.session_state:
    st.session_state.is_running = False

# --- Button actions ---
def start_timer():
    st.session_state.is_running = True

def pause_timer():
    st.session_state.is_running = False

def stop_timer():
    st.session_state.is_running = False
    st.session_state.time_left = 0

def reset_timer():
    st.session_state.is_running = False
    st.session_state.time_left = 10

# --- Buttons layout ---
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.button("▶️ Start", on_click=start_timer)
with col2:
    st.button("⏸️ Pause", on_click=pause_timer)
with col3:
    st.button("⏹️ Stop", on_click=stop_timer)
with col4:
    st.button("🔄 Reset", on_click=reset_timer)

# --- Display placeholder ---
count_display = st.empty()

# --- Timer update logic ---
if st.session_state.is_running and st.session_state.time_left > 0:
    for _ in range(st.session_state.time_left):
        if not st.session_state.is_running:
            break
        count_display.markdown(f"""
            <h1 style='text-align: center; color: red; font-size: 72px;'>
                {st.session_state.time_left}
            </h1>
        """, unsafe_allow_html=True)
        time.sleep(1)
        st.session_state.time_left -= 1
    st.session_state.is_running = False

# Final value shown
count_display.markdown(f"""
    <h1 style='text-align: center; color: red; font-size: 72px;'>
        {st.session_state.time_left}
    </h1>
""", unsafe_allow_html=True)
