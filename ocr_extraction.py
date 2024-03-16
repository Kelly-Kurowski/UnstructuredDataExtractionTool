import cv2
import numpy as np
import pytesseract
from pdf2image import convert_from_path
from preprocessing import preprocess_image
from spell_correction import correct_misspelled_words
from ai_correction import correct_text_with_OpenAI
from language import detect_file_language

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Define a default language for Tesseract OCR
DEFAULT_LANGUAGE_TESSERACT = 'eng'


def extract_text_from_image(image, lang=DEFAULT_LANGUAGE_TESSERACT):
    # Perform OCR using Tesseract
    text = pytesseract.image_to_string(image, lang=lang)
    return text.strip()


def process_pdf(pdf_path, lang=DEFAULT_LANGUAGE_TESSERACT):
    # Convert all pages of the PDF to images
    images = convert_from_path(pdf_path)

    extracted_text = ''

    for i, image in enumerate(images):
        # Convert PIL image to NumPy array
        image_np = np.array(image)

        # Preprocess the image
        preprocessed_image = preprocess_image(image_np)
        # cv2.imwrite(f'new_img_preprocessed{i}.jpg', preprocessed_image)

        # Extract text from preprocessed image
        text = extract_text_from_image(preprocessed_image, lang=lang)

        extracted_text += text

    return extracted_text.strip()


def process_file(file_path, lang=DEFAULT_LANGUAGE_TESSERACT):
    # Check file format and process accordingly
    if file_path.lower().endswith(('.jpg', '.jpeg', '.png', '.tif')):
        image = cv2.imread(file_path)
        preprocessed_image = preprocess_image(image)
        extracted_text = extract_text_from_image(preprocessed_image, lang=lang)
        cv2.imwrite(f'new_img_preprocessed.jpg', preprocessed_image)
        return extracted_text
    elif file_path.lower().endswith('.pdf'):
        extracted_text = process_pdf(file_path, lang=lang)
        return extracted_text
    else:
        return "Unsupported file format."


def get_final_text(file_path):
    language_code, language_code_tesseract = detect_file_language(file_path)

    OCR_extracted_text = process_file(file_path, lang=language_code_tesseract)
    text_with_corrected_words = correct_misspelled_words(extracted_words=OCR_extracted_text.split(), lang=language_code)
    final_result = correct_text_with_OpenAI(" ".join(text_with_corrected_words))

    return final_result
