import cv2
from pdf2image import convert_from_path
import numpy as np


def preprocess_image(image):
    # Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply binary thresholding
    _, binary_image = cv2.threshold(gray_image, 200, 255, cv2.THRESH_BINARY)

    # Sharpen the text
    sharpened_image = cv2.GaussianBlur(binary_image, (0, 0), 3)
    sharpened_image = cv2.addWeighted(binary_image, 1.2, sharpened_image, -0.2, 0)

    return sharpened_image


# Convert PDF to list of PIL images
images = convert_from_path('Data/soham.pdf')

# Iterate through each PIL image
for i, image in enumerate(images):
    # Convert PIL image to NumPy array
    image_np = np.array(image)

    # Preprocess the image
    preprocessed_image = preprocess_image(image_np)

    # Write the preprocessed image to disk
    cv2.imwrite(f'new_img_{i + 1}_preprocessed.jpg', preprocessed_image)
