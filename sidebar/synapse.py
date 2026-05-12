import streamlit as st
from google import genai
import re
import time
import streamlit.components.v1 as components

def show_synapse():
    st.title("🧠 QSense Synapse")
    st.markdown("Generate a conceptual Mind Map for any topic.")
    
    topic = st.text_input("Enter Topic", placeholder="e.g., Laws of Motion")

    if st.button("Generate Map") and topic:
        api_key = st.secrets.get("GEMINI_API_KEY")
        
        
        if not api_key:
            st.error("Missing GEMINI_API_KEY in Streamlit Secrets!")
            return
        
        api_key = str(api_key[0] if isinstance(api_key, tuple) else api_key).strip() # Snippet to remove any API errors

        response = None

        try:
            client = genai.Client(
            api_key=api_key.strip(),
            http_options={'api_version': 'v1beta'}
        )
            prompt = f"You are QSense Synapse, an elite AI academic visualization engine designed for students. Create a highly structured, conceptually rich, and visually organized Mermaid.js graph TD mind map for the topic: {topic}. STRICT OUTPUT RULES: Output ONLY raw Mermaid.js code and nothing else. The response MUST start exactly with 'graph TD'. DO NOT use markdown. DO NOT use triple backticks. DO NOT add explanations, comments, headings, notes, examples, or extra text. Use ONLY simple alphanumeric node IDs such as A1, B2, C3, etc. Every node label MUST use square brackets only. DO NOT use parentheses (), curly braces, angle brackets, quotes, colons, semicolons, pipes, slashes, mathematical operators, arrows, emojis, or any other special symbols inside labels. Keep labels clean, compact, readable, and syntax-safe using plain text only. Structure the graph hierarchically with the main topic as the root node followed by major subtopics, formulas, laws, principles, identities, reactions, methods, applications, tricks, exceptions, and important JEE concepts. Maintain strong logical flow, balanced branching, conceptual grouping, and readable organization. Include only high-value academic content useful for revision and conceptual understanding. For Physics topics include laws, formulas, graphs, assumptions, and conceptual relations. For Chemistry topics include reactions, mechanisms, periodic trends, exceptions, and conceptual links. For Mathematics topics include identities, transformations, theorem relations, methods, and standard results. Ensure all Mermaid.js syntax is fully valid, directly renderable, professionally formatted, and completely free from syntax errors or disconnected nodes."        
            with st.spinner("AI is thinking..."):
                response = client.models.generate_content(
                    model='gemini-3.1-flash-lite',
                    contents=prompt
                )

        except Exception as e:
            if "429" in str(e):
                st.warning("Quota hit! Retrying in 10 seconds...")
                time.sleep(10)
                try:
                    # Fallback model for retries
                    response = client.models.generate_content(
                        model='gemini-1.5-flash',
                        contents=prompt
                    )
                except Exception as e2:
                    st.error(f"Retry failed: {e2}")
            else:
                st.error(f"API Error: {e}")

        if response and hasattr(response, 'text') and response.text:
            clean_mermaid = response.text.replace("```mermaid", "").replace("```", "").strip()
            
            st.success(f"{topic} Mind Map")

            html_code = f"""
                <div class="mermaid" style="background-color: white; padding: 20px; border-radius: 10px;">
                    {clean_mermaid}
                </div>
                <script type="module">
                    import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs';
                    mermaid.initialize({{ startOnLoad: true, theme: 'forest' }});
                </script>
                """
            components.html(html_code, height=600, scrolling=True)
            
        else:
            if not any(st.session_state.get("_errors", [])):
                st.warning("No data received. The AI might be throttled. Try again in 1 minute.")