import spacy

def perform_ner_spacy(text_file, model_name='en_ner_bc5cdr_md'):
    nlp = spacy.load(model_name)
    with open(text_file, 'r') as file:
        text = file.read()
        doc = nlp(text)
        entities = [(ent.text, ent.label_) for ent in doc.ents if ent.label_ in ['DISEASE', 'DRUG']]
        return entities


ner_entities_spacy = perform_ner_spacy('combined_text.txt')
print(ner_entities_spacy)