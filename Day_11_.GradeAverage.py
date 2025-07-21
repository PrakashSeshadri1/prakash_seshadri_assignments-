import streamlit as st

# Page configuration
st.set_page_config(page_title="Day 11 - Grade Average", page_icon="🎓")

# Title and symbol
st.markdown("# 🎓 Day 11: Grade Average Assignment")
st.write("Enter 5 test scores to calculate the average and find out if the student passed or failed.")

# Input section inside a form
with st.form("grade_form"):
    score1 = st.number_input("Enter Test Score 1", min_value=0.0, max_value=100.0, step=1.0)
    score2 = st.number_input("Enter Test Score 2", min_value=0.0, max_value=100.0, step=1.0)
    score3 = st.number_input("Enter Test Score 3", min_value=0.0, max_value=100.0, step=1.0)
    score4 = st.number_input("Enter Test Score 4", min_value=0.0, max_value=100.0, step=1.0)
    score5 = st.number_input("Enter Test Score 5", min_value=0.0, max_value=100.0, step=1.0)

    submitted = st.form_submit_button("Calculate Average")

# Result section
if submitted:
    scores = [score1, score2, score3, score4, score5]
    average = sum(scores) / 5

    st.subheader("📊 Results")
    st.write(f"**Scores:** {scores}")
    st.write(f"**Average Score:** {average:.2f}")

    if average >= 40:
        st.success("🎉 Result: PASS")
    else:
        st.error("❌ Result: FAIL")

# Footer
st.markdown("---")
st.markdown("📘 *App by Prakash Seshadri*")
