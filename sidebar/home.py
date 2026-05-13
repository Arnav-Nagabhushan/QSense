import streamlit as st
import time
import random
from streamlit_extras.metric_cards import style_metric_cards

def show_home():
    quotes = [
    "“The only way to learn mathematics is to do mathematics.” – Paul Halmos",
    "“Physics is about questioning everything.” – Elon Musk",
    "“Don't count the days, make the days count.”"
    ]
    
    for i in range(5):
        st.progress(i)
    st.sidebar.markdown(f"> Daily Motivation: {random.choice(quotes)}")

    st.write("Welcome to 🧠 QSense")
    st.markdown("""### Your Personalized AI Tutor" 
                    Master complex topics, visualize mind maps and solve any problem with :rainbow[3.1—Flash—Lite] precision!
                """)

    st.divider

    st.title("🧠 QSense Dashboard")

    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)

    col1.metric(label="Synapses", value=random.choice(1267, 2367), delta=f"{random.choice(12.00, 14.00)}%")
    col2.metric(label="Solved", value=random.choice(867, 1967), delta=f"{random.choice(5.00, 7.00)}%")
    col3.metric(label="Accuracy", value=f"{random.choice(97.00, 99.00)}%", delta=f"{random.choice(0.4, 0.6)}%")
    col4.metric(label="Streak", value=random.choice(17, 67), delta="🔥")

    style_metric_cards(
        background_color="#1E1E1E", 
        border_left_color="#4CAF50",
        border_size_px=1,
        box_shadow=True
    )    

    time.sleep(1)
    st.markdown("-> Analyze your academic performance")
    time.sleep(0.5)

    st.markdown("-> Take :green[smart tests]")
    time.sleep(0.5)

    st.markdown("-> Improve :red[weak areas]")
    time.sleep(0.5)

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
            st.caption("Scan and solve any JEE problem instantly.")
            if st.button("Launch Lens", key="home_lens"):
                st.session_state.tool = "QSense Lens" # Logic to switch tools

    with t2:
        with st.container(border=True):
            st.subheader("🧠 Synapse")
            st.caption("Generate AI mind maps for deep revision.")
            if st.button("Launch Synapse", key="home_synapse"):
                st.session_state.tool = "QSense Synapse"

    with t3:
        with st.container(border=True):
            st.subheader("📈 Analyzer")
            st.caption("Track your performance and weak spots.")
            if st.button("Launch Analyzer", key="home_analyzer"):
                st.session_state.tool = "Performance Analyzer"

