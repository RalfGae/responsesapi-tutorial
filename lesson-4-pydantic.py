from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

from pydantic import BaseModel, ConfigDict
from typing import List

# Create the Pydantic class
class Event(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str
    date: str
    location: str
    attendees: List[str]

schema = Event.model_json_schema()

print(schema)

# Initial messages
input_messages = [
    {
        "role":"user",
        "content": "Alice and Bob are going to a science fair in New York on friday."
    }
]

client = OpenAI()

response = client.responses.create(
    model="gpt-4o-mini",
    instructions="Extract the event information.",
    input=input_messages,
    text={
        "format": {
            "type": "json_schema",
            "name": "calendar_event",
            "schema": schema, 
            "strict": True
        }
    }
)

print(response.output_text)