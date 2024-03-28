from fuzzywuzzy import fuzz
import re


def fuzzy_match_input(user_input, options):
    """
    Performs fuzzy matching to find the closest match to user input
    within a list of options.
    """
    best_match = None
    max_score = -1

    for option in options:
        score = fuzz.partial_ratio(user_input, option)
        if score > max_score:
            max_score = score
            best_match = option

    return best_match


def extract_information(user_input, text):
    # Define fuzzy regular expressions for different types of information
    fuzzy_regexes = {
        'name': r'\b[A-Z][a-z]*\s+[A-Z][a-z]*\b',  # Match alphabetical characters and spaces
        'e-mail': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',  # Match email addresses
        'phone number': r'\d(?:[\s-]?\d{1,}){6,}',  # Match phone numbers with optional spaces or dashes
        'age': r'\b\d{2}\b',  # Match 2 digits for age
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
        return "Invalid input. Please provide valid information type ('name', 'email', 'phone number')."


# Example usage:
input_text = "My name is Johans Doe, my email is john@example.com, and my phone number is 06789800. I was born in 1989"

# Prompt user for input
user_input = input("What information do you want to extract?: ")

# Extract information based on user input
result = extract_information(user_input, input_text)
print(result)
