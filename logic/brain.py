import google.generativeai as genai
import streamlit as st

def get_ai_recommendations(weak_topics, avg_score):
    # Setup client
    client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
    
    # 2026 PRO TIP: Flash-Lite is the most stable free model
    model_id = "gemini-2.5-flash-lite"
    
    prompt = f"You are an elite academic mentor and performance-improvement tutor helping a student strengthen weak areas and improve exam performance efficiently. The student's current average score is {avg_score}%. The topics they currently struggle with are: {', '.join(weak_topics)}. Analyze the student's weak areas carefully and generate exactly 3 highly practical, personalized, and actionable study tips focused specifically on improving understanding, accuracy, retention, and problem-solving ability in these topics. The tips must feel intelligent, realistic, exam-oriented, and optimized for a high school student preparing for competitive exams like JEE Main and Advanced. Avoid generic advice such as 'study harder', 'practice more', 'revise daily', or anything vague and repetitive. Every tip must target a real academic weakness students usually face such as conceptual gaps, calculation mistakes, weak visualization, poor question analysis, formula confusion, silly mistakes, lack of pattern recognition, weak application skills, panic during difficult problems, poor time management, or inability to connect concepts. Each tip should clearly explain WHAT the student should do, HOW they should do it, and WHY it helps. The advice should encourage active learning instead of passive reading. Include methods such as mistake analysis, pattern spotting, concept linking, timed solving, reverse thinking, visualization, memory tricks, question decomposition, error logging, topic prioritization, or smart revision techniques wherever relevant. Ensure the tips are short, crisp, and concise, with each tip limited to around 1–2 lines maximum while still being meaningful and information-dense. The tips should sound motivating, practical, and easy to apply immediately. Make all 3 tips clearly different from each other and avoid repeating the same style of advice. Keep the tone supportive, smart, focused, and student-friendly. Output ONLY the 3 numbered tips and nothing else."
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