import streamlit as st
import os


st.set_page_config(page_title="Structured Output Explorer", layout="centered")

# 🎨 Sidebar Layout
st.sidebar.title("🚀 Structured Output App")
st.sidebar.markdown("Navigate through pages to learn and experiment with structured outputs.")

# 🌐 Optional: API key input
openai_api_key = st.sidebar.text_input("🔑 Enter OpenAI API Key", type="password")
if openai_api_key:
    os.environ["OPENAI_API_KEY"] = openai_api_key
    st.sidebar.success("API key set!")

st.title("📊 Structured Output Explorer")
st.markdown("""
Welcome to the **Structured Output Explorer**!  
This educational tool helps you understand how to extract structured data from unstructured text using **LangChain** and **LLMs**.

### 🧠 What You’ll Learn:
- What is structured output?
- Why it's important in LLM workflows
- How to extract data using:
    - ✅ `TypedDict`
    - 🧬 `Pydantic`
    - 📦 `JSON Schema`
- When to use each and how they differ

👉 Use the sidebar to explore!
""")
