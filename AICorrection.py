import os
import openai

api_key = os.environ.get('OPENAI_API_KEY')

# Check if the API key is available
if api_key:
    # Set the API key explicitly
    openai.api_key = api_key
else:
    print("OpenAI API key is not set. Please set it as an environment variable.")

def correct_text(text):
    prompt = "Correct the following text:\n\n" + text
    response = openai.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[{'role': 'user', 'content': prompt}],
      max_tokens=len(text) + 10
    )
    return response.choices[0].message.content


# Example usage
text_to_correct = "KAPIL GAWANDE a & ML ENGINEER PROFILE ixpecierced a & RAL engine stilled in analyzing large datasets, developing advaacecl ML solutions and carried nice ne insights effectively proficient i penal and Hugging Face APlfcor creating into light catboats and ALP ready z designing and optimizing machine learning plipelinestar seamless integration and delivering siasn-quality All salutionstiat drive real business value"
corrected_text = correct_text(text_to_correct)
print(corrected_text)
