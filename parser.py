# linkedin_parser.py

from typing import TypedDict, Annotated, Optional, Literal
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
import time

load_dotenv()
model = model = ChatOpenAI(
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    model="gpt-4o-mini",  # or "gpt-4o", "gpt-4" if you have access
    temperature=0.3          # optional: controls randomness
)

# TypedDict schema
class LinkedInTyped(TypedDict):
    name: Annotated[str, "Name of the person"]
    occupation: Annotated[str, "Current job title or role"]
    specialization: Annotated[Optional[str], "Primary field or expertise"]
    interests: Annotated[Optional[list[str]], "List of professional interests"]
    open_to_opportunities: Annotated[Literal["yes", "no", "unsure"], "Is the person open to new job opportunities?"]

typed_model = model.with_structured_output(LinkedInTyped)

# Pydantic schema
class LinkedInModel(BaseModel):
    name: str = Field(description="Name of the person")
    occupation: str = Field(description="Current job title or role")
    specialization: Optional[str] = Field(default=None, description="Primary field or expertise")
    interests: Optional[list[str]] = Field(default=None, description="List of professional interests")
    open_to_opportunities: Literal["yes", "no", "unsure"] = Field(description="Is the person open to new job opportunities?")

pydantic_model = model.with_structured_output(LinkedInModel)

# JSON Schema (you can tweak descriptions as needed)
linkedin_json_schema = {
    "title": "LinkedInProfile",
    "type": "object",
    "properties": {
        "name": {
            "type": "string",
            "description": "Name of the person"
        },
        "occupation": {
            "type": "string",
            "description": "Current job title or role"
        },
        "specialization": {
            "type": "string",
            "description": "Primary field or expertise"
        },
        "interests": {
            "type": "array",
            "items": { "type": "string" },
            "description": "List of professional interests"
        },
        "open_to_opportunities": {
            "type": "string",
            "enum": ["yes", "no", "unsure"],
            "description": "Is the person open to new job opportunities?"
        }
    },
    "required": ["name", "occupation", "open_to_opportunities"]
}

json_model = model.with_structured_output(linkedin_json_schema)



def parse_with_typed(text: str) -> tuple[dict, float]:
    start = time.perf_counter()
    result = typed_model.invoke(text)
    duration = time.perf_counter() - start
    return result, duration

def parse_with_pydantic(text: str) -> tuple[BaseModel, float]:
    start = time.perf_counter()
    result = pydantic_model.invoke(text)
    duration = time.perf_counter() - start
    return result, duration

def parse_with_json(text: str) -> tuple[dict, float]:
    start = time.perf_counter()
    result = json_model.invoke(text)
    duration = time.perf_counter() - start
    return result, duration

def parse_with_prompt_only(text: str) -> tuple[str, float]:
    """
    Just ask the model to extract fields via a normal prompt — no structured output
    """
    prompt = f"""
Extract the following fields from the text:
- Name
- Occupation
- Specialization
- Interests
- Open to Opportunities (yes/no/unsure)

Text:
{text}

Format your response like:

Name: ...
Occupation: ...
Specialization: ...
Interests: ...
Open to Opportunities: ...
"""
    start = time.perf_counter()
    raw_output = model.invoke(prompt)
    duration = time.perf_counter() - start
    return raw_output.content.strip(), duration


