import easyocr
from pdf2image import convert_from_path
import io


def pages_to_images(pdf_path):
    # Convert all pages of the PDF to images
    images = convert_from_path(pdf_path)
    return images


def extract_text_from_pdf(pdf_path):
    text = ''
    # Create an EasyOCR reader object
    reader = easyocr.Reader(['en'])

    # Convert PDF to images
    images = pages_to_images(pdf_path)

    # Process each image separately
    for img in images:
        # Convert image to bytes
        img_bytes = io.BytesIO()
        img.save(img_bytes, format='JPEG')
        img_bytes = img_bytes.getvalue()

        # Perform OCR on the image
        result = reader.readtext(img_bytes)

        # Extract and append the text from OCR result
        for detection in result:
            text += detection[1] + ' '
    return text


# Path to your PDF file
pdf_path = 'Data/inkoop_factuur.pdf'

# Extract text from the PDF
text = extract_text_from_pdf(pdf_path)

# Print the extracted text
print(text)