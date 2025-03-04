import pytesseract
from PIL import Image

# If you're using Windows, you might need to specify the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Open the image file
image = Image.open("image.jpg")

# Extract text from the image
text = pytesseract.image_to_string(image)

# Print the extracted text
print(text) 