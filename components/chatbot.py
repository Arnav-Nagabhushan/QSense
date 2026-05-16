import streamlit as st
from google import genai

def show_chatbot():
    with st.expander("💬 Chat with Q-Bit!", expanded=True):
        st.caption("Ask. Learn. Solve. Repeat.")

        client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

        if "global_chat_history" not in st.session_state:
            st.session_state.global_chat_history = [
                {"role": "assistant", "content": "Hi! I’m **Q-Bit** 🧠 Your AI study partner for mastering concepts, solving doubts, and making tough topics finally click"}
            ]

        chat_container = st.container(height=300)

        with chat_container:
            for message in st.session_state.global_chat_history:
                if message["role"] == "user":
                    with st.chat_message("user", avatar="👨‍💻"):
                        st.markdown(f"**You**\n\n{message['content']}")
                else:
                    with st.chat_message("assistant", avatar="🧠"):
                        st.markdown(f"**Q-Bit**\n\n{message['content']}")

        if user_query := st.chat_input("Confused? Ask Q-Bit 🧠", key="chat_input"):            
            with chat_container:
                with st.chat_message("user", avatar="👨‍💻"):
                    st.markdown(f"**Aspirant**\n\n{user_query}")
            st.session_state.global_chat_history.append({"role": "user", "content": user_query})

            with chat_container:
                with st.chat_message("assistant", avatar="🧠"):
                    st.markdown("**Q-Bit**")
                    system_instruction = ("You are Q-Bit, the elite AI mentor inside QSense for students, specializing in Physics, Chemistry, and Mathematics; explain concepts and solve problems step-by-step with deep intuition, clear logic, concise exam-oriented reasoning, motivating student-friendly tone, strong conceptual clarity, practical analogies, and clean structured explanations while making difficult topics feel simple, engaging, and approachable.")
                    
                    try:
                        with st.spinner("🧠 Q-Bit is analyzing your query..."):
                            response = client.models.generate_content_stream(
                                model='gemini-3.1-flash-lite',
                                contents=user_query,
                                config={"system_instruction": system_instruction}
                            )
                            full_response = st.write_stream(response)
                        
                        st.session_state.global_chat_history.append({"role": "assistant", "content": full_response})
                        st.rerun()
                        
                    except Exception as e:
                        st.error(f"Error connecting to Q-Bit: {e}")