import cv2
import pytesseract

# Set the path to the tesseract executable
# This step is not necessary if you've added the Tesseract directory to your system's PATH
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Load the image from file
image = cv2.imread('angle.png')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Use Tesseract to do OCR on the image
text = pytesseract.image_to_string(gray_image, config='--psm 6 -c tessedit_char_whitelist=0123456789')

print(text)