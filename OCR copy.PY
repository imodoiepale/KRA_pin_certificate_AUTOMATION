import cv2
import pytesseract
import matplotlib.pyplot as plt
from PIL import Image
import re

# Load the image (update the image path as needed)
image = cv2.imread('cAPTCHA.png')

def read_character(roi_coordinates):
    for i, (x1, y1, x2, y2) in enumerate(roi_coordinates):
        x1 = max(0, x1)
        y1 = max(0, y1)
        x2 = min(image.shape[1], x2)
        y2 = min(image.shape[0], y2)

        # Crop the ROI from the image
        roi = image[y1:y2, x1:x2]

        # Convert the ROI to grayscale
        gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

        # Display the grayscale ROI
        plt.figure()
        plt.imshow(cv2.cvtColor(gray_roi, cv2.COLOR_GRAY2RGB))
        plt.axis('off')
        plt.show()

        # Convert the ROI to a PIL Image
        pil_image = Image.fromarray(gray_roi)

        # Perform OCR on the preprocessed ROI using pytesseract
        extracted_text = pytesseract.image_to_string(pil_image, config='--psm 7')

        # Extract numbers from the extracted text
        numbers = re.findall(r'\d+', extracted_text)

        # Display the extracted numbers
        if numbers:
            print(f"Numbers from ROI: {'.'.join(numbers)}")
        else:
            print(f"No numbers found in ROI")

# Define the regions of interest (ROIs) where you want to extract data
image_parts = [{'x1': 0, 'y1': 0, 'x2': 38, 'y2': 13}]

for coordinate in image_parts:
    x1, y1, x2, y2 = coordinate.values()
    roi_coordinates = [(x1, y1, x2, y2)]
    read_character(roi_coordinates)
