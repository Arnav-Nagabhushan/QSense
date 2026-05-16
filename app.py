import streamlit as st

from sidebar.home import show_home
from sidebar.performance_analyzer import analyze_performance 
from sidebar.test_simulator import simulate_test
from sidebar.xplain import xplain
from sidebar.lens import show_lens
from sidebar.formula_api import show_formula_api
from sidebar.synapse import show_synapse
from components.chatbot import show_chatbot

st.set_page_config(page_title="QSense", layout="wide")

st.badge("Beta")
st.title("🧠 QSense")
st.caption("From confusion to clarity.")

st.sidebar.header("Main Menu")
feature = st.sidebar.radio("Go to", ["Home", "Test Simulator", "Xplain", "Performance Analyzer", "QSense Lens", "Formula API", "QSense Synapse"]))


st.header(feature)

if feature == "Xplain":
    xplain()
    st.divider()
    show_chatbot()

elif feature == "Performance Analyzer":
    analyze_performance()
    st.divider()
    show_chatbot()

elif feature == "QSense Lens":
    show_lens()
    st.divider()
    show_chatbot()

elif feature == "QSense Synapse":
    show_synapse()
    st.divider()
    show_chatbot()


elif feature == "Formula API":
    show_formula_api()
    st.divider()
    show_chatbot()

elif feature == "Home":
    show_home()
    st.divider()
    show_chatbot()

elif feature == "Test Simulator":
    simulate_test()
    st.divider()
    show_chatbot()