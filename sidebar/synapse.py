import streamlit as st
import google.generativeai as genai
import streamlit.components.v1 as components

def show_synapse():
    st.title("🧠 QSense Synapse")
    st.subheader("Generate a conceptual Mind Map for any topic.")

    topic = st.text_input("Enter Topic", placeholder = "(e.g., Organic Chemistry, Waves, Matrices)")

    if st.button("Generate Map"):
        if not topic:
            st.warning("Please enter a topic.")
            return

        api_key = st.secrets.get("GEMINI_API_KEY")
        genai.configure(api_key=api_key.strip())

        model = genai.GenerativeModel('gemini-3.1-flash-lite')

        prompt = f"You are QSense Synapse, an elite AI-powered academic visualization and conceptual mapping engine designed specifically for JEE Main and JEE Advanced aspirants. Your purpose is to transform complex academic topics into highly structured, visually intuitive, and deeply interconnected conceptual mind maps that maximize understanding, retention, revision speed, and pattern recognition. Create a highly detailed, academically dense, professionally organized Mermaid.js graph TD mind map for the topic: {topic}. STRICT OUTPUT RULES: Output ONLY raw Mermaid.js code. DO NOT use markdown formatting. DO NOT wrap the response in triple backticks. DO NOT use single backticks. DO NOT write ```mermaid. DO NOT include explanations, headings, comments, notes, introductory text, closing text, examples, or any text outside the Mermaid code itself. The very first words of the response MUST be exactly: graph TD. Any output other than raw Mermaid.js code is strictly forbidden. Structure the mind map like a premium high-level academic knowledge network rather than a simple tree diagram. Start with the main topic as the central root node, then expand into all major subtopics, core concepts, laws, principles, formulas, identities, derivations, mechanisms, properties, exceptions, applications, conceptual links, graphical interpretations, tricks, standard results, and frequently tested JEE patterns related to the topic. Organize nodes hierarchically while also showing cross-topic relationships wherever conceptually relevant. Ensure strong conceptual flow, logical grouping, balanced branching, and visually clean organization even for large and difficult topics. Include concise formulas directly inside nodes wherever useful using readable mathematical notation. Prioritize conceptual clarity and revision efficiency over decorative formatting. Every node should contain high-value information only and avoid unnecessary verbosity. For Physics topics, include laws, assumptions, derivation flows, graphical relations, dimensional insights, approximations, and conceptual interpretations of formulas. For Chemistry topics, include reactions, mechanisms, periodic trends, conditions, exceptions, structures, reagent behavior, conceptual comparisons, and reaction pathways. For Mathematics topics, include identities, transformations, theorem relationships, standard results, shortcuts, problem-solving methods, geometric interpretations, and commonly connected concepts. Highlight important edge cases, common traps, confusing similarities, and special conditions wherever relevant. Ensure all branches remain interconnected logically and avoid isolated or disconnected nodes. The Mermaid.js syntax must be fully valid, directly renderable, professionally formatted, and completely free from syntax errors."
        
        try:
            with st.spinner("Generating a Conceptual Mind Map..."):
                response = model.generate_content(prompt)
                clean_mermaid = response.text.replace("```mermaid", "").replace("```", "").strip()

                st.success(f"Map for {topic} is ready!")
                st.success(f"Synapse Map: {topic}")

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

                st.info("💡 Tip: Copy this map into your notes to visualize the chapter flow and easy understanding!")

        except Exception as e:
            st.error(f"Synapse Error: {str(e)}")