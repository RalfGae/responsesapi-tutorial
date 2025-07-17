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
tools = []

# OpenAI client initialization
client = OpenAI()

response = client.responses.create(
    model="gpt-4o-mini",
    input=input_messages,
    tools=tools
)

print(response.output_text)

# With Streaming (optional)
# full_response = ""
# for event in response:
#     if event.type == "response.output_text.delta":
#         print(event.delta, end="", flush=True)
#         full_response += event.delta
# print("\n\nFull Response: ", full_response)
