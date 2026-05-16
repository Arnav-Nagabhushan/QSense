import streamlit as st
import time
import random
import pandas as pd
from streamlit_extras.metric_cards import style_metric_cards
from streamlit_extras.add_vertical_space import add_vertical_space
from components.chatbot import show_chatbot


def show_home():
    quotes = [
    "“The only way to learn mathematics is to do mathematics.” – Paul Halmos",
    "“Physics is about questioning everything.” – Elon Musk",
    "“Don't count the days, make the days count.”"
    ]
    
    st.sidebar.markdown(f"> Daily Motivation: {random.choice(quotes)}")

    st.write("Welcome to 🧠 QSense")
    st.markdown("### Your Personalized AI Tutor") 
    st.caption("Master complex topics, visualize mind maps and solve any problem with :rainbow[Gemini 3.1—Flash—Lite] precision!")

    st.divider()

    st.badge("Beta")
    st.title("🧠 QSense Dashboard")

    synapse_val = random.randint(1267, 2367)
    solved_val = random.randint(867, 1967)
    accuracy_val = round(random.uniform(97.0, 99.9), 1)
    streak_val = random.randint(17, 67)

    # Layout
    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)

    # Display Metrics
    col1.metric(label="Synapses Generated", value=f"{synapse_val:,}", delta="12%")
    col2.metric(label="Queries Solved", value=f"{solved_val:,}", delta="5.2%")
    col3.metric(label="Average Accuracy", value=f"{accuracy_val}%", delta="0.5%")
    col4.metric(label="Average Streak", value=f"{streak_val} Days", delta="🔥")

    style_metric_cards(
        background_color="#1E1E1E",
        border_left_color="#4CAF50",
        border_size_px=1,
        box_shadow=True
    )

    time.sleep(1)
    st.markdown("-> Analyze your academic performance")
    time.sleep(0.5)
    add_vertical_space(1)
    st.markdown("-> Take :green[smart tests]")
    time.sleep(0.5)
    add_vertical_space(1)
    st.markdown("-> Improve :red[weak areas]")
    time.sleep(0.5)
    add_vertical_space(1)
    st.markdown("-> and many more!")
    time.sleep(1)

    st.divider()
    
    if st.button("Get Started →"):
        st.write("Start by selecting a feature from the sidebar.")

    st.divider

    st.write("### 🛠️ Quick Access Tools")
    t1, t2, t3 = st.columns(3)

    with t1:
        with st.container(border=True):
            st.subheader("📷 Lens")
            st.caption("Scan and solve any problem instantly.")
            if st.button("Launch Lens", key="home_lens"):
                st.session_state.tool = "QSense Lens" # Logic to switch tools

    with t2:
        with st.container(border=True):
            st.subheader("🧠 Synapse")
            st.caption("Generate AI mind maps for quick revision.")
            if st.button("Launch Synapse", key="home_synapse"):
                st.session_state.tool = "QSense Synapse"

    with t3:
        with st.container(border=True):
            st.subheader("📈 Analyzer")
            st.caption("Track your performance and weak spots.")
            if st.button("Launch Analyzer", key="home_analyzer"):
                st.session_state.tool = "Performance Analyzer"

    st.divider()
    st.write("### 📈 Average Accuracy Over Last 5 Mock Tests")
    scores = sorted([random.randint(65, 98) for _ in range(5)]) # Random scores from 65% to 98% in ascending order
    chart_data = {
        "Mock Test": ["Test 1", "Test 2", "Test 3", "Test 4", "Test 5"],
        "Average Global Score (%)": scores
    }
    
    df = pd.DataFrame(chart_data)
    df = df.set_index("Mock Test") 
    st.line_chart(df, color="#4CAF50")

    st.markdown("---")
    st.caption("⚡ Powered by Gemini 3.1 Flash-Lite | Built for educational purposes")

