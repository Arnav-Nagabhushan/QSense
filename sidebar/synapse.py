import streamlit as st
from google import genai
client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
import streamlit.components.v1 as components
import re

def clean_for_mermaid(text):
    text = text.replace("```mermaid", "").replace("```", "").strip()
    text = re.sub(r'([a-zA-Z0-9])\((.*?)\)', r'\1_\2', text)
    return text

def show_synapse():
    st.title("✨ QSense Synapse")
    st.subheader("Generate a conceptual Mind Map for any topic.")

    topic = st.text_input("Enter Topic", placeholder = "(e.g., Organic Chemistry, Waves, Matrices)")

    if st.button("Generate Map"):
        if not topic:
            st.warning("Please enter a topic.")
            return

        api_key = st.secrets.get("GEMINI_API_KEY")
        genai.configure(api_key=api_key.strip())

        model = genai.GenerativeModel('gemini-3.1-flash-lite')

        prompt = f"You are QSense Synapse, an elite AI academic visualization engine designed for students. Create a highly structured, conceptually rich, and visually organized Mermaid.js graph TD mind map for the topic: {topic}. STRICT OUTPUT RULES: Output ONLY raw Mermaid.js code and nothing else. The response MUST start exactly with 'graph TD'. DO NOT use markdown. DO NOT use triple backticks. DO NOT add explanations, comments, headings, notes, examples, or extra text. Use ONLY simple alphanumeric node IDs such as A1, B2, C3, etc. Every node label MUST use square brackets only. DO NOT use parentheses (), curly braces, angle brackets, quotes, colons, semicolons, pipes, slashes, mathematical operators, arrows, emojis, or any other special symbols inside labels. Keep labels clean, compact, readable, and syntax-safe using plain text only. Structure the graph hierarchically with the main topic as the root node followed by major subtopics, formulas, laws, principles, identities, reactions, methods, applications, tricks, exceptions, and important JEE concepts. Maintain strong logical flow, balanced branching, conceptual grouping, and readable organization. Include only high-value academic content useful for revision and conceptual understanding. For Physics topics include laws, formulas, graphs, assumptions, and conceptual relations. For Chemistry topics include reactions, mechanisms, periodic trends, exceptions, and conceptual links. For Mathematics topics include identities, transformations, theorem relations, methods, and standard results. Ensure all Mermaid.js syntax is fully valid, directly renderable, professionally formatted, and completely free from syntax errors or disconnected nodes."        
        try:
            with st.spinner("Generating a Conceptual Mind Map..."):
                response = model.generate_content(prompt)
                clean_mermaid = response.text.replace("```mermaid", "").replace("```", "").strip()

                st.success(f"Map for {topic} is ready!")
                st.success(f"Synapse Map: {topic}")

                html_content = f"""
                <html>
                    <body>
                        <pre class="mermaid">{clean_mermaid}</pre>
                        <script type="module">
                            import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs';
                            mermaid.initialize({{ startOnLoad: true }});
                        </script>
                    </body>
                </html>
                """
                st.logo("🧠", icon_image=None) 
                st.iframe(data=html_content, height=600)

                st.info("💡 Tip: Copy this map into your notes to visualize the chapter flow and easy understanding!")

        except Exception as e:
            st.error(f"Synapse Error: {str(e)}")