import os
import openai

def call_autogen(prompt):
    try:
        response = openai.Completion.create(
            model="text-davinci-003",  # Specify the model
            prompt=prompt,
            temperature=0.7,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Set the API key using an environment variable for security
openai.api_key = os.getenv('OPENAI_API_KEY')

# Example usage
prompt = "Your prompt here"
generated_code = call_autogen(prompt)
print(generated_code)
