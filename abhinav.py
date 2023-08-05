import cv2
import pytesseract
import re
from difflib import SequenceMatcher

def is_pan_card_valid(image_path):
    # Load the image using OpenCV
    image = cv2.imread(image_path)
    
    # Convert the image to grayscale for better OCR results
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    _, threshold_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    
    extracted_text = pytesseract.image_to_string(threshold_image)
    # print(extracted_text)

    # Regular expression pattern to match a valid PAN Card number
    pan_pattern = re.compile(r"[A-Z]{5}[0-9]{4}[A-Z]{1}")
    
    # Regular expression pattern to match the date of birth in the format DD/MM/YYYY
    dob_pattern = re.compile(r"\d{2}/\d{2}/\d{4}")
    
    pan_number = pan_pattern.search(extracted_text)
    # print('pan number', pan_number)
    dob = dob_pattern.search(extracted_text)
    # print('dob', dob)
    if pan_number and dob:
        # similarity_ratio = SequenceMatcher(None, pan_number.group(0), "ABCDE1234F").ratio()
        # print('similarity ratio', similarity_ratio)
        # similarity_threshold = 0.8
        
        # if similarity_ratio >= similarity_threshold:
            return pan_number.group(0), dob.group(0)
    
    return "Invalid alert"

if __name__ == "__main__":
    image_paths = [
        "assets/pan_from_internet.png",
        "assets/pan_from_internet2.png",
        "assets/pan_from_internet3.png",
        "assets/pan1.png",
        "assets/pan2.png",
        "assets/pan3.png",
        "assets/pann.jpeg",
        "assets/pann2.jpeg"
    ]
    
    for image_path in image_paths:
        result = is_pan_card_valid(image_path)
        print(f"Image: {image_path}\nResult: {result}\n")
