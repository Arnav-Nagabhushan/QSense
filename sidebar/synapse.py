import streamlit as st
from google import genai
import re
import time

def show_synapse():
    st.title("🧠 QSense Synapse")
    st.markdown("Generate a conceptual Mind Map for any JEE topic.")
    
    topic = st.text_input("Enter Topic", placeholder="e.g., Laws of Motion")

    if st.button("Generate Map") and topic:
        api_key = st.secrets.get("GEMINI_API_KEY")
        
        if not api_key:
            st.error("Missing GEMINI_API_KEY in Streamlit Secrets!")
            return

        try:
            client = genai.Client(api_key=api_key.strip())
            prompt = f"You are QSense Synapse, an elite AI academic visualization engine designed for students. Create a highly structured, conceptually rich, and visually organized Mermaid.js graph TD mind map for the topic: {topic}. STRICT OUTPUT RULES: Output ONLY raw Mermaid.js code and nothing else. The response MUST start exactly with 'graph TD'. DO NOT use markdown. DO NOT use triple backticks. DO NOT add explanations, comments, headings, notes, examples, or extra text. Use ONLY simple alphanumeric node IDs such as A1, B2, C3, etc. Every node label MUST use square brackets only. DO NOT use parentheses (), curly braces, angle brackets, quotes, colons, semicolons, pipes, slashes, mathematical operators, arrows, emojis, or any other special symbols inside labels. Keep labels clean, compact, readable, and syntax-safe using plain text only. Structure the graph hierarchically with the main topic as the root node followed by major subtopics, formulas, laws, principles, identities, reactions, methods, applications, tricks, exceptions, and important JEE concepts. Maintain strong logical flow, balanced branching, conceptual grouping, and readable organization. Include only high-value academic content useful for revision and conceptual understanding. For Physics topics include laws, formulas, graphs, assumptions, and conceptual relations. For Chemistry topics include reactions, mechanisms, periodic trends, exceptions, and conceptual links. For Mathematics topics include identities, transformations, theorem relations, methods, and standard results. Ensure all Mermaid.js syntax is fully valid, directly renderable, professionally formatted, and completely free from syntax errors or disconnected nodes."        
            with st.spinner("Brain is thinking... (waiting for quota if needed)"):
                response = client.models.generate_content(
                    model='gemini-1.5-flash',
                    contents=prompt
                )
        except Exception as e:
            if "429" in str(e):
                st.warning("Quota hit! Auto-retrying in 15 seconds... don't click anything!")
                time.sleep(15)
                response = client.models.generate_content(
                    model='gemini-2.0-flash',
                    contents=prompt
                )

                # response = client.models.generate_content(model='gemini-1.5-flash', contents=prompt)


            else:
                st.error(f"Error: {e}")
                clean_mermaid = response.text.replace("```mermaid", "").replace("```", "").strip()
                
                st.success(f"Synapse Map: {topic}")

                import streamlit.components.v1 as components
                html_code = f"""
                <div class="mermaid" style="background-color: white; padding: 20px; border-radius: 10px;">
                    {clean_mermaid}
                </div>
                <script type="module">
                    import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs';
                    mermaid.initialize({{ startOnLoad: true, theme: 'forest' }});
                </script>
                """
                components.html(html_code, height=800, scrolling=True)

        except Exception as e:
            st.error(f"Synapse Error: {e}")