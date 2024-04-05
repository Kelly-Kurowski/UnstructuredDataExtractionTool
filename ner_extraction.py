import spacy
from spacy.matcher import Matcher


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
        'birthday': 'DATE',
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
        'geboortedatum': 'DATE',
        'verjaardag': 'DATE',
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



def extract_entities(entity_types, text):
    # Modified extract_entities function with enhanced custom pattern matching
    nlp = load_package(lang='nl')

    # Process the input text with the NLP pipeline
    doc = nlp(text)

    # Initialize an empty list to store entities
    entities = []

    for entity_type in entity_types:
        # Add custom pattern matching for money entities
        if entity_type == 'MONEY':
            matcher = Matcher(nlp.vocab)
            pattern1 = [{'IS_DIGIT': True}, {'LOWER': {'IN': ['euro', 'dollar', '€', '$']}}]
            pattern2 = [{'IS_DIGIT': True}, {'TEXT': {'IN': ['euro', 'dollar', '€', '$']}}]
            pattern3 = [{'IS_DIGIT': True}, {'LOWER': 'euro'}]
            pattern4 = [{'IS_DIGIT': True}, {'LOWER': 'dollar'}]
            matcher.add('MONEY_PATTERN', [pattern1, pattern2, pattern3, pattern4])

            matches = matcher(doc)
            matched_spans = set()  # Keep track of matched spans to avoid duplicates
            for match_id, start, end in matches:
                # Create a new 'MONEY' entity
                span = doc.char_span(doc[start:end].start_char, doc[start:end].end_char, label='MONEY')
                if span is not None and span.text not in matched_spans:
                    entities.append(span.text)
                    matched_spans.add(span.text)
                    break  # Stop after the first match

            # If no match found, check for numbers
            if not entities:
                for token in doc:
                    if token.like_num:
                        entities.append(token.text)
                        break  # Stop after the first match
        else:
            entities.extend([ent.text for ent in doc.ents if ent.label_ == entity_type])

    return entities


print(extract_entities(entity_types=['DATE'], text='KLM is opgericht in 12-11-1978'))