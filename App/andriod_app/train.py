import random
from spacy.training.example import Example

# Create the training data in the format spaCy expects
training_examples = []
for text, annotations in TRAIN_DATA:
    doc = nlp.make_doc(text)
    example = Example.from_dict(doc, annotations)
    training_examples.append(example)

# Start training
# Disable other pipeline components to avoid them being updated during training (except NER)
other_pipes = [pipe for pipe in nlp.pipe_names if pipe != "ner"]
with nlp.disable_pipes(*other_pipes):
    optimizer = nlp.begin_training()
    for epoch in range(30):  # Adjust the number of epochs based on your data
        random.shuffle(training_examples)
        losses = {}
        # Iterate over the training data
        for batch in spacy.util.minibatch(training_examples, size=8):
            # Update the model with each batch
            nlp.update(batch, drop=0.5, losses=losses)
        print(f"Epoch {epoch + 1} Losses: {losses}")
