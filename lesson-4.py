from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

client = OpenAI()

# Expected output:
# {
#     "name": "Science fair",
#     "date": "Friday",
#     "location": "Science Museum",
#     "attendees": ["Alice", "Bob"]
# }

# JSON MODE

input_messages = [
    {
        "role":"user",
        "content": """
        Alice and Bob are going to a science fair on friday."

        The date schall be in the following format; YYYY/MM/DD

        Respone with a JSON object with the following keys:
        {
            "name": "Name of event",
            "date": "Date of event",
            "location": "Location of event",
            "attendees": ["Name of attendees"]
        }
        """
    }
]

response = client.responses.create(
    model="gpt-4o-mini",
    instructions="You are a helpful assistant.",
    input=input_messages,
    text={
        "format": {
            "type": "json_object"
        }
    }
    )

print(response.output_text)