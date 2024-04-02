import spacy


def load_package(lang):
    if lang == 'nl':
        return spacy.load('nl_core_news_lg')
    elif lang == 'en':
        return spacy.load('en_core_web_trf')
    else:
        raise ValueError(f"Unsupported language: {lang}")


def map_user_input_to_entity_type(user_input):

        entity_mapping = {
            # English mappings
        'cardinal': 'CARDINAL',
        'date': 'DATE',
        'event': 'EVENT',
        'conference': 'EVENT',
        'festival': 'EVENT',
        'facility': 'FAC',
        'building': 'FAC',
        'airport': 'FAC',
        'bridge': 'FAC',
        'location': 'GPE',
        'geopolitical entity': 'GPE',
        'language': 'LANGUAGE',
        'law': 'LAW',
        'place': 'LOC',
        'money': 'MONEY',
        'total': 'MONEY',
        'amount': 'MONEY',
        'total amount': 'MONEY',
        'nationality': 'NORP',
        'ordinal': 'ORDINAL',
        'organization': 'ORG',
        'company': 'ORG',
        'percentage': 'PERCENT',
        'person': 'PERSON',
        'product': 'PRODUCT',
        'food': 'PRODUCT',
        'vehicle': 'PRODUCT',
        'object': 'PRODUCT',
        'quantity': 'QUANTITY',
        'time': 'TIME',
        'timestamp': 'TIME',
        'artwork': 'WORK_OF_ART',
        'song': 'WORK_OF_ART',
        'book': 'WORK_OF_ART',

        # Dutch mappings
        'kaartinaal': 'CARDINAL',
        'datum': 'DATE',
        'evenement': 'EVENT',
        'conferentie': 'EVENT',
        'festival': 'EVENT',
        'faciliteit': 'FAC',
        'gebouw': 'FAC',
        'vliegveld': 'FAC',
        'brug': 'FAC',
        'locatie': 'GPE',  # Generic term for locations
        'geo-politieke entiteit': 'GPE',  # Generic term for geopolitical entities
        'taal': 'LANGUAGE',
        'wet': 'LAW',
        'plaats': 'LOC',  # Generic term for places
        'geld': 'MONEY',
        'totaal': 'MONEY',
        'bedrag': 'MONEY',
        'totaal bedrag': 'MONEY',
        'nationaliteit': 'NORP',
        'rangtelwoord': 'ORDINAL',
        'organisatie': 'ORG',
        'bedrijf': 'ORG',
        'percentage': 'PERCENT',
        'persoon': 'PERSON',
        'product': 'PRODUCT',
        'eten': 'PRODUCT',
        'voertuig': 'PRODUCT',
        'object': 'PRODUCT',
        'hoeveelheid': 'QUANTITY',
        'tijd': 'TIME',
        'tijdstip': 'TIME',
        'kunstwerk': 'WORK_OF_ART',
        'liedje': 'WORK_OF_ART',
        'boek': 'WORK_OF_ART',
    }

        # Check if the user input exists in the mapping

        if user_input.lower() in entity_mapping:
            return entity_mapping[user_input.lower()]
        else:
            # If the user input doesn't match any predefined mapping, return None
            return None


def extract_entities(entity_type, text):
    # Load the English language model with transformer-based architecture
    nlp = load_package(lang='nl')

    # Process the input text with the NLP pipeline
    doc = nlp(text)

    # Extract entities of the specified type from the document
    entities = [ent.text for ent in doc.ents if ent.label_ == entity_type]

    return entities


entity_type = map_user_input_to_entity_type(input())
print(entity_type)
print(extract_entities('MONEY', 'Ik heb 67 euro bestaald voor die ouwe iPhone.'))


