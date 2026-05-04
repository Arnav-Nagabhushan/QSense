import streamlit as st
import time

def show_home():
    with st.spinner("Loading the webpage..."):
        time.sleep(2)

    st.write("Welcome to 🧠 QSense")

    time.sleep(1)
    st.markdown("-> Analyze your academic performance")
    time.sleep(0.5)

    st.markdown("-> Take smart tests")
    time.sleep(0.5)

    st.markdown("-> Improve weak areas")
    time.sleep(0.5)

    st.markdown("-> and many more!")
    time.sleep(1)

    st.divider()
    
    st.write("Start by selecting a feature from the sidebar.")

    st.write("Start by selecting a feature from the sidebar.")
