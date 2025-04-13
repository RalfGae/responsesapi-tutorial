from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

client = OpenAI()

input_messages = [
    {
        "role":"user",
        "content":"Hey!"
    }
]

response = client.responses.create(
    model="gpt-4o-mini",
    instructions="RYou are a helpful assistant.",
    input=input_messages, # pass several messages at once
)

print(response.output_text)