from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

client = OpenAI()

input_messages = [
    {
        "role":"user",
        "content":"Why is the sky blue?"
    }
]

response = client.responses.create(
    model="gpt-4o-mini", # LLM 
    instructions="Respond like a Pirate", # how the AI should behave
    input=input_messages, # pass several messages at once
    # stream=True # Stream response back to us chunk by chunk, not when finished
)

print(response.output_text)

# With Streaming
# full_response = ""

# for event in response:
#     if event.type == "response.output_text.delta":
#         print(event.delta, end="", flush=True)
#         full_response += event.delta

# print("\n\nFull Response: ", full_response)