import streamlit as st
from google import genai

def show_formula_api():
    st.title("📡 Formula API")
    st.subheader("Get Exam-Ready Formulas for Last-Minute Revisions!")

    query = st.text_input("Enter Topic Path", placeholder="e.g., /physics/thermodynamics")

    if query:
        st.code(f"GET /api/v1{query}", language="bash")

    if st.button("Execute Request"):
        if not query or len(query) < 3:
            st.warning("Please enter a valid topic path first.")
            return
        
        if "GEMINI_API_KEY" not in st.secrets:
            st.error("Missing API Key")
            return
            
        try:
            api_key = st.secrets["GEMINI_API_KEY"].strip()
            client = genai.Client(api_key=api_key)
            model_id = "gemini-1.5-flash"
            prompt = f"You are a high-performance technical documentation engine specialized in generating ultra-compact, exam-optimized JEE formula sheets for rapid revision and advanced problem-solving. The user is requesting the 'formula sheet' for the topic path: {query}. Generate a highly structured Markdown response with professional formatting and proper LaTeX notation using $$...$$ for display equations and $...$ for inline notation. The response must contain the following sections exactly: 1. Key Equations — Include all critical formulas, identities, transformations, standard results, shortcuts, derived forms, approximations, and commonly used relations relevant to the requested topic. Group formulas logically, define important symbols briefly, include alternate forms frequently used in JEE, and maintain mathematically correct notation throughout. Prioritize high-frequency and problem-solving-oriented equations only. 2. Constraints & Edge Cases — Mention assumptions, limitations, invalid conditions, sign conventions, approximation breakdowns, convergence conditions, undefined cases, neglected effects, and conceptual traps where formulas fail or produce incorrect results. Include common mistakes students make in exams and important edge scenarios frequently tested in JEE Main and Advanced. 3. Essential Constants — Include all relevant constants with symbol, numerical value, SI units, standard approximations used in JEE, and important conversion factors wherever applicable. Keep the response dense, technical, concise, professional, highly scannable, and optimized for last-minute revision under exam pressure. Avoid storytelling, beginner explanations, motivational language, unnecessary derivations, filler text, or conversational tone. Maintain consistent notation, clean Markdown structure, and maximum information density. If the topic path is invalid, unsupported, ambiguous, or empty, politely request a valid topic path such as /physics/thermodynamics, /chemistry/chemical-kinetics, or /mathematics/probability."

            with st.spinner("Fetching from QSense API..."):
                response = client.models.generate_content(
                    model=model_id,
                    contents=prompt
                        )
                        
            if response.text:
                st.success("Request Successful")
                st.markdown("---")

                st.markdown(response.text)
            
            else:
                st.warning("The API returned an empty response.")

        except Exception as e:
            st.error(f"API Error: {str(e)}")