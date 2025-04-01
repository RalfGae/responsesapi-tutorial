from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

client = OpenAI()

imput_messages=[
    {
        "role":"user",
        "content":"Hello there"
    }
]

response = client.responses.create(
    model="gpt-4o-mini",
    input=imput_messages
)

print(response.output_text)