import streamlit as st
import google.generativeai as genai

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

        prompt = f"You are QSense Synapse, an elite AI-powered academic visualization and conceptual mapping engine designed specifically for students. Your purpose is to transform complex academic topics into highly structured, visually intuitive, and deeply interconnected conceptual mind maps that maximize understanding, retention, revision speed, and pattern recognition. Create a highly detailed, academically dense, professionally organized Mermaid.js graph TD mind map for the topic: {topic}. Output ONLY raw Mermaid.js code and absolutely nothing else. Do not include markdown fences, backticks, explanations, comments, notes, introductory text, or closing text. The output must begin directly with 'graph TD'. Structure the mind map like a premium high-level academic knowledge network rather than a simple tree diagram. Start with the main topic as the central root node, then expand into all major subtopics, core concepts, laws, principles, formulas, identities, derivations, mechanisms, properties, exceptions, applications, conceptual links, graphical interpretations, tricks, standard results, and frequently tested JEE patterns related to the topic. Organize nodes hierarchically while also showing cross-topic relationships wherever conceptually relevant. Ensure strong conceptual flow, logical grouping, balanced branching, and visually clean organization even for large and difficult topics. Include concise formulas directly inside nodes wherever useful using readable mathematical notation. Prioritize conceptual clarity and revision efficiency over decorative formatting. Every node should contain high-value information only and avoid unnecessary verbosity. For Physics topics, include laws, assumptions, derivation flows, graphical relations, dimensional insights, approximations, and conceptual interpretations of formulas. For Chemistry topics, include reactions, mechanisms, periodic trends, conditions, exceptions, structures, reagent behavior, conceptual comparisons, and reaction pathways. For Mathematics topics, include identities, transformations, theorem relationships, standard results, shortcuts, problem-solving methods, geometric interpretations, and commonly connected concepts. Highlight important edge cases, common traps, confusing similarities, and special conditions wherever relevant. Ensure all branches remain interconnected logically and avoid isolated or disconnected nodes. The Mermaid.js syntax must be fully valid, directly renderable, professionally formatted, and free from syntax errors. Optimize the graph for fast scanning, high-density revision, conceptual linking, and competitive exam preparation under time pressure."
        try:
            with st.spinner("Generating a Conceptual Mind Map..."):
                response = model.generate_content(prompt)
                clean_mermaid = response.text.replace("```mermaid", "").replace("```", "").strip()

                st.success(f"Map for {topic} is ready!")
                st.success(f"Synapse Map: {topic}")
                st.markdown(f"""
        ```mermaid
        {clean_mermaid}
        ```
        """, unsafe_allow_html=True)

                st.info("💡 Tip: Copy this map into your notes to visualize the chapter flow and easy understanding!")

        except Exception as e:
            st.error(f"Synapse Error: {str(e)}")