import json 
from flask import Flask, render_template, request 

text = """
David Hale, M.D. he is 45 years old and works as Data Engineer at GE 
Healthcare, which is located in Delaware. For personal Contact and 
Email: 555-555-555, hale@gmail.com, Dr. Molina Cortes, MD. is 
affiliated with the Cocke County Baptist Hospital in Des Moines.
"""

ents = {
    "DATE": [],
    "NAME": [],
    "AGE": [],
    "LOCATION": [],
    "PROFESSION": [],
    "CONTACT": [],
    "Email": []
}

ner_prompt = f"""<|input|>
### Template: 




### Text:
{text}
<|output|>
""" 
#with open('JsonFile.txt','w') as fp: 
 
Medication_Information = {json.dumps(ents, indent=4)} 
print (Medication_Information)



# print (output) 