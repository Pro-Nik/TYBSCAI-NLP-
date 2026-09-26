# Practical 9: Named Entity Recognition (NER)

# Step 1: Import spaCy
import spacy

# Step 2: Load pre-trained English NLP model
nlp = spacy.load("en_core_web_sm")

# Step 3: Input text
text = """
Rahul works at Microsoft in Mumbai.
He joined the company in 2024.
Microsoft announced a new product worth $500 million.
"""

# Step 4: Process the text
doc = nlp(text)

# Step 5: Extract named entities
print("Named Entities:")
print("----------------")

for entity in doc.ents:
    print(entity.text, "->", entity.label_)

# Step 6: Display meaning of entity labels
print("\nEntity Details:")
print("----------------")

for entity in doc.ents:
    print(
        entity.text,
        "->",
        entity.label_,
        "->",
        spacy.explain(entity.label_)
    )
  
