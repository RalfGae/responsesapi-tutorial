from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

client = OpenAI()

input_messages = [
    {
        "role":"user",
        "content":"What is the current weather near me?"
    }
]

tools = [
    {
        "type": "web_search_preview",
        "user_location": {
            "type": "approximate",
            "country": "GB",
            "city": "London",
            "region": "London"
        }
    }
]

response = client.responses.create(
    model="gpt-4o-mini",
    instructions="When looking up real time data using web search, do not ask for the user's location. It will be provided by the web search tool itself.",
    input=input_messages,
    tools=tools
)

print(response.output_text)