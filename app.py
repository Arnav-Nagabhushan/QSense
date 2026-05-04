import streamlit as st

from sidebar.home import show_home
from sidebar.performance_analyzer import analyze_performance
from sidebar.test_simulator import simulate_test

st.set_page_config(page_title="QSense", layout="wide")

st.title("🧠 QSense")
st.caption("From confusion to clarity.")

feature = st.sidebar.selectbox(
    "Choose Feature",
    ["Home", "Performance Analyzer", "Test Simulator"]
)

st.header(feature)

if feature == "Home":
    show_home()

elif feature == "Performance Analyzer":
    analyze_performance()

elif feature == "Test Simulator":
<<<<<<< HEAD
    simulate_test()
=======
    simulate_test()
>>>>>>> da8c1064f663d3e7b46067fa57c3713d9c4a9720
