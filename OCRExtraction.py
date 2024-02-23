import cv2
import numpy as np
import pytesseract
from pdf2image import convert_from_path
from PreprocessingModule import preprocess_image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def extract_text_from_image(image):
    # Perform OCR using Tesseract
    text = pytesseract.image_to_string(image, lang='eng')

    return text


def process_pdf(pdf_path):
    # Convert all pages of the PDF to images
    images = convert_from_path(pdf_path)

    extracted_text = ''

    for i, image in enumerate(images):
        # Convert PIL image to NumPy array
        image_np = np.array(image)

        # Preprocess the image
        preprocessed_image = preprocess_image(image_np)

        # Extract text from preprocessed image
        text = extract_text_from_image(preprocessed_image)

        extracted_text += text

    return extracted_text


if __name__ == '__main__':
    # Path to your PDF or image file
    file_path = 'new_img_1_preprocessed.jpg'

    if file_path.lower().endswith(('.jpg', '.jpeg', '.png', '.tif')):
        image = cv2.imread(file_path)
        preprocessed_image = preprocess_image(image)
        extracted_text = extract_text_from_image(preprocessed_image)
        print(extracted_text)
    elif file_path.lower().endswith('.pdf'):
        extracted_text = process_pdf(file_path)
        print(extracted_text)
    else:
        print("Unsupported file format.")

