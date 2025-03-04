import pytesseract 
from PIL import Image 
import cv2 

#path to tesseract OCR so can use, add to PATH later to simplify 

pytesseract.pytesseract.tesseract_cmd = r':/Users/sophi/AppData/Local/Programs/Python/Python310\Scripts/pytesseract.exe' 

#where image be = 
image_path = 'r./testOCRimage.webp' 

def extract_text(image_path): 
    #load image 
    img = cv2.imread(image_path) 

    #into greyscale = better OCR accuracy 
    turn_grey = cv2.cvtColor (img, cv2.COLOR_BGR2GRAY) 


    #use OCR 

    text = pytesseract.image_to_string(turn_grey) 
    return text 

#print it  
text = extract_text(image_path) 
print(f"Extracted text:{text}") 