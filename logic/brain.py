from google import genai
import streamlit as st

def get_ai_recommendations(weak_topics, avg_score):
    # Setup client
    client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
    
    # 2026 PRO TIP: Flash-Lite is the most stable free model
    model_id = "gemini-2.5-flash-lite"
    
    prompt = f"You are a helpful and knowledgeable tutor assisting a student in improving their academic performance. The student's current average score is {avg_score}%. The topics they need to improve are: {', '.join(weak_topics)}. Based on this information, analyze their situation and focus on helping them strengthen their understanding and performance in these specific topics. Provide exactly 3 short and practical study tips tailored to these weak areas. Each tip should be clear, actionable, and focused on improving conceptual understanding, problem-solving skills, and reducing common mistakes. Avoid generic advice such as 'study more' or 'revise regularly'. Keep each tip concise (1–2 lines), easy to understand, and suitable for a high school student preparing for exams like JEE. Ensure the tips are specific, useful, and different from each other."
    try:
        response = client.models.generate_content_stream(
        model='gemini-2.5-flash-lite',
        contents=prompt
        )
        
        for chunk in response:
            yield chunk.text

    except Exception as e:
        # Switch 'return' to 'yield' for generators!
        if "503" in str(e):
            yield "🚀 The AI servers are super busy. Please wait 10 seconds and click again!"
        elif "429" in str(e):
            yield "🕒 You've hit the speed limit. Wait 1 minute for the free tier to reset."
        else:
            yield f"⚠️ Connection Issue: {str(e)}"