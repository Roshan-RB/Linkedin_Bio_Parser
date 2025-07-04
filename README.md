# 🧠 Structured Output Explorer with LangChain

This interactive Streamlit app helps you **understand, test, and compare** different methods of extracting structured data from unstructured text using LangChain and LLMs.

> ⚙️ Built as an educational playground — not for production use.

---

## 🚀 Features

* ✅ Try out **TypedDict**, **Pydantic**, and **JSON Schema**-based parsing
* 📋 Compare structured outputs **side by side**
* ⏱️ See **latency per method** to understand performance
* 💾 Load diverse LinkedIn bio examples (minimal, research, junior, vague, etc.)
* 📝 Try a “Prompt-only” (no schema) approach to see its pitfalls
* 📚 Learn from the integrated guide: *When to use what & why structured output matters*

---

## 📦 Tech Stack

* [Streamlit](https://streamlit.io/)
* [LangChain](https://www.langchain.com/)
* [OpenAI GPT-4o / gpt-3.5](https://platform.openai.com/)
* `TypedDict`, `Pydantic`, and JSON Schema

---

## 🧪 Usage

```bash
# Install dependencies
pip install -r requirements.txt

# Set your API key
export OPENAI_API_KEY=your-key-here

# Run the app
streamlit run app.py
```

Alternatively, enter your key in the sidebar input at runtime.

---

## 📂 Project Structure

```
.
├── app.py                          # Home / Intro page
├── pages/
│   ├── 1_Try_it_Out.py             # Playground to test parsing
│   ├── 2_When_to_Use_What.py       # Comparison table
│   └── 3_Structured_Output_Guide.py# Conceptual guide
├── parser.py                       # All parsing logic (TypedDict, Pydantic, etc.)
├── requirements.txt
└── .gitignore
```

---

## 📚 Learn More

* [LangChain: `with_structured_output()`](https://python.langchain.com/docs/modules/model_io/output_parsers/)
* [Pydantic Docs](https://docs.pydantic.dev/)
* [JSON Schema](https://json-schema.org/)

---

## ❤️ Contributions

This is an educational app — feel free to fork, learn, or improve!

---

## 📸 Screenshots 

![image](https://github.com/user-attachments/assets/fa150d50-4183-45dc-87e9-b0fa79e17fda)

![image](https://github.com/user-attachments/assets/b5eabd0a-60a2-494a-ba38-47193acda7de)

![image](https://github.com/user-attachments/assets/65e61b9c-3580-4267-9bd7-0d28d56918e9)

![image](https://github.com/user-attachments/assets/404c5982-4305-475e-8b9c-dd8cc208a390)

![image](https://github.com/user-attachments/assets/9fcee9e1-35e9-443d-bf77-66df501190ee)



---

## 🌐 Credits

This app was heavily inspired by the fantastic LangChain tutorial by **CampusX**.

🎥 Watch the original tutorial here: [LangChain Output Parsers Tutorial](https://www.youtube.com/watch?v=y5EmRr1O1h4&list=PLKnIA16_RmvaTbihpo4MtzVm4XOQa0ER0&index=7&t=2511s)

Channel: [CampusX YouTube](https://www.youtube.com/@CampusX/videos)

---

## 🔮 Next Steps (Planned)

* [ ] Accept direct LinkedIn profile URLs and auto-extract bio
* [ ] Language-aware parsing for multilingual profiles
* [ ] Generate structured resume summaries in PDF/JSON
* [ ] Add LLM output validation and hallucination warnings
* [ ] Provide public API endpoint for LinkedIn bio parsing
