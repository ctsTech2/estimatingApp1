import os
from openai import OpenAI

def call_autogen(prompt):
    # Instantiate the OpenAI client
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

    try:
        # Make a completion request
        response = client.completions.create(
            model="text-davinci-003",  # Specify the model
            prompt=prompt,
            temperature=0.7,
            max_tokens=150
        )

        # Return the text of the first choice
        return response.choices[0].text.strip()
    except Exception as e:
        # Handle any exceptions that occur
        return f"An error occurred: {str(e)}"

# Example usage
prompt = "Write a Flask route in Python with an HTML form for inputting an item's name and quantity. Include fields for 'item name' and 'quantity' and a submit button. Also, provide a Flask route to handle POST requests and print the submitted values."
generated_code = call_autogen(prompt)
print(generated_code)
