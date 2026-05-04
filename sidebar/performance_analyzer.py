import streamlit as st
import time
from logic.brain import get_ai_recommendations

def parse_input_marks(marks):
    marks_dict = {}

    subjects = marks.split(",")

    for item in subjects:
        parts = item.split(":")
        name = parts[0].strip()
        score = int(parts[1].strip())
        marks_dict[name] = score

    return marks_dict


def calculate_percentage(total, count):
    if count == 0:
        return 0
    return total / count


def analyze_performance():
    strongest_subject = "N/A"
    strongest_marks = 0
    weakest_subject = "N/A"
    weakest_marks = 0
    
    marks = st.text_input(
        "Enter your marks",
        placeholder="Mathematics:80, Physics:60, Chemistry:90"
    )

    st.caption("Format: Subject:Marks, comma-separated values")

    if st.button("Analyze"):
        st.subheader("🧠 Decoding Your Performance...")
        time.sleep(0.5)

        with st.spinner("Analyzing your performance..."):
            time.sleep(2)

        try:
            marks_dict = parse_input_marks(marks)

            total = sum(marks_dict.values())

            average = calculate_percentage(total, len(marks_dict))
            
            st.session_state.avg_score = average
            st.session_state.weakest_subject = min(marks_dict, key=marks_dict.get)
            st.session_state.strongest_subject = max(marks_dict, key=marks_dict.get)
            st.session_state.weak_list = [st.session_state.weakest_subject]

            strongest_marks = marks_dict[st.session_state.strongest_subject]
            weakest_marks = marks_dict[st.session_state.weakest_subject]


            st.subheader("📊 Results")
            if average == 100:
                st.success(f"Perfect score! You're averaging {average:.2f}!")
                st.balloons()
                st.toast("You got 100 percentile! 🏆")
            elif average >= 85:
                st.success(f"Outstanding: {average:.2f}")
                st.balloons()
                st.toast("Brilliant Performance! 🏆")

            total = sum(marks_dict.values())
            average = calculate_percentage(total, len(marks_dict))

            strongest_subject = max(marks_dict, key=marks_dict.get)
            weakest_subject = min(marks_dict, key=marks_dict.get)

            strongest_marks = marks_dict[strongest_subject]
            weakest_marks = marks_dict[weakest_subject]

            st.subheader("📊 Results")

            if average == 100:
                st.success(f"Perfect score: {average:.2f}")
            elif average >= 85:
                st.success(f"Outstanding: {average:.2f}")
            elif average >= 60:
                st.info(f"Average: {average:.2f}")
            else:
                st.warning(f"Needs improvement: {average:.2f}")

            # Use f-strings for simple, clear formatting
            st.write(f"Strongest Subject: {st.session_state.strongest_subject} ({strongest_marks})")
            st.write(f"Weakest Subject: {st.session_state.weakest_subject} ({weakest_marks})")

        except:
            st.error("Invalid format! Use: Mathematics:80, Physics:60")

    if "avg_score" in st.session_state:
        st.divider() 
        if st.button("✨ Get Study Tips", key="ai_study_plan_btn"):
            with st.spinner("Consulting Experienced AI Mentor..."):
                advice = get_ai_recommendations(st.session_state.weak_list, st.session_state.avg_score)

            with st.status("🧠 AI Mentor is analyzing your performance...", expanded=True) as status:
                st.write("Getting Smart Recommendations...")
                st.success("Analysis Complete!")
                st.markdown("### 🧠 Personalized Study Tips just for you!")
                st.write_stream(advice)
            st.write(f"Strongest: {strongest_subject} ({strongest_marks})")
            st.write(f"Weakest: {weakest_subject} ({weakest_marks})")