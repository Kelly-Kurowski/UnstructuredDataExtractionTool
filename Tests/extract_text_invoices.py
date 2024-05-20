import os
from ocr_extraction import get_final_text

with open("test.txt", "r", encoding='utf-8') as text_file:
    content = text_file.read()

file_path = r'C:\Users\kelly\OneDrive\Bureaublad\Inkoop Facturen labSC\13593-4137-bro-2023.pdf'
print(content)
text, _ = get_final_text(file_path)

# Split text into words
words_my_solution = set(text.split())
words_txt = set(content.split())

# Calculate Jaccard similarity
intersection = len(words_my_solution.intersection(words_txt))
union = len(words_my_solution.union(words_txt))
similarity = intersection / union

diff1 = words_my_solution - words_txt
diff2 = words_txt - words_my_solution

print(similarity)
print(f"These words are in my solution but not in the .txt file: {diff1}")
print(f"These words are in the .txt file but not in my solution: {diff2}")