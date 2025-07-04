# pages/generate_bio.py

import os
import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

# Load environment variables
load_dotenv()

# Define the Pydantic schema for the generated output
class GeneratedBio(BaseModel):
    bio: str = Field(description="Enhanced LinkedIn bio")

# Streamlit UI
st.title("🔁 Generate Improved LinkedIn Bio")

# Step 1: Check for extracted attributes
if "structured_output" not in st.session_state:
    st.warning("⚠️ No extracted attributes found. Please visit the 'Try it out' page first. \n This works with only Pydantic outputs! \n Extract outputs with Pydantic first and get back here :) ")
else:
    attributes = st.session_state["structured_output"]

    # Step 1: Tone selection
    tone = st.selectbox("🎨 Select Tone", ["professional", "friendly", "confident", "enthusiastic"])

    # Safely convert to dict no matter the type (Pydantic or dict)
    if hasattr(st.session_state["structured_output"], "model_dump"):
        attributes = st.session_state["structured_output"].model_dump()
    else:
        attributes = dict(st.session_state["structured_output"])

    # Step 2: Preprocess input
    input_data = {
        "name": attributes.get("name", ""),
        "occupation": attributes.get("occupation", ""),
        "specialization": attributes.get("specialization", "N/A"),
        "interests": ", ".join(attributes.get("interests", [])),
        "open_to_opportunities": attributes.get("open_to_opportunities", "unknown"),
        "tone": tone
    }


    # Step 3: Display input
    with st.expander("View Extracted attributes from original Linkedin bio"):
        st.subheader("📦 Extracted Attributes")
        st.json(attributes)

    # Step 4: Setup generation chain
    model = ChatOpenAI(
        openai_api_key=os.getenv("OPENAI_API_KEY"),
        model="gpt-4o-mini",  # or gpt-4o-mini / gpt-4
        temperature=0.3
    )

    parser = PydanticOutputParser(pydantic_object=GeneratedBio)

    prompt = PromptTemplate(
        input_variables=["name", "occupation", "specialization", "interests", "open_to_opportunities", "tone"],
        partial_variables={"format_instruction": parser.get_format_instructions()},
        template=(
            "Write a {tone} LinkedIn bio using the following information:\n\n"
            "Name: {name}\n"
            "Occupation: {occupation}\n"
            "Specialization: {specialization}\n"
            "Interests: {interests}\n"
            "Open to Opportunities: {open_to_opportunities}\n\n"
            "{format_instruction}"
        )
    )

    chain = prompt | model | parser

    # Step 5: Trigger generation
    if st.button("✨ Generate Bio"):
        with st.spinner("Crafting your LinkedIn bio..."):
            try:
                result = chain.invoke(input_data)
                st.subheader("📝 Generated LinkedIn Bio")
                st.success(result.bio)
            except Exception as e:
                st.error(f"❌ Error: {e}")
