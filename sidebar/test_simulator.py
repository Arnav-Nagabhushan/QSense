import streamlit as st
import time
from question_bank import question_bank as questions


def calculate_percentage(score, total):
    if total == 0:
        return 0
    return (score / total) * 100


def simulate_test():
    if "wrong_topics" not in st.session_state:
        st.session_state.wrong_topics = {}

    if "q_index" not in st.session_state:
        st.session_state.q_index = 0

    if "total_score" not in st.session_state:
        st.session_state.total_score = 0

    if "answered" not in st.session_state:
        st.session_state.answered = False

    subject = st.selectbox("Choose Subject", questions)
    subject_questions = questions[subject]

    st.info(f"Question {st.session_state.q_index + 1} of {len(subject_questions)}")

    question = subject_questions[st.session_state.q_index]
    st.write(question["question"])

    selected_option = st.radio(
        "Choose an answer:",
        question["options"],
        disabled=st.session_state.answered
    )

    if st.button("Submit Answer") and not st.session_state.answered:
        st.session_state.answered = True

        if selected_option == question["answer"]:
            st.success("✅ Correct!")
            st.session_state.total_score += 1
        else:
            st.error(f"❌ Wrong! Correct answer: {question['answer']}")

            topic = question["topic"]
            if topic not in st.session_state.wrong_topics:
                st.session_state.wrong_topics[topic] = 0

            st.session_state.wrong_topics[topic] += 1

        st.info(f"Explanation: {question['explanation']}")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Next Question"):
            if st.session_state.q_index < len(subject_questions) - 1:
                st.session_state.q_index += 1
                st.session_state.answered = False

    with col2:
        if st.button("Restart Test"):
            st.session_state.q_index = 0
            st.session_state.total_score = 0
            st.session_state.answered = False
            st.session_state.wrong_topics = {}

    if st.button("Finish Test"):
        show_result(len(subject_questions))


def show_result(total_qs):
    score = st.session_state.total_score

    st.success("🎉 Test Completed!")

    with st.spinner("Calculating your score..."):
        time.sleep(2)

    st.subheader("📊 Final Result")
    st.write(f"Score: {score}/{total_qs}")

    percentage = calculate_percentage(score, total_qs)
    st.write(f"Percentage: {percentage:.2f}%")

    st.subheader("🧠 Weak Areas")

    if st.session_state.wrong_topics:
        sorted_topics = sorted(
            st.session_state.wrong_topics.items(),
            key=lambda x: x[1],
            reverse=True
        )

        weakest = sorted_topics[0][0]

        for topic, count in sorted_topics:
            st.warning(f"{topic} → {count} mistakes")

        st.info(f"Focus more on {weakest}")
    else:
        st.success("No weak areas detected!")
