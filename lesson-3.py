from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

client = OpenAI()

def chat_loop():

    history = []
      
    while True:
        # Get user input
        user_input = input("You: ")

        if user_input.lower() in ["exit", "bye", "quit"]:
            print("Goodbye!")
            break
        
        history.append({
            "role": "user",
            "content": user_input
        })

        response = client.responses.create(
            model="gpt-4o-mini",
            input=history,
        )

        history.append({
            "role": "assistant",
            "content": response.output_text,
        })

        print("Bot: ", response.output_text)

if __name__ == "__main__":
    chat_loop()