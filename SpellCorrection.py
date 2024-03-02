from spellchecker import SpellChecker
from joblib import Parallel, delayed


def correct_word(spell_checker, word):
    if word.isupper():  # Do not modify words only containing capital letters
        return word
    corrected_word = spell_checker.correction(word)
    return word if corrected_word is None else corrected_word


def correct_misspelled_words(extracted_words: list, lang: str) -> list:
    """Correct misspelled words in a list.

    Args:
        extracted_words (list): List of words to correct.
        lang (str): Language code for spell checking.

    Returns:
        list: A list of corrected words, if the word is extremely misspelled,
        the misspelled word is returned in the list.
    """
    spell_checker = SpellChecker(language=lang)

    # Use parallel processing to correct words
    corrected_words = Parallel(n_jobs=-1)(delayed(correct_word)(spell_checker, word) for word in extracted_words)

    return corrected_words