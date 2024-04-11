import spacy
from spacy.matcher import Matcher
from ai_correction import extract_info_OpenAI


def load_package(lang):
    if lang == 'nl':
        return spacy.load('nl_core_news_lg')
    elif lang == 'en':
        return spacy.load('en_core_web_trf')
    else:
        raise ValueError(f"Unsupported language: {lang}")


## user_input is for instance 'person, date'
def map_user_input_to_entity_type(user_input):
    entity_mapping = {
        # English mappings
        'amount': 'MONEY',
        'birthday': 'DATE',
        'building': 'FAC',
        'city': 'GPE',
        'company': 'ORG',
        'conference': 'EVENT',
        'date': 'DATE',
        'event': 'EVENT',
        'facility': 'FAC',
        'geopolitical entity': 'GPE',
        'language': 'LANGUAGE',
        'law': 'LAW',
        'location': 'GPE',
        'money': 'MONEY',
        'nationality': 'NORP',
        'object': 'PRODUCT',
        'organization': 'ORG',
        'percentage': 'PERCENT',
        'person': 'PERSON',
        'place': 'LOC',
        'product': 'PRODUCT',
        'quantity': 'QUANTITY',
        'time': 'TIME',
        'timestamp': 'TIME',

        # Dutch mappings
        'bedrag': 'MONEY',
        'bedrijf': 'ORG',
        'conferentie': 'EVENT',
        'datum': 'DATE',
        'evenement': 'EVENT',
        'faciliteit': 'FAC',
        'gebouw': 'FAC',
        'geld': 'MONEY',
        'geo-politieke entiteit': 'GPE',
        'geboortedatum': 'DATE',
        'hoeveelheid': 'QUANTITY',
        'locatie': 'GPE',
        'nationaliteit': 'NORP',
        'organisatie': 'ORG',
        'persoon': 'PERSON',
        'plaats': 'GPE',
        'product': 'PRODUCT',
        'stad': 'GPE',
        'dorp': 'GPE',
        'tijd': 'TIME',
        'tijdstip': 'TIME',
        'taal': 'LANGUAGE',
        'verjaardag': 'DATE',
    }

    # Split user input into words
    words = user_input.lower().split(',')

    # Map each word individually
    entity_types = []
    for word in words:
        word = word.strip()
        if word in entity_mapping:
            entity_types.append(entity_mapping[word])
        else:
            # If the word doesn't match any predefined mapping
            entity_types.append(f"{word}: No Matches Found")

    return entity_types



def extract_entities(user_input, text):
    # Modified extract_entities function with enhanced custom pattern matching
    nlp = load_package(lang='en')

    entity_types = map_user_input_to_entity_type(user_input)

    # Process the input text with the NLP pipeline
    doc = nlp(text)

    # Initialize an empty list to store entities
    entities = []

    for entity_type in entity_types:
        # Check if the entity_type has a message indicating it wasn't found
        if ": No Matches Found" in entity_type:
            # Extract the word from the message
            word = entity_type.split(":")[0]
            # Append the word with the message to entities
            # entities.append(f"{word}: No Matches Found")
            # Use OpenAI key to find information in text
            info = extract_info_OpenAI(word, text)
            entities.append(f"{info}")

        # Add custom pattern matching for money entities
        if entity_type == 'MONEY':
            matcher = Matcher(nlp.vocab)
            pattern1 = [{'LIKE_NUM': True}, {'LOWER': {'IN': ['euro', 'dollar', '€', '$', 'USD', 'EUR']}}]
            pattern2 = [{'TEXT': {'IN': ['€', '$', 'USD', 'EUR']}}, {'LIKE_NUM': True}]

            matcher.add('MONEY_PATTERN', [pattern1, pattern2])

            matches = matcher(doc)
            matched_spans = set()  # Keep track of matched spans to avoid duplicates
            for match_id, start, end in matches:
                # Create a new 'MONEY' entity
                span = doc.char_span(doc[start:end].start_char, doc[start:end].end_char, label='MONEY')
                if span is not None and span.text not in matched_spans:
                    entities.append(span.text)
                    matched_spans.add(span.text)

        else:
            entities.extend([ent.text for ent in doc.ents if ent.label_ == entity_type])

    return entities

