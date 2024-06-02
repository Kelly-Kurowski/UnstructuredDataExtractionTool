import os
from ocr_extraction import get_final_text


# Function to extract the numeric part of the filename
def extract_number(filename):
    return int(filename.split('_')[1].split('.')[0])


# Function to mutate words based on specified rules
def mutate_words(word_list):
    word_set = set(word_list)  # Convert the list to a set to ensure uniqueness
    mutated_set = set()

    for word in word_set:
        # Rule 1: Convert to lower case
        word = word.lower()

        # Rule 2: Remove one characters
        if len(word) == 1:
            continue

        # Rule 3: Remove specific characters from the start or end of the word
        if word.startswith('€'):
            word = word[1:]
        if word.endswith(':') or word.endswith('.') or word.endswith('%') or word.endswith(';') or word.endswith(',') or word.endswith('!') or word.endswith('€'):
            word = word[:-1]

        # Rule 4: Remove '(' and ')' from the start or end of the word
        if word.startswith('('):
            word = word[1:]
        if word.endswith(')'):
            word = word[:-1]

        word = word.replace('-', ' ').replace('—', ' ')

        mutated_set.add(word)

    return mutated_set


file_path1 = r"C:\Users\kelly\OneDrive\Bureaublad\Randomly selected 100 invoices"
file_path2 = r"C:\Users\kelly\OneDrive\Bureaublad\Randomly selected 100 invoices txt"

# List and sort filenames in both directories
files1 = sorted(os.listdir(file_path1), key=extract_number)
files2 = sorted(os.listdir(file_path2), key=extract_number)

# Zip the sorted filenames together
for filename_pdf, filename_txt in zip(files1, files2):
    # Construct full paths for the files
    full_path_pdf = os.path.join(file_path1, filename_pdf)
    full_path_txt = os.path.join(file_path2, filename_txt)

    # Extract text from the PDF file
    text_my_solution, _ = get_final_text(full_path_pdf)

    # Read content from the text file with utf-8 encoding
    with open(full_path_txt, 'r', encoding='utf-8') as file:
        file_content = file.read()

    # Tokenize the texts into sets of words
    set1 = mutate_words(text_my_solution.split())
    set2 = mutate_words(file_content.split())

    # Calculate the intersection and union of the sets
    intersection = set1.intersection(set2)
    union = set1.union(set2)

    diff1 = set1 - set2
    diff2 = set2 - set1
    result = len(intersection) / len(union)

    # Append results to the result file
    with open("Data Invoice/extracted_text_invoices_second_run.txt", "a", encoding='utf-8') as file:
        file.write(f"For the PDF file '{filename_pdf}':\n")
        file.write(f"  Jaccard similarity: {result:.3f}\n")
        file.write(f"  Words in the Text Extraction Component but not in the actual .txt file: {diff1}\n")
        file.write(f"  Words in the .txt file but not in the Text Extraction Component: {diff2}\n")
        file.write("\n")

