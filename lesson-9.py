from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

import json
from pydantic import BaseModel, ConfigDict
from duckduckgo_search import DDGS

# Tool function: Reliable image search using duckduckgo-search

def search_image(query: str):
    with DDGS() as ddgs:
        results = list(ddgs.images(query, max_results=1))
        if results:
            return f"Found image for '{query}': {results[0]['image']}"
        else:
            return f"No image found for '{query}'."

class SearchImageParams(BaseModel):
    model_config = ConfigDict(extra="forbid")
    query: str

search_image_schema = SearchImageParams.model_json_schema()

tools = [
    {
        "type": "function",
        "name": "search_image",
        "description": "Search for an image by query string.",
        "parameters": search_image_schema,
        "strict": True
    }
]

input_messages = [
    {
        "role": "user",
        "content": "Find an image of a frog."
    }
]


client = OpenAI()

# Single image search request
image_url = None
response = client.responses.create(
    model="gpt-4o-mini",
    input=input_messages,
    tools=tools
)

response_output = response.output[0]
response_type = response_output.type

if response_type == "message":
    print(response.output_text)
if response_type == "message":
    print(response.output_text)
elif response_type == "function_call":
    function_name = response_output.name
    arguments = response_output.arguments
    args = json.loads(arguments)
    print(f"Function: {function_name} with args: {args}")
    tool_result = ""
    if function_name == "search_image":
        tool_result = search_image(args["query"])
        if tool_result.startswith("Found image for"):
            image_url = tool_result.split(": ", 1)[-1]
            print(f"Image URL: {image_url}")
            # Immediately verify the image using LLM
            verify_prompt = f"Based on the image, how likely is it that this is a photo of {args['query']}? Respond with a short explanation and a likelihood estimate (e.g., 'very likely', 'likely', 'uncertain', 'unlikely')."
            print("Verification prompt:", verify_prompt)
            verify_messages = [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "input_text",
                            "text": verify_prompt
                        },
                        {
                            "type": "input_image",
                            "image_url": image_url
                        }
                    ]
                }
            ]
            verify_response = client.responses.create(
                model="gpt-4o-mini",
                input=verify_messages
            )
            print("Verification result:", verify_response.output_text)
    input_messages.append(response_output)
    input_messages.append({
        "type": "function_call_output",
        "call_id": response_output.call_id,
        "output": str(tool_result)
    })
