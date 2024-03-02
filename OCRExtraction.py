import cv2
import numpy as np
import pytesseract
from pdf2image import convert_from_path
from PreprocessingModule import preprocess_image
from SpellCorrection import correct_misspelled_words

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def extract_text_from_image(image, lang='eng'):
    # Perform OCR using Tesseract
    text = pytesseract.image_to_string(image, lang=lang)
    return text.strip()


def process_pdf(pdf_path, lang='eng'):
    # Convert all pages of the PDF to images
    images = convert_from_path(pdf_path)

    extracted_text = ''

    for i, image in enumerate(images):
        # Convert PIL image to NumPy array
        image_np = np.array(image)

        # Preprocess the image
        preprocessed_image = preprocess_image(image_np)
        cv2.imwrite(f'page_{i}_preprocessed.jpg', preprocessed_image)

        # Extract text from preprocessed image
        text = extract_text_from_image(preprocessed_image, lang=lang)

        extracted_text += text

    return extracted_text.strip()

def process_image_file(file_path, lang='eng'):
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


if __name__ == '__main__':
    # Path to your PDF or image file
    file_path = 'Data/13.pdf'

    # Process the file
    OCR_extracted_text = process_image_file(file_path)
    check = correct_misspelled_words(extracted_words=OCR_extracted_text.split(), lang='en')
    print(OCR_extracted_text.split())
    print(check)

