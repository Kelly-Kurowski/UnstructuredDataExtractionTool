from fuzzywuzzy import fuzz
import re


def fuzzy_match_input(user_input, options):
    """
    Performs fuzzy matching to find the closest match to user input
    within a list of options.
    """
    best_match = None
    max_score = 80  # Input should be at least an 80% match

    for option in options:
        score = fuzz.partial_ratio(user_input, option)
        if score > max_score:
            max_score = score
            best_match = option

    return best_match


def extract_information(user_input, text):
    # Define fuzzy regular expressions for different types of information
    fuzzy_regexes = {
        # English
        'name': r'\b[A-Z][a-z]*\s+[A-Z][a-z]*\b',  # Match alphabetical characters and spaces
        'e-mail': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',  # Match email addresses
        'phone number': r'\d(?:[\s-]?\d{1,}){6,}',  # Match phone numbers with optional spaces or dashes
        'age': r'\b\d{2}\b',  # Match 2 digits for age
        'invoice date': r"\b(?:\d{1,2}-\d{2}-\d{4}|\d{1,2}-[A-Z]{3}-\d{4}|\d{1,2}\s+\w+\s+\d{4}|\d{1,2}/\d{1,2}/\d{4})\b",
        'bank account number': r"\b[A-Z]{2}\d{2}[A-Z]{4}\d{10}\b",

        # Dutch
        'leeftijd': r'\b\d{2}\b',
        'telefoon nummer': r'\d(?:[\s-]?\d{1,}){6,}',
        'factuurdatum': r"\b(?:\d{1,2}-\d{2}-\d{4}|\d{1,2}-[A-Z]{3}-\d{4}|\d{1,2}\s+\w+\s+\d{4}|\d{1,2}/\d{1,2}/\d{4})\b",
        'iban': r"\b[A-Z]{2}\d{2}[A-Z]{4}\d{10}\b",
        'rekeningnummer': r"\b[A-Z]{2}\d{2}[A-Z]{4}\d{10}\b",
        'kvk': r"\bKVK\s+(\d+)\b",
        'btw': r"\bBTW\s+([A-Za-z0-9]+)\b"
    }

    # Find the closest match to user input among available options
    matched_input = fuzzy_match_input(user_input.lower(), fuzzy_regexes.keys())

    if matched_input:
        # Use the matched input to select the appropriate fuzzy regex
        fuzzy_regex = fuzzy_regexes[matched_input]

        # Find matches in the text using the fuzzy regex
        matches = re.findall(fuzzy_regex, text)

        # If matches are found, return the first match
        if matches:
            return matches[0]  # Return only the first match
        else:
            return "No {} found in the text.".format(matched_input)
    else:
        return "Invalid input. Please provide valid information type."  # Use more advanced technique


# Example usage:
input_text = ""

# Prompt user for input
user_input = input("What information do you want to extract?: ")

# Extract information based on user input
result = extract_information(user_input, input_text)
print(result)
