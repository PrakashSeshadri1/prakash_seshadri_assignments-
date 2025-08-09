# SimpleLog.py
import streamlit as st
from datetime import datetime, date
import json
import os

LOG_FILE = "simple_log.json"

# ------------------- Helpers -------------------
def load_logs():
    """Load logs from file."""
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_logs(logs):
    """Save logs to file."""
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        json.dump(logs, f, indent=4)

def add_log(activity):
    """Add a new log entry."""
    logs = load_logs()
    now = datetime.now()
    logs.append({
        "date": now.strftime("%Y-%m-%d"),
        "time": now.strftime("%H:%M:%S"),
        "activity": activity.strip()
    })
    save_logs(logs)

def clear_logs():
    """Clear all logs."""
    open(LOG_FILE, "w", encoding="utf-8").write("[]")

# ------------------- UI -------------------
st.set_page_config(page_title="Simple Log", page_icon="📝")
st.title("📝 Multi-Day Simple Daily Log")

# Current date & time
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
st.write(f"📅 Current Date & Time: **{now}**")

# Input form
with st.form("log_form", clear_on_submit=True):
    activity = st.text_area("Enter today's activity")
    submitted = st.form_submit_button("Add to Log")

    if submitted:
        if activity.strip() == "":
            st.warning("Please enter an activity.")
        else:
            add_log(activity)
            st.success("Activity logged!")

# Load logs
logs = load_logs()

# Date filter
st.subheader("🔍 Search Logs by Date")
selected_date = st.date_input("Select Date", value=date.today())

# Filter logs by selected date
filtered_logs = [log for log in logs if log["date"] == selected_date.strftime("%Y-%m-%d")]

# Show logs (latest first)
st.subheader(f"📜 Log History for {selected_date}")
if filtered_logs:
    for entry in sorted(filtered_logs, key=lambda x: (x["date"], x["time"]), reverse=True):
        st.write(f"[{entry['date']} {entry['time']}] {entry['activity']}")
else:
    st.info("No logs for this date.")

# Show all logs option
if st.checkbox("📂 Show All Logs"):
    st.write("### All Entries (Latest First)")
    for entry in sorted(logs, key=lambda x: (x["date"], x["time"]), reverse=True):
        st.write(f"[{entry['date']} {entry['time']}] {entry['activity']}")

# Clear logs button
if st.button("🗑 Clear All Logs"):
    clear_logs()
    st.warning("All logs cleared!")
