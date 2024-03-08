import os
import openai

api_key = os.environ.get('OPENAI_API_KEY')

# Check if the API key is available
if api_key:
    # Set the API key explicitly
    openai.api_key = api_key
else:
    print("OpenAI API key is not set. Please set it as an environment variable.")


def correct_text_with_OpenAI(text):
    prompt = "Correct and format the following text:\n\n" + text
    response = openai.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[{'role': 'user', 'content': prompt}],
      max_tokens=len(text) + 10,
      temperature=0.6
    )
    return response.choices[0].message.content

