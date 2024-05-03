import PyPDF2
from langdetect import detect

# Detected language code with corresponding Tesseract language codes.
language_mapping = {
    'en': 'eng',
    'nl': 'nld',

}


def detect_file_language(file_path):
    try:
        # Open the PDF file
        with open(file_path, 'rb') as file:
            # Create a PDF reader object
            reader = PyPDF2.PdfReader(file)

            # Initialize a variable to store the extracted text
            text = ""

            # Iterate through each page of the PDF
            for page_num in range(len(reader.pages)):
                # Extract text from the current page
                page = reader.pages[page_num]
                text += page.extract_text()

        # Detect the language of the text
        language = detect(text)

        return language, language_mapping[language]

    except Exception as e:
        return 'en', 'eng'
