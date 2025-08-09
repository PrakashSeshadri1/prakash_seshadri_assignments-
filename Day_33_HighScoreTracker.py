# Day_33_HighScoreTracker.py
import streamlit as st
import json
import os
from datetime import datetime

SCORE_FILE = "highscores.json"

# ------------------- Data Handling -------------------
def load_scores():
    if os.path.exists(SCORE_FILE):
        with open(SCORE_FILE, "r") as f:
            return json.load(f)
    return []

def save_scores(scores):
    with open(SCORE_FILE, "w") as f:
        json.dump(scores, f, indent=4)

# ------------------- UI Setup -------------------
st.set_page_config(page_title="High Score Tracker", page_icon="🎯")
st.title("🎯 High Score Tracker")

# Show actual date & time (non-editable)
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
st.write(f"📅 Current Date & Time: **{now}**")

# Load into session state
if "scores" not in st.session_state:
    st.session_state.scores = load_scores()

if "edit_index" not in st.session_state:
    st.session_state.edit_index = None

# ------------------- Add Score Form -------------------
with st.form("add_score_form", clear_on_submit=True):
    player_name = st.text_input("Player Name")
    score = st.number_input("Score", min_value=0, step=1)
    submitted = st.form_submit_button("Add Score")

    if submitted:
        if player_name.strip() == "":
            st.warning("Please enter a player name.")
        else:
            st.session_state.scores.append({
                "name": player_name.strip(),
                "score": score
            })
            st.session_state.scores.sort(key=lambda x: x["score"], reverse=True)
            save_scores(st.session_state.scores)
            st.success(f"Score added for {player_name}!")

# ------------------- Display Scores -------------------
st.subheader("🏆 High Scores")

if st.session_state.scores:
    for idx, entry in enumerate(st.session_state.scores):
        col1, col2, col3, col4 = st.columns([2, 2, 1, 1])

        # Show player info
        col1.write(f"{idx+1}. {entry['name']}")
        col2.write(f"Score: {entry['score']}")

        # Edit button
        if col3.button("✏ Edit", key=f"edit_{idx}"):
            st.session_state.edit_index = idx

        # Delete button
        if col4.button("🗑 Delete", key=f"delete_{idx}"):
            st.session_state.scores.pop(idx)
            save_scores(st.session_state.scores)
            st.rerun()

    # Edit form
    if st.session_state.edit_index is not None:
        st.write("---")
        edit_idx = st.session_state.edit_index
        st.write(f"Editing score for **{st.session_state.scores[edit_idx]['name']}**")
        new_score = st.number_input(
            "New Score",
            min_value=0,
            step=1,
            value=st.session_state.scores[edit_idx]['score'],
            key="edit_score_input"
        )
        if st.button("Save Changes"):
            st.session_state.scores[edit_idx]['score'] = new_score
            st.session_state.scores.sort(key=lambda x: x["score"], reverse=True)
            save_scores(st.session_state.scores)
            st.session_state.edit_index = None
            st.rerun()

else:
    st.info("No scores yet. Add one above!")

# ------------------- Announce Winners -------------------
if st.button("📢 Announce Top 2 Winners"):
    if len(st.session_state.scores) >= 2:
        first = st.session_state.scores[0]
        second = st.session_state.scores[1]
        st.success(f"🥇 {first['name']} with {first['score']} points!")
        st.success(f"🥈 {second['name']} with {second['score']} points!")
    elif len(st.session_state.scores) == 1:
        first = st.session_state.scores[0]
        st.success(f"🥇 {first['name']} with {first['score']} points!")
        st.info("Only one player available.")
    else:
        st.warning("No scores to announce.")

# ------------------- Clear All -------------------
if st.button("Clear All Scores"):
    st.session_state.scores = []
    save_scores([])
    st.warning("All scores cleared!")
