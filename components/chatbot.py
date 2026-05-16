import streamlit as st
from google import genai

def show_chatbot():
    with st.expander("💬 Chat with QSense AI Mentor!", expanded=False):
        st.caption("24x7 Doubt Solving Assistance")

    client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

    if "global_chat_history" not in st.session_state: # Page-specific history
            st.session_state.global_chat_history = [
                {"role": "AI Assistant", "content": "Need help with a step on this page? Ask me!"}
            ]

    chat_container = st.container(height=300)

    with chat_container:
            for message in st.session_state.global_chat_history:
                with st.chat_message(message["role"]):
                    st.write(message["content"])

    if user_query := st.chat_input("Ask a quick doubt...", key="chat_input"):
        with chat_container:
            with st.chat_message("User"):
                st.write(user_query)
        st.session_state.global_chat_history.append({"role": "user", "content": user_query})

        with chat_container:
            with st.chat_message("assistant"):
                system_instruction = "You are QSense AI, a precise, helpful engineering exam study mentor."
                try:
                    response = client.models.generate_content_stream(
                        model='gemini-3.1-flash-lite',
                        contents=user_query,
                        config={"system_instruction": system_instruction}
                    )
                    full_response = st.write_stream(response)
                    st.session_state.global_chat_history.append({"role": "assistant", "content": full_response})
                    
                    st.rerun()
                    
                except Exception as e:
                    st.error(f"Error: {e}")