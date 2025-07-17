from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

# Input messages
input_messages = [
    {
        "role": "user",
        "content": "Find an Image of Emma Watson."
    }
]

# Tools
tools = [{
    "type": "computer_use_preview",
    "display_width": 1920,
    "display_height": 1200,
    "environment": "browser"
}]

# OpenAI client initialization
client = OpenAI()

response = client.responses.create(
    model="computer-use-preview",
    input=input_messages,
    tools=tools,
    reasoning={
        "generate_summary": "concise",
    },
    truncation="auto"
)

print(response.output_text)
