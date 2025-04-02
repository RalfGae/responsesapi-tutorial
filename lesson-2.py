from openai import OpenAI
import base64

from dotenv import load_dotenv
load_dotenv()

def encode_image(image_path):
    with open(image_path, 'rb') as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

base64_image1 = encode_image("./image1.png")
base64_image2 = encode_image("./image2.png")

client = OpenAI()

imput_messages=[
    {
        "role":"user",
        "content": [
            {
                "type": "input_text",
                "text": "Please describe the image"
            },
            {
                "type": "input_image",
                "image_url": f"data:image/jpeg;base64,{base64_image1}"
            },
            {
                "type": "input_image",
                "image_url": f"data:image/jpeg;base64,{base64_image2}"
            },
            {
                "type": "input_image",
                "image_url": "https://upload.wikimedia.org/wikipedia/en/f/f3/Dilbert-20050910.png"
            }
        ]
    }
]

response = client.responses.create(
    model="gpt-4o-mini",
    input=imput_messages
)

print(response.output_text)