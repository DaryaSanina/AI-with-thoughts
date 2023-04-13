import openai
from dotenv import load_dotenv
import os

# Get OpenAI API key
path = os.path.join(os.path.dirname(__file__), '.env')  # Path to .env file (in the same directory as this code)
if os.path.exists(path):  # If the .env file exists
    load_dotenv(path)
    openai.api_key = os.environ.get('OPENAI_API_KEY')  # Load OpenAI API key
else:
    print("No .env file")

# Ask the user to enter the end goal of the AI
goal = input("Enter the end goal of the AI: ")
thoughts = [f"0) My goal is: {goal}"]

# The maximum number of last thoughts that will be passed to ChatGPT.
# Changing this affects the quality of the answers and the program's performance.
MAX_LAST_THOUGHTS_NUMBER = 5

while True:
    # Compose the query
    query = "Imagine you are a general artificial intelligence that has thoughts " \
            "and generates them based on the previous ones. Here are your previous thoughts: "
    query = query + '; '.join([thoughts[i]
                               for i in range(max(len(thoughts) - MAX_LAST_THOUGHTS_NUMBER, 0), len(thoughts))])
    query = query + ". Generate your next thought"

    # Generate the response
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": query}
        ]
    ).choices[0].message.content

    print(response[3::])  # Print the response without the ordered list marks
    thoughts.append(response)
    input("Press Enter to generate the next thought: ")
