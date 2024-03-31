import spacy


def load_package(lang):
    if lang == 'nl':
        return spacy.load('nl_core_news_lg')
    elif lang == 'en':
        return spacy.load('en_core_web_trf')
    else:
        raise ValueError(f"Unsupported language: {lang}")


def extract_entities(entity_type, text):
    # Load the English language model with transformer-based architecture
    nlp = load_package(lang='en')

    # Process the input text with the NLP pipeline
    doc = nlp(text)

    # Extract entities of the specified type from the document
    entities = [ent.text for ent in doc.ents if ent.label_ == entity_type]

    return entities


print(extract_entities('EDUCATION', 'I completed my Bachelor Degree in Computer Science at the University of Example.'))



