import streamlit as st
import pandas as pd

st.title("📌 When to Use What?")
st.markdown("A comparison of `TypedDict`, `Pydantic`, and `JSON Schema` for structured output:")

# Define table data
data = {
    "Feature": [
        "Basic structure",
        "Type enforcement",
        "Data validation",
        "Default values",
        "Automatic conversion",
        "Cross-language compatibility"
    ],
    "TypedDict ✅": ["✅", "✅", "❌", "❌", "❌", "❌"],
    "Pydantic 🧬": ["✅", "✅", "✅", "✅", "✅", "❌"],
    "JSON Schema 🌐": ["✅", "✅", "✅", "❌", "✅", "✅"]
}

df = pd.DataFrame(data)
st.table(df)
