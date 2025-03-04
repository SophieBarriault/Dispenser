import spacy
import fitz  # PyMuPDF = PDF extracting 
import sys 
import json #so that OCRApp can read the numerical output 
import os 




def find_value():
    # Step 1: Load the trained spaCy model
    model_dir = './model'  # Path to the trained model (same directory as the Python script)
    #nlp = spacy.load(model_dir) 

    base_path = os.path.dirname(os.path.abspath(__file__))  # Get the script's directory
    model_path = os.path.join(base_path, "model")  # Ensure absolute path

    nlp = spacy.load(model_path) 


    # Defines certain entities the NER may extract and creates a dictionary showing what numerical values they correspond to 
    frequency_map = {
        "twice daily": 2,
        "daily": 1,
        "three times per day": 3,
        "once per day": 1, 
        "two times per day": 2, 
        "three times daily": 3, 
        "four times daily":4, 
        "four times per day":4,  
        #"At night" #add later on 
    }  



    # Step 2: Read the PDF content
    #pdf_path = './info/ocr_output.pdf'  # Path to your PDF file 
    base_path = os.path.dirname(os.path.abspath(__file__))  # Directory of the script
    pdf_path = os.path.join(base_path, "info", "ocr_output.pdf")

    print("PDF Path:", pdf_path)  # Debugging: Check if path is correct 
    pdf_document = fitz.open(pdf_path)



    #etxract the text from pdf 

            
    text = "" 
    for page_num in range(pdf_document.page_count):
            page = pdf_document.load_page(page_num)
            text += page.get_text() 
    # Step 3: Process the extracted text using the trained spaCy model 


    doc = nlp(text)  

    print("\nEntities found in the PDF:")
    for ent in doc.ents: 
        print(f"{ent.text} ({ent.label_})") #for debugging 
        if ent.label_ == "FREQUENCY":
            value = frequency_map.get(ent.text.lower(), "????????")  # = ???????????? if it's not defined in the dictionary above 
            print(f"Extracted: {ent.text} -> Assigned Value: {value}") #for debugging 
        #######now have to take debugging value and make it so that it inputs into main.py (computer_app) for start time and end time 