import re
from fuzzywuzzy import fuzz
from ner_extraction import extract_entities

def fuzzy_match_input(user_input, options):
    """
    Performs fuzzy matching to find the closest match to user input
    within a list of options.
    """
    best_match = None
    max_score = 80  # Input should be at least an 80% match

    for option in options:
        score = fuzz.partial_ratio(user_input, option)
        if score == 100 and len(user_input) == len(option):
            return user_input
        elif score > max_score:
            max_score = score
            best_match = option

    return best_match

def extract_information(user_input, text):
    # Define fuzzy regular expressions for different types of information
    fuzzy_regexes = {
        # English
        'name': r'\b[A-Z][a-z]*\s+[A-Z][a-z]*\b',  # Match alphabetical characters and spaces
        'surname': r'\b[A-Z][a-z]*\s+([A-Z][a-z]*)\b',
        'e-mail': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',  # Match email addresses
        'phone number': r'\d(?:[\s-]?\d{1,}){6,}',  # Match phone numbers with optional spaces or dashes
        'age': r'\b\d{2}\b',  # Match 2 digits for age
        'invoice date': r"\b(?:\d{1,2}-\d{2}-\d{4}|\d{1,2}-[A-Z]{3}-\d{4}|\d{1,2}\s+\w+\s+\d{4}|\d{1,2}/\d{1,2}/\d{4})\b",
        'bank account number': r"\b[A-Z]{2}\s*\d{2}\s*[A-Z]{4,}\s*\d{7,}\b|\b[A-Z]{2}\s*\d{2}\s*[A-Z]{4,}\s*\d{4}\s*\d{4}\s*\d{2}\b",
        'website': r"\b(?:https?://)?(?:www\.)?[a-zA-Z0-9-]+(?:\.[a-zA-Z]{2,})+\b",
        'total': r"(?i)(?:totaal|total|totaal\sbedrag|total\samount)[:\s]*([€]?\s*[\d.,]+)",

        # Dutch
        'naam': r'\b[A-Z][a-z]*\s+[A-Z][a-z]*\b',
        'achternaam': r'\b[A-Z][a-z]*\s+([A-Z][a-z]*)\b',
        'adres': r"\b[A-Z]\w*\s+\d{1,3}(?:\s*[-\s]?[A-Z]|\s*[A-Z]?)?(?:,\s*|\s+)\d{4}\s+[A-Z]{2}\s+[A-Z]\w*\b",
        'leeftijd': r'\b\d{2}\b',
        'telefoon nummer': r'\d(?:[\s-]?\d{1,}){6,}',
        'factuurdatum': r"\b(?:\d{1,2}-\d{2}-\d{4}|\d{1,2}-[A-Z]{3}-\d{4}|\d{1,2}\s+\w+\s+\d{4}|\d{1,2}/\d{1,2}/\d{4})\b",
        'iban': r"\b[A-Z]{2}\s*\d{2}\s*[A-Z]{4,}\s*\d{7,}\b|\b[A-Z]{2}\s*\d{2}\s*[A-Z]{4,}\s*\d{4}\s*\d{4}\s*\d{2}\b",
        'rekeningnummer': r"\b[A-Z]{2}\s*\d{2}\s*[A-Z]{4,}\s*\d{7,}\b|\b[A-Z]{2}\s*\d{2}\s*[A-Z]{4,}\s*\d{4}\s*\d{4}\s*\d{2}\b",
        'kvk': r"\bKVK\s+(\d+)\b|\bKvK\s+(\d+)\b",
        'btw': r"\bBTW\s+([A-Za-z0-9]+)\b",
        'totaal': r"(?i)(?:totaal|total|totaal\sbedrag|total\samount)[:\s]*([€]?\s*[\d.,]+)",
        'totaal bedrag': r"(?i)(?:totaal|total|totaal\sbedrag|total\samount)[:\s]*([€]?\s*[\d.,]+)",
    }

    # Convert user_input to lowercase to ensure case-insensitive matching
    user_input = user_input.lower()

    # Check if user_input is a comma-separated list
    if ',' in user_input:
        user_input_list = [x.strip() for x in user_input.split(',')]
    else:
        user_input_list = [user_input]

    results = []

    for input_type in user_input_list:
        # Find the closest match to user input among available options
        matched_input = fuzzy_match_input(input_type, fuzzy_regexes.keys())

        if matched_input:
            # Use the matched input to select the appropriate fuzzy regex
            fuzzy_regex = fuzzy_regexes[matched_input]

            # Find matches in the text using the fuzzy regex
            matches = re.findall(fuzzy_regex, text)

            # If matches are found, add to results list
            if matches:
                # Extend the results list with each match separately
                for match in matches:
                    results.append(f'{input_type}: {match}')
            else:
                results.append(f'{input_type}: No Matches Found')
        else:
            # If the input type is not found in fuzzy_regexes, use NER extraction
            ner_matches = extract_entities(input_type, text)
            for match in ner_matches:
                results.append(f'{input_type}: {match}')

        results = [result.replace('\n', ' ') for result in results]

    return results


print(extract_information("total", "Basisbedrag belast met 0% btw € 642,97 Basisbedrag belast met 21% btw € 0,00 Btw 21% € 0,00 Totaal: € 642,97"))