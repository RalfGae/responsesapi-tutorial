from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

client = OpenAI()

def chat_loop():
    current_response_id = None

    while True:
        # Get user input
        user_input = input("You: ")

        if user_input.lower() in ["exit", "bye", "quit"]:
            print("Goodbye!")
            break

        response = client.responses.create(
            model="gpt-4o-mini",
            input=user_input,
            previous_response_id=current_response_id
        )

        current_response_id = response.id

        # Print the response
        print("Bot: ", response.output_text)

if __name__ == "__main__":
    chat_loop()