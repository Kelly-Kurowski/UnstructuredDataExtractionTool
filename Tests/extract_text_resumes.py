import os
from ocr_extraction import get_final_text
from pdfminer.high_level import extract_text

# Directory containing your PDF files
pdf_directory = r'C:\Users\kelly\OneDrive\Bureaublad\Generated Fake Resumes'


# Function to read text from a PDF file using your function and pdfminer
def compare_text_extraction(pdf_file):
    # Extract text using your function
    text_custom, _ = get_final_text(pdf_file)

    # Extract text using pdfminer
    text_pdfminer = extract_text(pdf_file)

    # Split text into words
    words_custom = set(text_custom.split())
    words_pdfminer = set(text_pdfminer.split())

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
pdf_files = pdf_files[198:201]

with open('extracted_text_results_third_run_part3.txt', 'w') as file:
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

