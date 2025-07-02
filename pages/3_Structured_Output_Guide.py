import streamlit as st

st.set_page_config(page_title="Structured Output Guide", layout="centered")
st.title("📚 Structured Output Guide")

# Section 1: What is Structured Output?
st.header("🧾 What is Structured Output?")
st.markdown("""
Structured output is when a Language Model (LLM) returns information in a **well-defined format** (e.g., JSON, Python dict, schema-based object) instead of plain text.

This is especially useful when your app or workflow depends on predictable formats like:
- JSON APIs
- Data ingestion pipelines
- Frontend display or downstream ML tasks
""")

# Section 2: Why Do We Need Structured Output?
st.header("❓ Why Structured Output?")
st.markdown("""
While LLMs are good at generating human-like text, they are **not reliable** for freeform outputs when:
- You expect specific fields like `name`, `price`, `sentiment`
- You want to convert natural language into structured data (like a form or table)
- You need schema validation, default values, or error handling

Structured outputs ensure **consistency**, **validity**, and **easier post-processing**.
""")

# Section 3: Ways to Get Structured Output
st.header("🔧 Ways to Get Structured Output in LangChain")

with st.expander("🔹 TypedDict"):
    st.markdown("""
- Based on Python’s `typing.TypedDict`
- Simple to define
- Works well for small, static structures
- ✅ Fast
- ❌ No validation or default values
""")

with st.expander("🔹 Pydantic"):
    st.markdown("""
- Uses `pydantic.BaseModel`
- Supports data validation, defaults, and conversion
- ✅ Strong typing and schema enforcement
- ✅ Popular in FastAPI and data workflows
""")

with st.expander("🔹 JSON Schema"):
    st.markdown("""
- Define structure as a JSON-compatible dictionary
- Ideal for **cross-language** or API tools
- ✅ Compatible with web frontends, JSON APIs
- ✅ Works well for OpenAPI / tools interoperability
""")

# Section 4: LangChain usage
st.header("🔗 LangChain's `with_structured_output()`")

st.code("""
structured_model = model.with_structured_output(MySchema)
result = structured_model.invoke(text)
""", language="python")

st.markdown("""
LangChain automatically:
- Creates a prompt with output formatting instructions
- Parses the model's output into the defined schema
- Raises errors if output is malformed
""")

# Section 5: Real-World Applications
st.header("🌍 Real-World Applications")
st.markdown("""
- Extracting structured data from user reviews
- Parsing resumes or LinkedIn bios into profile fields
- Creating structured form-fillers from emails
- Auto-generating SQL/JSON from natural language
""")

# Final Tip
st.success("💡 Tip: Always validate the model output before trusting it in production!")
