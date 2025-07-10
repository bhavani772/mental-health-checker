import streamlit as st

# Question bank grouped by categories
stress_questions = [
    "I find it hard to relax",
    "I feel tired or have little energy",
    "I have difficulty concentrating",
    "I feel overwhelmed by responsibilities",
    "I feel irritated or annoyed easily",
    "I have trouble managing time or tasks"
]

anxiety_questions = [
    "I feel nervous or anxious",
    "I worry excessively about different things",
    "I have trouble sleeping due to worry",
    "I feel on edge or restless",
    "I have physical symptoms (e.g., sweating, trembling) when anxious",
    "I avoid situations that cause me anxiety"
]

depression_questions = [
    "I feel sad or hopeless",
    "I have lost interest in activities I used to enjoy",
    "I feel worthless or guilty",
    "I feel like life is not worth living",
    "I feel unmotivated to do daily activities",
    "I feel isolated or disconnected from others"
]

# Scoring options
options = {
    "": None,
    "Never": 0,
    "Sometimes": 1,
    "Often": 2,
    "Always": 3
}

# Streamlit UI
st.set_page_config(page_title="Mental Health Kiosk", layout="centered")
st.title("\U0001F9E0 Mental Health Self-Assessment")
st.write("Please answer all questions to receive a summary. Your answers remain private.")

def ask_questions(questions, section_key):
    scores = []
    for i, q in enumerate(questions):
        answer = st.radio(q, list(options.keys())[1:], key=f"{section_key}_{i}")
        scores.append(options.get(answer))
    return scores

with st.form("mental_health_form"):
    stress_scores = ask_questions(stress_questions, "stress")
    anxiety_scores = ask_questions(anxiety_questions, "anxiety")
    depression_scores = ask_questions(depression_questions, "depression")

    submitted = st.form_submit_button("Submit")

if submitted:
    if None in stress_scores + anxiety_scores + depression_scores:
        st.error("\U0001F6D1 Please answer all the questions before submitting.")
    else:
        st.success("\u2705 Assessment Complete")
        st.subheader("\U0001F4DD Your Mental Health Summary")

        def interpret_score(score):
            if score <= 5:
                return ("Low", "\U0001F7E2")   # Green circle
            elif score <= 11:
                return ("Moderate", "\U0001F7E1")  # Yellow circle
            else:
                return ("High", "\U0001F534")   # Red circle

        stress_score = sum(stress_scores)
        anxiety_score = sum(anxiety_scores)
        depression_score = sum(depression_scores)

        stress_level, stress_icon = interpret_score(stress_score)
        anxiety_level, anxiety_icon = interpret_score(anxiety_score)
        depression_level, depression_icon = interpret_score(depression_score)

        total_score = stress_score + anxiety_score + depression_score
        if total_score <= 15:
            overall_status = ("Mentally Stable", "\U0001F7E2")
        elif total_score <= 25:
            overall_status = ("Needs Attention", "\U0001F7E1")
        else:
            overall_status = ("At Risk - Seek Help", "\U0001F534")

        st.markdown(f"**Stress Level:** {stress_icon} {stress_level}  ")
        st.markdown(f"**Anxiety Level:** {anxiety_icon} {anxiety_level}  ")
        st.markdown(f"**Depression Level:** {depression_icon} {depression_level}  ")
        st.markdown("---")
        st.markdown(f"### \U0001F9FE Overall Mental Health: {overall_status[1]} {overall_status[0]}")

        st.markdown("---")
        st.subheader("\U0001F4CC Suggested Advice")
        if overall_status[0] == "Mentally Stable":
            st.info("Keep taking care of your mental health with good habits, rest, and regular check-ins.")
        elif overall_status[0] == "Needs Attention":
            st.warning("You're experiencing mild to moderate symptoms. Consider speaking to a counselor or support group.")
        else:
            st.error("Please seek help from a mental health professional immediately.")
