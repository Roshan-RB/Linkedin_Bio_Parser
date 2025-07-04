# app.py

import streamlit as st
from parser import parse_with_pydantic, parse_with_typed, parse_with_json, parse_with_prompt_only
import os

st.set_page_config(page_title="LinkedIn Bio Extractor", layout="centered")
st.title("🔎 LinkedIn Bio to Structured Profile")

# Example bios
examples = {
    "— Select Example —": "",
    
    "🧠 AI Researcher – Aisha Rahman": """Hi, I'm Aisha Rahman, a Data Scientist with 5 years of experience in machine learning and predictive analytics. I specialize in NLP and deep learning for fintech applications. Currently working at N26. I’m passionate about ethical AI, mentoring, and women in tech. Actively open to new roles in research-driven teams.""",
    
    "💼 Junior Developer – Arjun Mehta": """Recent Computer Science graduate from TU Berlin with internship experience in front-end development (React, TypeScript) at a Berlin startup. Eager to grow in full-stack engineering roles. Looking for junior developer or trainee opportunities in Europe.""",
    
    "🔄 Career Switcher – Maria Lopes": """I spent 10 years as a high school math teacher before retraining as a Data Analyst via a 12-month bootcamp. I now work with Excel, Power BI, and Python to build dashboards and reports. Currently working freelance, but open to full-time roles in edtech or government analytics.""",
    
    "🧪 Research-Oriented – Kevin Zhang": """PhD in Computer Vision from ETH Zurich, working on object tracking and multimodal learning. Currently a postdoc at MIT CSAIL. I collaborate with industry partners to apply vision models in robotics. Interested in research scientist roles at AI-first companies. Open to relocation.""",
    
    "🔍 Minimal Signals – Chris Baker": """Software developer. I like building cool things and occasionally writing open-source tools. Working on personal projects right now.""",
    
    "🚫 Incomplete – Samira Khan": """Based in Munich. Passionate about technology and creativity. Love learning new things. Let's connect!"""
}


# User choice
parse_mode = st.radio("🧬 Choose schema", ["TypedDict", "Pydantic", "JSON Schema","Prompt Only", "Compare All"], horizontal=True)

# 2. Load example
selected_example = st.selectbox("📋 Load Example Bio (optional)", list(examples.keys()))
default_bio = examples[selected_example] if selected_example in examples else ""
user_input = st.text_area("✍️ Enter or Edit LinkedIn Bio Below", value=default_bio, height=250, key="bio_text")

# Parse on click
if st.button("🧠 Extract Profile"):
    if user_input.strip() == "":
        st.warning("Please enter or load a LinkedIn bio to parse.")
    else:
        with st.spinner("Parsing..."):

            if parse_mode == "TypedDict":
                result, latency = parse_with_typed(user_input)
                st.subheader("📋 TypedDict Output")
                st.write("**👤 Name:**", result.get("name"))
                st.write("**💼 Occupation:**", result.get("occupation"))
                st.write("**📌 Specialization:**", result.get("specialization"))
                st.write("**🎯 Interests:**", ", ".join(result.get("interests", [])) if result.get("interests") else "-")
                st.write("**🚀 Open to Opportunities:**", result.get("open_to_opportunities").capitalize())

                with st.expander("🔍 View Raw Typed"):
                    st.json(result)

            elif parse_mode == "Pydantic":
                result, latency = parse_with_pydantic(user_input)
                st.subheader("📋 Pydantic Output")
                st.write("**👤 Name:**", result.name)
                st.write("**💼 Occupation:**", result.occupation)
                st.write("**📌 Specialization:**", result.specialization or "-")
                st.write("**🎯 Interests:**", ", ".join(result.interests or []))
                st.write("**🚀 Open to Opportunities:**", result.open_to_opportunities.capitalize())

                st.session_state["structured_output"] = result

                with st.expander("🔍 View Raw pydantic"):
                    st.json(result)

            elif parse_mode == "JSON Schema":
                result, latency = parse_with_json(user_input)
                st.subheader("📋 JSON Schema Output")
                st.write("**👤 Name:**", result.get("name"))
                st.write("**💼 Occupation:**", result.get("occupation"))
                st.write("**📌 Specialization:**", result.get("specialization", "-"))
                st.write("**🎯 Interests:**", ", ".join(result.get("interests", [])) if result.get("interests") else "-")
                st.write("**🚀 Open to Opportunities:**", result.get("open_to_opportunities").capitalize())

                with st.expander("🔍 View Raw JSON"):
                    st.json(result)

            elif parse_mode == "Prompt Only":
                result, latency = parse_with_prompt_only(user_input)
                st.subheader("📝 Raw Output without Structure")
                st.text(result)
                st.caption(f"⏱️ {latency:.2f} sec")

            elif parse_mode == "Compare All":
                with st.spinner("Parsing via all methods..."):
                    typed_result, t_time = parse_with_typed(user_input)
                    pydantic_result, p_time = parse_with_pydantic(user_input)
                    json_result, j_time = parse_with_json(user_input)

                st.subheader("🔎 Comparison Across Methods")

                col1, col2, col3 = st.columns(3)

                with col1:
                    st.markdown("### 🧱 TypedDict")
                    st.json(typed_result)
                    st.caption(f"⏱️ {t_time:.2f} sec")

                with col2:
                    st.markdown("### 🧬 Pydantic")
                    st.json(pydantic_result.model_dump())  # or .dict() if older Pydantic
                    st.caption(f"⏱️ {p_time:.2f} sec")
                with col3:
                    st.markdown("### 📦 JSON Schema")
                    st.json(json_result)
                    st.caption(f"⏱️ {j_time:.2f} sec")

            elif parse_mode == "Compare Structured vs Prompt":
                raw_result, raw_time = parse_with_prompt_only(user_input)
                structured_result, struct_time = parse_with_pydantic(user_input)

                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown("### 📝 Prompt-Based (Unstructured)")
                    st.text(raw_result)
                    st.caption(f"⏱️ {raw_time:.2f} sec")

                with col2:
                    st.markdown("### ✅ Structured (Pydantic)")
                    st.json(structured_result)
                    st.caption(f"⏱️ {struct_time:.2f} sec")