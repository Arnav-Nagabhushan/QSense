import streamlit as st

from sidebar.home import show_home
from sidebar.performance_analyzer import analyze_performance
from sidebar.test_simulator import simulate_test
from sidebar.xplain import xplain

st.set_page_config(page_title="QSense", layout="wide")

st.title("🧠 QSense")
st.caption("From confusion to clarity.")

feature = st.sidebar.selectbox(
    "Choose Feature",
    ["Home", "Performance Analyzer", "Test Simulator", "Xplain"]
)

st.header(feature)

if feature == "Home":
    show_home()

elif feature == "Performance Analyzer":
    analyze_performance()

elif feature == "Test Simulator":
    simulate_test() 

elif feature == "Xplain":
    xplain()