
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from plyer import camera, filechooser
from plyer.utils import platform
import os
import pytesseract 
from PIL import Image 
import cv2 
import re
import json 
from reportlab.lib.pagesizes import letter 
from reportlab.pdfgen import canvas 
from textwrap import fill  # This helps in formatting text into paragraphs 
#import spacey 
from spacey import * 
import subprocess 





def save_to_pdf(extracted_data, file_path ="ocr_output.pdf"):
    # Get the current working directory (where the Python file is located)
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)  # Create the directory if it doesn't exist 

    # Combine directory and file name to get the full path
    #file_path = os.path.join(directory, file_name)

    # Create a PDF file
    c = canvas.Canvas(file_path, pagesize=letter)

    # Set the starting position on the page
    x = 50
    y = 750

    # Add a title to the PDF
    c.setFont("Helvetica-Bold", 16)
    c.drawString(x, y, "Extracted Information from OCR")

    # Move to a new line
    y -= 30

    # Add the extracted text to the PDF
    c.setFont("Helvetica", 12)
    #c.drawString(x, y, f"Extracted Text: {extracted_data}") #just writes a line of text, not good for NER to read 

 # Use textwrap to format the extracted text into paragraphs that fit the page width
    wrapped_text = fill(extracted_data, width=80)

    # Split the wrapped text into lines
    lines = wrapped_text.split("\n") 

    # no need extracted_data[string] as not in dictionary format for json file anymore 
    #y -= 20 

     # Loop through lines and add them to the PDF
    for line in lines:
        c.drawString(x, y, line)
        y -= 15  # Move down to the next line
        
        # Check if we need to create a new page (if there is no space left on the current page)
        if y < 50:
            c.showPage()  # Create a new page
            y = 750  # Reset Y position to top of the new page 

    # Add medications if any
    #if extracted_data.get('medications'):
        #c.drawString(x, y, "Medications Found:")
        #y -= 20
        #for medication in extracted_data['medications']:
         #   c.drawString(x, y, f"- {medication}")
         #   y -= 15

    # Save the PDF file
    c.save() 



