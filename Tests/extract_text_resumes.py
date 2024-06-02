import os
from ocr_extraction import get_final_text
from pdfminer.high_level import extract_text

# Directory containing your PDF files
pdf_directory = r'C:\Users\kelly\OneDrive\Bureaublad\Generated Fake Resumes'


def mutate_words(word_list):
    word_set = set(word_list)  # Convert the list to a set to ensure uniqueness
    mutated_set = set()

    for word in word_set:
        # Rule 1: Convert to lower case
        word = word.lower()

        # Rule 2: Don't add character to the list
        if len(word) == 1:
            continue

        # Rule 3: Remove specific characters from the start or end of the word
        if word.startswith(('€', '[')):
            word = word[1:]
        if word.endswith(':') or word.endswith('.') or \
                word.endswith('%') or word.endswith(';') or \
                word.endswith(',') or word.endswith('!') or \
                word.endswith('€') or word.endswith(']'):
            word = word[:-1]

        # Rule 4: Remove '(' and ')' from the start or end of the word
        if word.startswith('('):
            word = word[1:]
        if word.endswith(')'):
            word = word[:-1]

        word = word.replace('-', '').replace('—', '')

        mutated_set.add(word)

    return mutated_set


# Function to read text from a PDF file using your function and pdfminer
def compare_text_extraction(pdf_file):
    # Extract text using your function
    text_custom, _ = get_final_text(pdf_file)

    # Extract text using pdfminer
    text_pdfminer = extract_text(pdf_file)

    # Split text into words
    words_custom = mutate_words(text_custom.split())
    words_pdfminer = mutate_words(text_pdfminer.split())

    # Calculate Jaccard similarity
    intersection = len(words_custom.intersection(words_pdfminer))
    union = len(words_custom.union(words_pdfminer))
    similarity = intersection / union

    diff1 = words_custom - words_pdfminer
    diff2 = words_pdfminer - words_custom

    return similarity, diff1, diff2


# Iterate through all PDF files in the directory
pdf_files = [file for file in os.listdir(pdf_directory) if file.endswith('.pdf')]
pdf_files.sort(key=lambda x: int(x.split('_')[-1].split('.')[0]))
pdf_files = pdf_files[341:]

with open('Data Resume/extracted_text_resumes_fourth_run.txt', 'a') as file:
    for pdf_file in pdf_files:

        # Construct full path to PDF file
        pdf_path = os.path.join(pdf_directory, pdf_file)

        # Calculate Jaccard similarity
        jaccard_similarity, diff1, diff2 = compare_text_extraction(pdf_path)

        # Extract the numerical part of the filename for enumeration
        file_number = int(pdf_file.split('_')[-1].split('.')[0])

        # Output comparison result
        # Write Jaccard similarity and word differences to file
        file.write(f"For the PDF file '{pdf_file}' (File {file_number}):\n")
        file.write(f"  Jaccard similarity: {jaccard_similarity:.3f}\n")
        file.write(f"  Words in the Text Extraction Component but not in the PDF extractor: {diff1}\n")
        file.write(f"  Words in the PDF extractor but not in the Text Extraction Component: {diff2}\n")
        file.write("\n")

