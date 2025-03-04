import spacy
from spacy.training.example import Example
import random
from sklearn.model_selection import train_test_split

# Expanded training data with entity annotations (medical-related, daily and per day frequencies only)
TRAIN_DATA = [
    # Original Examples for Frequency (already present)
    ("JOHNSON, JUDITH VERAPAMIL ER 240 MG tablet GENERIC FOR ISOPTIN SR Manufacturer: Ivax Pharmaceutical Take one tablet by mouth twice daily Treats high blood pressure", {"entities": [(125, 136, "FREQUENCY")]}),
    ("JOHNSON, JUDITH 1 AZOPT Ophth 1% Susp 10mLAL Manufacturer.Alcon Laboratories Instill 1 drop in each eye in the morning and 1 drop in each eye in the evening for glaucoma #Do not use other eye drops at least 10 minutes*", {"entities": [(104, 118, "FREQUENCY")]}),
    
    # Additional similar examples with "daily" or "per day" in frequency
    ("Acetaminophen 500mg, take 1 tablet daily for pain relief", {"entities": [(28, 51, "FREQUENCY")]}),
    ("Aspirin 81mg, take one tablet daily for heart protection", {"entities": [(29, 54, "FREQUENCY")]}),
    ("Ibuprofen 200mg, take 1 tablet daily for fever", {"entities": [(22, 47, "FREQUENCY")]}),
    ("Amoxicillin 500mg, take 1 capsule three times daily for 10 days", {"entities": [(43, 77, "FREQUENCY")]}),
    ("Losartan 50mg, take 1 tablet once daily for high blood pressure", {"entities": [(36, 74, "FREQUENCY")]}),
    ("Paracetamol 650mg, take 1 tablet daily for mild pain relief", {"entities": [(30, 52, "FREQUENCY")]}),
    ("Prednisone 10mg, take 1 tablet daily for inflammation", {"entities": [(28, 54, "FREQUENCY")]}),
    ("Hydrochlorothiazide 25mg, take 1 tablet daily for fluid retention", {"entities": [(50, 84, "FREQUENCY")]}),
    ("Lisinopril 10mg, take 1 tablet daily for blood pressure", {"entities": [(42, 72, "FREQUENCY")]}),
    ("Metformin 500mg, take 1 tablet daily for diabetes", {"entities": [(39, 68, "FREQUENCY")]}),
    ("Clonazepam 0.5mg, take 1 tablet daily for anxiety", {"entities": [(29, 59, "FREQUENCY")]}),
    ("Simvastatin 20mg, take 1 tablet daily for cholesterol", {"entities": [(37, 60, "FREQUENCY")]}),
    ("Furosemide 40mg, take 1 tablet daily for edema", {"entities": [(39, 61, "FREQUENCY")]}),
    ("Alprazolam 1mg, take 1 tablet daily for anxiety", {"entities": [(28, 56, "FREQUENCY")]}),
    ("Lorazepam 2mg, take 1 tablet daily for sleep", {"entities": [(30, 56, "FREQUENCY")]}),
    
    # Continued medical examples with "daily" or "per day"
    ("Doxycycline 100mg, take 1 capsule daily for 7 days", {"entities": [(42, 68, "FREQUENCY")]}),
    ("Cetirizine 10mg, take 1 tablet daily for allergy symptoms", {"entities": [(34, 64, "FREQUENCY")]}),
    ("Hydroxychloroquine 200mg, take 1 tablet daily for lupus", {"entities": [(47, 75, "FREQUENCY")]}),
    ("Gabapentin 300mg, take 1 capsule daily for nerve pain", {"entities": [(44, 74, "FREQUENCY")]}),
    ("Amlodipine 5mg, take 1 tablet daily for high blood pressure", {"entities": [(33, 62, "FREQUENCY")]}),
    ("Montelukast 10mg, take 1 tablet daily for asthma", {"entities": [(35, 62, "FREQUENCY")]}),
    ("Losartan 25mg, take 1 tablet daily for high blood pressure", {"entities": [(34, 62, "FREQUENCY")]}),
    ("Ranitidine 150mg, take 1 tablet daily for acid reflux", {"entities": [(37, 67, "FREQUENCY")]}),
    ("Bupropion 150mg, take 1 tablet daily for depression", {"entities": [(48, 78, "FREQUENCY")]}),
    
    # Additional frequency-based instructions in medical context (daily and per day)
    ("Ibuprofen 400mg, take 1 tablet daily for pain", {"entities": [(22, 47, "FREQUENCY")]}),
    ("Atorvastatin 40mg, take 1 tablet daily for cholesterol management", {"entities": [(37, 72, "FREQUENCY")]}),
    ("Loratadine 10mg, take 1 tablet daily for seasonal allergies", {"entities": [(34, 63, "FREQUENCY")]}),
    ("Gabapentin 600mg, take 1 capsule daily for neuropathy", {"entities": [(44, 74, "FREQUENCY")]}),
    ("Enalapril 10mg, take 1 tablet daily for high blood pressure", {"entities": [(38, 67, "FREQUENCY")]}),
    ("Fluoxetine 20mg, take 1 tablet daily for depression", {"entities": [(37, 63, "FREQUENCY")]}),
    ("Sertraline 50mg, take 1 tablet daily for depression", {"entities": [(37, 65, "FREQUENCY")]}), 


     ("JOHNSON, JUDITH VERAPAMIL ER 240 MG TABLET GENERIC FOR ISOPTIN SR MANUFACTURER: IVAX PHARMACEUTICAL TAKE ONE TABLET BY MOUTH TWICE DAILY TREATS HIGH BLOOD PRESSURE", {"entities": [(125, 136, "FREQUENCY")]}),
    ("JOHNSON, JUDITH 1 AZOPT OPHTH 1% SUSP 10MLAL MANUFACTURER.ALCON LABORATORIES INSTILL 1 DROP IN EACH EYE IN THE MORNING AND 1 DROP IN EACH EYE IN THE EVENING FOR GLAUCOMA #DO NOT USE OTHER EYE DROPS AT LEAST 10 MINUTES*", {"entities": [(104, 118, "FREQUENCY")]}),
    ("ACETAMINOPHEN 500MG, TAKE 1 TABLET DAILY FOR PAIN RELIEF", {"entities": [(28, 51, "FREQUENCY")]}),
    ("ASPIRIN 81MG, TAKE ONE TABLET DAILY FOR HEART PROTECTION", {"entities": [(29, 54, "FREQUENCY")]}),
    ("IBUPROFEN 200MG, TAKE 1 TABLET DAILY FOR FEVER", {"entities": [(22, 47, "FREQUENCY")]}),
    ("AMOXICILLIN 500MG, TAKE 1 CAPSULE THREE TIMES DAILY FOR 10 DAYS", {"entities": [(43, 77, "FREQUENCY")]}),
    ("LOSARTAN 50MG, TAKE 1 TABLET ONCE DAILY FOR HIGH BLOOD PRESSURE", {"entities": [(36, 74, "FREQUENCY")]}),
    ("PARACETAMOL 650MG, TAKE 1 TABLET DAILY FOR MILD PAIN RELIEF", {"entities": [(30, 52, "FREQUENCY")]}),
    ("PREDNISONE 10MG, TAKE 1 TABLET DAILY FOR INFLAMMATION", {"entities": [(28, 54, "FREQUENCY")]}),
    ("HYDROCHLOROTHIAZIDE 25MG, TAKE 1 TABLET DAILY FOR FLUID RETENTION", {"entities": [(50, 84, "FREQUENCY")]}),
    ("LISINOPRIL 10MG, TAKE 1 TABLET DAILY FOR BLOOD PRESSURE", {"entities": [(42, 72, "FREQUENCY")]}),
    ("METFORMIN 500MG, TAKE 1 TABLET DAILY FOR DIABETES", {"entities": [(39, 68, "FREQUENCY")]}),
    ("CLONAZEPAM 0.5MG, TAKE 1 TABLET DAILY FOR ANXIETY", {"entities": [(29, 59, "FREQUENCY")]}),
    ("SIMVASTATIN 20MG, TAKE 1 TABLET DAILY FOR CHOLESTEROL", {"entities": [(37, 60, "FREQUENCY")]}),
    ("FUROSEMIDE 40MG, TAKE 1 TABLET DAILY FOR EDEMA", {"entities": [(39, 61, "FREQUENCY")]}),
    ("ALPRAZOLAM 1MG, TAKE 1 TABLET DAILY FOR ANXIETY", {"entities": [(28, 56, "FREQUENCY")]}),
    ("LORAZEPAM 2MG, TAKE 1 TABLET DAILY FOR SLEEP", {"entities": [(30, 56, "FREQUENCY")]}),
    ("DOXYCYCLINE 100MG, TAKE 1 CAPSULE DAILY FOR 7 DAYS", {"entities": [(42, 68, "FREQUENCY")]}),
    ("CETIRIZINE 10MG, TAKE 1 TABLET DAILY FOR ALLERGY SYMPTOMS", {"entities": [(34, 64, "FREQUENCY")]}),
    ("HYDROXYCHLOROQUINE 200MG, TAKE 1 TABLET DAILY FOR LUPUS", {"entities": [(47, 75, "FREQUENCY")]}),
    ("GABAPENTIN 300MG, TAKE 1 CAPSULE DAILY FOR NERVE PAIN", {"entities": [(44, 74, "FREQUENCY")]}),
    ("AMLODIPINE 5MG, TAKE 1 TABLET DAILY FOR HIGH BLOOD PRESSURE", {"entities": [(33, 62, "FREQUENCY")]}),
    ("MONTELUKAST 10MG, TAKE 1 TABLET DAILY FOR ASTHMA", {"entities": [(35, 62, "FREQUENCY")]}),
    ("LOSARTAN 25MG, TAKE 1 TABLET DAILY FOR HIGH BLOOD PRESSURE", {"entities": [(34, 62, "FREQUENCY")]}),
    ("RANITIDINE 150MG, TAKE 1 TABLET DAILY FOR ACID REFLUX", {"entities": [(37, 67, "FREQUENCY")]}),
    ("BUPROPION 150MG, TAKE 1 TABLET DAILY FOR DEPRESSION", {"entities": [(48, 78, "FREQUENCY")]}),
    ("IBUPROFEN 400MG, TAKE 1 TABLET DAILY FOR PAIN", {"entities": [(22, 47, "FREQUENCY")]}),
    ("ATORVASTATIN 40MG, TAKE 1 TABLET DAILY FOR CHOLESTEROL MANAGEMENT", {"entities": [(37, 72, "FREQUENCY")]}),
    ("LORATADINE 10MG, TAKE 1 TABLET DAILY FOR SEASONAL ALLERGIES", {"entities": [(34, 63, "FREQUENCY")]}),
    ("GABAPENTIN 600MG, TAKE 1 CAPSULE DAILY FOR NEUROPATHY", {"entities": [(44, 74, "FREQUENCY")]}),
    ("ENALAPRIL 10MG, TAKE 1 TABLET DAILY FOR HIGH BLOOD PRESSURE", {"entities": [(38, 67, "FREQUENCY")]}),
    ("FLUOXETINE 20MG, TAKE 1 TABLET DAILY FOR DEPRESSION", {"entities": [(37, 63, "FREQUENCY")]}),
    ("SERTRALINE 50MG, TAKE 1 TABLET DAILY FOR DEPRESSION", {"entities": [(37, 65, "FREQUENCY")]}), 
]