class OCRApp: 

    def __init__(self, label): 
        self.label = label # = update label widget in main.py 

    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.label = Label(text="Select an image or take a photo")
        
        # Button to pick an image from the gallery
        self.gallery_button = Button(text="Pick Image from Gallery")
        self.gallery_button.bind(on_press=self.pick_image)
        
        # Button to take a photo using the camera
        self.camera_button = Button(text="Take a Photo")
        self.camera_button.bind(on_press=self.take_photo)
        
        # Add buttons and label to the layout
        self.layout.add_widget(self.label)
        self.layout.add_widget(self.gallery_button)
        self.layout.add_widget(self.camera_button)
        
        return self.layout 
    

    #if want to use own image = 
    def pick_image(self, instance): 
          
        if platform == 'android':
            filechooser.open_file(on_selection=self.on_image_selected)
        else:
            # For desktop platforms, you can simply use the filechooser
            filechooser.open_file(on_selection=self.on_image_selected) 

    #if use camera = 

    def take_photo(self, instance): 
        if platform == 'android':
            # Request camera permission (this is handled internally in buildozer) 
            
            camera.take_picture(on_complete=self.on_picture_taken)
        else:
            self.label.text = "Camera not supported on this platform" 


    #with image selected 

    def on_image_selected(self, selection):  
        if selection:
            image_path = selection[0]  # Get the selected image path
            self.label.text = f"Selected image: {image_path}"
            # You can now pass the image to your OCR function
            self.process_image(image_path) 


    #with image taken 

    def on_picture_taken(self, picture_path): 
        if picture_path:
            self.label.text = f"Picture taken: {picture_path}"
            # You can now pass the taken picture to your OCR function
            self.process_image(picture_path)
 

    #path to tesseract OCR so can use, add to PATH later to simplify 

    #pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR' 

    #where image be = 
    #image_path = r'C:/Users/sophi/Dispenser/App/andriod_app/testocrex.png' 

    def process_image(self, image_path): 


        text = ""  # Initialize text to an empty string to avoid referencing before assignment 

        try: 
            img = Image.open(image_path) 
            text = pytesseract.image_to_string(img)

            # Get the current directory where Android_App.py is located
            current_dir = os.path.dirname(os.path.abspath(__file__))  # This gives the path to the directory all files are currently in, andriod_app 
            
            # Construct path to "info" file, in same directory/folder as Andriod_App.py, in android_app folder 
            save_directory = os.path.join(current_dir, "info") 
            if not os.path.exists(save_directory):
                os.makedirs(save_directory)  # Create the "info" directory if it doesn't exist

            # Path for saving as PDF
            pdf_path = os.path.join(save_directory, "ocr_output.pdf")

            # Save the extracted text to PDF
            save_to_pdf(text, pdf_path)

            # Display the extracted text on the label
            self.label.text = f"Extracted Text: {text}" 

            print(f"Extracted Text: {text}")  # for debugging 

            
 
                
        except Exception as e: 
            # Handle any errors (e.g., file not found, invalid image)
            self.label.text = f"Error: {str(e)}" 
            print(f"uh oh, error!!!") 

        find_value()  

        

        
    #def process_with_spacy(pdf_path): 
        #try: 


            #result = subprocess.run(
                #["python", "spacey.py", pdf_path], 
               # check=True, 
                #capture_output=True, 
                #text=True
            #)
           # 
           # # Parse JSON output
           # output_data = json.loads(result.stdout)
            #frequencies = output_data.get("FREQUENCY", [])

            #if frequencies: 
              #  print(f"Extracted Frequency: {frequencies}")
            #else:
             #   print("No frequency detected.")

        #except subprocess.CalledProcessError as e:
           # print(f"Error running spacey.py: {e}") 


            #current_dir = os.path.dirname(os.path.abspath(__file__))  # Get script directory
            #pdf_path = os.path.join(current_dir, "info", "ocr_output.pdf")  # Path to PDF
            # Call spacey.py and pass the PDF path as an argument
            #subprocess.run(["python", "spacey.py", pdf_path], check=True)
        #except subprocess.CalledProcessError as e:
            #print(f"Error running spacey.py: {e}")
    #current_dir = os.path.dirname(os.path.abspath(__file__))  # Get script directory
    #pdf_path = os.path.join(current_dir, "info", "ocr_output.pdf")  # Path to PDF 
    #process_with_spacy(pdf_path) 

        


        # Function to organize the extracted text into categories
    #def organize_extracted_data(self, text): #nm, I'm going to add all the identification stuff with an AI that reads and identifies in the text PDF form afterwards, like originally planned 
     #   data = {
      #      "person's name": self.extract_person_name(text),
       #     "medication name": self.extract_medication_name(text),
        #    "other info": text  # Optionally store the entire text for reference
        #}
        #return data

    # Function to extract person's name (using a basic regex for now)
    #def extract_person_name(self, text):
       # match = re.search(r"(Mr\.|Mrs\.|Ms\.|Dr\.)\s+[A-Za-z]+", text)
       # if match:
         #   return match.group(0)
       # return "Not found" 
    



    # Sample list of known medications
    #known_medicines = [
   # "Aspirin", "Tylenol", "Ibuprofen", "Paracetamol", "Amoxicillin", "Penicillin", #this pains me lol 
   # "Metformin", "Lipitor", "Advil", "Zoloft", "Vicodin", "Cipro", "Lisinopril",
   # "Omeprazole", "Azithromycin", "Gabapentin", "Losartan", "Atorvastatin", "Famotidine", "Pepcid", "Ranitidine", "Zantac", "Rabeprazole", "Aciphex", "Esomprazole", "Nexium", "Lansoprazole", "Prevacid", "Omeprazole", "Prilosec", "Pantoprazole", "Protonix", "Ondansetron", "Zofran", "Promethazine", "Phenergan", "Metoclopramide", "Reglan", "Diclofenac", "Voltaren", "Motrin", "Naproxen", "Naprosen", "Meloxicam", "Mobic", "Celecoxib", "Celebrex", "Clobetasol", "Temovate", "Hydrocortisone", "Various", "Methylprednisolone", "Medrol", "Prednisolone (Oral)", "Orapred", "Prednisone", "Deltasone", "Morphine ER", 
   # "MS Contin", "Avinza", "Kadian", "Hydrocodone", "Acetaminophen", "Vicodin", "Oxycodone", "Oxycontin", "Tramadol", "Ultram", "Sumatriptan", "Imitrex", "Alendronate", "Fosamax", "Ibandronate", "Boniva", "Baclofen", "Lioresal", "Soma", "Carisoprodol", "Cyclobenzaprine", "Flexeril", "Methocarbamol", "Robaxin", "Tizanidine", "Zanaflex", "Hydroxyzine HCL", "Atarax", "Cetirizine", "Zyrtec", "Levocetirizine", "Xyzal", "Mometasone", "Nasonex", "Triamcinolone", "Nasacort AQ", "Montelukast", "Singulair", "Budesonide", "Pulmicort", "Fluticasone", "Flovent", "Budesonide", "Formoterol", "Symbicort", "Fluticasone", "Salmeterol", "Advair Diskus", "Advair HFA", "Albuterol", "ProAir HFA", "Proventiil HFA", "Ventolin HFA", "Levalbuterol", "Xopenex HFA", 
   # "Ipratropium", "Albuterol", "Combivent", "Tiotropium", "Spiriva", "Benzonatate", "Tessalon Perles", "Meclizine", "Antivert", "Dramamine", "Allopurinol", "Zyloprim", "Zolpidem", "Ambien", "Temazepam", "Restoril", "Varenicline", "Chantix", "Amoxicillin", "Amoxil", "Penicillin", "Amox/Clavulanate", "Augmentin", "Cefdinir", "Omnicef", "Cefuroxime", "Ceftin", "Cephalexin", "Keflex", "Metformin"  
   # ] 

    # Function to extract medication name (basic list matching for demo purposes)
    #def extract_medication_name(self, text):
       # matches = [] 

       # known_medicines = [
        #"Aspirin", "Tylenol", "Ibuprofen", "Paracetamol", "Amoxicillin", "Penicillin", 
        #"Metformin", "Lipitor", "Advil", "Zoloft", "Vicodin", "Cipro", "Lisinopril",
        #"Omeprazole", "Azithromycin", "Gabapentin", "Losartan", "Atorvastatin", "Famotidine", "Pepcid", "Ranitidine", "Zantac", "Rabeprazole", "Aciphex", "Esomprazole", "Nexium", "Lansoprazole", "Prevacid", "Omeprazole", "Prilosec", "Pantoprazole", "Protonix", "Ondansetron", "Zofran", "Promethazine", "Phenergan", "Metoclopramide", "Reglan", "Diclofenac", "Voltaren", "Motrin", "Naproxen", "Naprosen", "Meloxicam", "Mobic", "Celecoxib", "Celebrex", "Clobetasol", "Temovate", "Hydrocortisone", "Various", "Methylprednisolone", "Medrol", "Prednisolone (Oral)", "Orapred", "Prednisone", "Deltasone", "Morphine ER", 
        #"MS Contin", "Avinza", "Kadian", "Hydrocodone", "Acetaminophen", "Vicodin", "Oxycodone", "Oxycontin", "Tramadol", "Ultram", "Sumatriptan", "Imitrex", "Alendronate", "Fosamax", "Ibandronate", "Boniva", "Baclofen", "Lioresal", "Soma", "Carisoprodol", "Cyclobenzaprine", "Flexeril", "Methocarbamol", "Robaxin", "Tizanidine", "Zanaflex", "Hydroxyzine HCL", "Atarax", "Cetirizine", "Zyrtec", "Levocetirizine", "Xyzal", "Mometasone", "Nasonex", "Triamcinolone", "Nasacort AQ", "Montelukast", "Singulair", "Budesonide", "Pulmicort", "Fluticasone", "Flovent", "Budesonide", "Formoterol", "Symbicort", "Fluticasone", "Salmeterol", "Advair Diskus", "Advair HFA", "Albuterol", "ProAir HFA", "Proventiil HFA", "Ventolin HFA", "Levalbuterol", "Xopenex HFA", 
        #"Ipratropium", "Albuterol", "Combivent", "Tiotropium", "Spiriva", "Benzonatate", "Tessalon Perles", "Meclizine", "Antivert", "Dramamine", "Allopurinol", "Zyloprim", "Zolpidem", "Ambien", "Temazepam", "Restoril", "Varenicline", "Chantix", "Amoxicillin", "Amoxil", "Penicillin", "Amox/Clavulanate", "Augmentin", "Cefdinir", "Omnicef", "Cefuroxime", "Ceftin", "Cephalexin", "Keflex", "Metformin"  
        #]  
    
        # Regex pattern to match capitalized words that may be medications
        #pattern = r"\b[A-Za-z]+(?:in|ol|ine|ine|mycin|cillin|statin|zole|azepam|pril|one)\b"

        # Find all matches in the extracted text
        #matches = re.findall(pattern, text)

        # You can match the found words to a list of known medications
        #matched_meds = [med for med in known_medicines if med.lower() in [match.lower() for match in matches]]

        #return matched_meds if matched_meds else "Not Found" 
    # Function to save extracted data into a Python file
   # def save_to_python_file(self, data):
     #   try:
            # Save the extracted data to a Python file as a dictionary
       #     with open("my_json.py", "w") as file:
       #         file.write(f"extracted_data = {json.dumps(data, indent=4)}\n")
       #     print("Data saved to my_json.py")
       # except Exception as e:
       #     print(f"Error saving data to Python file: {e}")


#print it  
#read_text = extract_text(image_path) 
#print(f"Extracted text:{read_text}") 

#if __name__ == '__main__':
    #OCRApp().run() 