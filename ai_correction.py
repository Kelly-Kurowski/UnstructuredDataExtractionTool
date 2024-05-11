import os
import openai

api_key = os.environ.get('OPENAI_API_KEY')

# Check if the API key is available
if api_key:
    # Set the API key explicitly
    openai.api_key = api_key
else:
    print("OpenAI API key is not set. Please set it as an environment variable.")
# Correct (spelling) mistakes in the following text if there are any: 0.92

# Correct spelling mistakes in the following text if there are any: 0.93 + temperature 0.1!!
# Al 17 getest, ga door met de rest


def correct_text_with_OpenAI(text):
    prompt = f"""
Correct spelling mistakes in the following text if there are any:

{text}
"""
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=[{'role': 'user', 'content': prompt}],
        max_tokens=4096,
        temperature=0.1
    )
    return response.choices[0].message.content


def extract_info_OpenAI(user_input, text):
    prompt = f"""
Extract {user_input} from the following text below.

Text: "{text}"

{user_input}: 
"""
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=[{'role': 'user', 'content': prompt}],
        max_tokens=4096,
        temperature=0.6
    )
    return response.choices[0].message.content
