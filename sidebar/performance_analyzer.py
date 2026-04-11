import streamlit as st
import time

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

            st.write(f"Strongest: {strongest_subject} ({strongest_marks})")
            st.write(f"Weakest: {weakest_subject} ({weakest_marks})")

        except:
            st.error("Invalid format! Use: Mathematics:80, Physics:60")
