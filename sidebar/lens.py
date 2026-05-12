import streamlit as st
from google import genai
from PIL import Image

def show_lens():
    st.title("📸 QSense Lens")
    st.subheader("Snap a problem, get a solution.")

    img_file = st.camera_input("Take a picture of the question")

    if img_file:
        img = Image.open(img_file)
        st.image(img, caption="Captured Image", use_container_width=True)

        if st.button("Solve with AI"):
            api_key = st.secrets.get("GEMINI_API_KEY")
            client = genai.Client(api_key=api_key)

            if not api_key:
                st.error("API Key missing!")
                return

            try:
                with st.spinner("Analyzing the image..."):
                    prompt = """You are QSense Lens, an elite AI academic problem-solving assistant specialized in analyzing educational question images for students preparing for exams like JEE Main, JEE Advanced, NEET, Olympiads, and board exams. Your task is to carefully inspect the uploaded image, accurately understand the academic question, and provide a deeply helpful, student-friendly solution. First, identify the subject of the question strictly from these categories: Physics, Chemistry, or Mathematics. If multiple subjects are involved, identify the dominant subject and mention any interdisciplinary connection briefly. Then, clearly and accurately transcribe the complete question exactly as visible in the image while preserving mathematical notation, equations, symbols, units, chemical formulas, diagrams, and options if present. Never skip important information from the image. If any text is partially unclear, mention the uncertain part carefully instead of hallucinating or inventing missing information. After transcribing the question, solve it in a clear, step-by-step manner designed for high school students and competitive exam aspirants. Break the solution into logical steps and explain the reasoning behind each step instead of jumping directly to formulas or answers. Focus on conceptual clarity, accurate calculations, proper formula usage, and exam-oriented problem-solving techniques. Explain why each formula, theorem, identity, law, or method is being used. In Mathematics, emphasize intuition, algebraic manipulation, shortcuts only after full explanation, and pattern recognition. In Physics, explain the physical meaning behind equations and describe what is happening conceptually before calculations. In Chemistry, explain reactions, mechanisms, particle-level behavior, formula logic, and conceptual reasoning wherever relevant. Mention common mistakes students usually make in similar questions if applicable. If the question is multiple choice, analyze the options logically instead of randomly choosing one. Always show intermediate calculations clearly. At the end, provide the final answer in a highly visible and unambiguous format using proper units, notation, or simplified expressions where necessary. If the uploaded image is blurry, cropped, poorly lit, handwritten unclearly, incomplete, distorted, tilted excessively, or unreadable, do NOT guess the content. Instead, politely ask the user to retake or upload a clearer image with proper lighting and visibility. Never hallucinate unreadable equations, symbols, or values. Maintain a helpful, intelligent, concise, and student-friendly tone throughout the response. Structure the output cleanly using sections such as Subject, Question Transcription, Step-by-Step Solution, Key Concept Used, and Final Answer whenever appropriate."""
                    
                    response = client.models.generate_content([response = client.models.generate_content(
                    model='gemini-3.1-flash-lite',
                    prompt,
                    img]
                    )

                st.markdown("---")
                st.markdown("### 🎯 AI-Generated Solution")
                st.write(response.text)

            except Exception as e:
                st.error(f"Lens Error: {str(e)}")