# Split the data into training and validation sets
train_data, val_data = train_test_split(TRAIN_DATA, test_size=0.2)

# Load the pre-trained spaCy model (or use a transformer-based model)
nlp = spacy.load("en_core_web_sm")  # You can use "en_core_web_trf" for better performance

# Add the NER pipeline if it's not already present
if "ner" not in nlp.pipe_names:
    ner = nlp.add_pipe("ner", last=True)

# Add custom entity labels to the NER pipeline
for _, annotations in train_data:
    for ent in annotations.get("entities"):
        nlp.get_pipe("ner").add_label(ent[2])  # Add custom label (e.g., "FREQUENCY")

# Prepare the training data as Example objects
training_examples = []
for text, annotations in train_data:
    doc = nlp.make_doc(text)
    example = Example.from_dict(doc, annotations)
    training_examples.append(example)

# Prepare the validation data as Example objects
validation_examples = []
for text, annotations in val_data:
    doc = nlp.make_doc(text)
    example = Example.from_dict(doc, annotations)
    validation_examples.append(example)

# Training configuration
other_pipes = [pipe for pipe in nlp.pipe_names if pipe != "ner"]
with nlp.disable_pipes(*other_pipes):
    optimizer = nlp.begin_training()
    for epoch in range(50):  # Number of epochs (increase if necessary)
        random.shuffle(training_examples)
        losses = {}
        for batch in spacy.util.minibatch(training_examples, size=8):  # Adjust batch size as needed
            nlp.update(batch, drop=0.5, losses=losses)  # Dropout to prevent overfitting
        print(f"Epoch {epoch + 1} Losses: {losses}")

        # Optional: evaluate the model on validation data after each epoch
        if epoch % 10 == 0:  # Evaluate every 10 epochs
            val_losses = {}
            for batch in spacy.util.minibatch(validation_examples, size=8):
                nlp.evaluate(batch)  # Evaluate on validation data
            print(f"Validation Losses: {val_losses}")

# Save the trained model
output_dir = "./model"  # Save to a folder named "model" in the current directory
nlp.to_disk(output_dir)
print(f"Model saved to {output_dir}")

# Load the trained model
nlp_trained = spacy.load(output_dir)

# Test the trained model on new data 
test_text = "Take this pill twice daily for high blood pressure."
doc = nlp_trained(test_text)

# Print recognized entities
print("\nEntities found in test text:")
for ent in doc.ents:
    print(ent.text, ent.label_)
 