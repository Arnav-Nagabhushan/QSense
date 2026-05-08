import streamlit as st

from sidebar.home import show_home
from sidebar.performance_analyzer import analyze_performance
from sidebar.test_simulator import simulate_test
from sidebar.xplain import xplain
from sidebar.lens import show_lens
from sidebar.formula_api import show_formula_api
from sidebar.synapse import show_synapse

st.set_page_config(page_title="QSense", layout="wide")

st.title("🧠 QSense")
st.caption("From confusion to clarity.")

st.sidebar.header("Main Menu")
feature = st.sidebar.radio("Go to", ["Home", "Test Simulator"])

st.sidebar.markdown("---")

st.sidebar.header("AI-Powered Tools")
tool = st.sidebar.selectbox("Navigate", ["Select a Tool...", "Xplain", "Performance Analyzer", "QSense Lens", "Formula API", "QSense Synapse"])


st.header(feature)

if tool == "Xplain":
    xplain()

elif tool == "Performance Analyzer":
    analyze_performance()

elif tool == "QSense Lens":
    show_lens()

elif tool == "QSense Synapse":
    show_synapse()


elif tool == "Formula API":
    show_formula_api()

elif feature == "Home":
    show_home()

elif feature == "Test Simulator":
    simulate_test()