import cv2
from pdf2image import convert_from_path
import numpy as np


def preprocess_image(image):
    # Scale image to a larger size to recognize small characters.
    img = cv2.resize(image, None, fx=1.3, fy=1.3, interpolation=cv2.INTER_CUBIC)

    # Convert to grayscale
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply binary thresholding
    _, binary_image = cv2.threshold(gray_image, 180, 255, cv2.THRESH_BINARY)

    # Apply morphological erosion to fill gaps between letters
    kernelE = np.ones((2, 2), np.uint16)  # Kernel size can be adjusted
    eroded_image = cv2.erode(binary_image, kernelE, iterations=1)

    kernelD = np.ones((2, 2), np.uint16)
    dilated_image = cv2.dilate(eroded_image, kernelD, iterations=1)

    # Find contours
    contours, _ = cv2.findContours(dilated_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Create a mask to extract only the text regions
    mask = np.zeros_like(dilated_image)

    # Draw contours on the mask
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 3:  # Adjust this threshold based on your document
            cv2.drawContours(mask, [contour], -1, 255, thickness=cv2.FILLED)

    # Apply the mask to the grayscale image
    result = cv2.bitwise_and(gray_image, dilated_image, mask=mask)

    sharpened_image = cv2.filter2D(result, -1, np.array([[-1, -1, -1],
                                                        [-1, 12, -1],
                                                        [-1, -1, -1]]))

    return sharpened_image


# Convert PDF to list of PIL images
images = convert_from_path('Data/inkoop_factuur.pdf')

# Iterate through each PIL image
for i, image in enumerate(images):
    # Convert PIL image to NumPy array
    image_np = np.array(image)

    # Preprocess the image
    preprocessed_image = preprocess_image(image_np)

    # Write the preprocessed image to disk
    cv2.imwrite(f'new_img_{i + 1}_preprocessed.jpg', preprocessed_image)
