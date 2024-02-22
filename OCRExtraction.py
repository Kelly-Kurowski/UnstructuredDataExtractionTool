import numpy as np
from pdf2image import convert_from_path
import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def pages_to_images(pdf_path):
    # Convert all pages of the PDF to images
    images = convert_from_path(pdf_path)
    return images


def extract_text_from_image(image):
    # Perform OCR using Tesseract
    text = pytesseract.image_to_string(image, lang='eng')

    return text


if __name__ == '__main__':
    # Path to your PDF or JPEG file
    file_path = 'new_img_1_preprocessed.jpg'

    if file_path.endswith(".pdf"):
        images = pages_to_images(file_path)
        text = ''
        for image in images:
            np_image = np.asarray(image)
            text += extract_text_from_image(np_image)
    else:
        image = cv2.imread(file_path)
        text = extract_text_from_image(image)

    print(text)
