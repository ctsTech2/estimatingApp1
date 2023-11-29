import os
from openai import OpenAI

# Create OpenAI client with API key from environment variable
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))


def call_autogen(prompt):
    try:
        response = client.completions.create(
            engine="davinci",  # You can choose a different engine if needed
            prompt=prompt,
            temperature=0.7,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Example usage
prompt = "Write a Flask route in Python with an HTML form for inputting an item's name and quantity. Include fields for 'item name' and 'quantity' and a submit button. Also, provide a Flask route to handle POST requests and print the submitted values."
generated_code = call_autogen(prompt)
print(generated_code)
