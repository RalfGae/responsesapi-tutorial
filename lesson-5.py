from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

client = OpenAI()

input_messages = [
    {
        "role":"user",
        "content":"What is the current weather in London?"
    }
]

tools = [
    {
        "type": "web_search_preview"
    }
]

response = client.responses.create(
    model="gpt-4o-mini",
    input=input_messages,
    tools=tools
)

print(response.output_text)