from spellchecker import SpellChecker
from joblib import Parallel, delayed
import math
import time


def correct_words_batch(spell_checker, words):
    corrected_batch = []
    for word in words:
        # Skip processing for capitalized words
        if not (word.isupper() or word[0].isupper()):
            corrected_word = spell_checker.correction(word)
            word = word if corrected_word is None else corrected_word
        corrected_batch.append(word)
    return corrected_batch


def correct_misspelled_words(extracted_words: list, lang: str, batch_size: int = 100) -> list:
    """Correct misspelled words in a list.

    Args:
        extracted_words (list): List of words to correct.
        lang (str): Language code for spell checking.
        batch_size (int): Number of words to process in each batch.

    Returns:
        list: A list of corrected words.
    """

    start_time = time.time()
    # Initialize spell checker once
    spell_checker = SpellChecker(language=lang)

    if len(extracted_words) < 200:
        batch_size = 60

    # Calculate the number of batches needed
    num_batches = math.ceil(len(extracted_words) / batch_size)

    # Correct words in each batch
    corrected_words = []
    for i in range(num_batches):
        start_idx = i * batch_size
        end_idx = min((i + 1) * batch_size, len(extracted_words))
        batch = extracted_words[start_idx:end_idx]

        # Correct words in the batch
        corrected_batch = correct_words_batch(spell_checker, batch)
        corrected_words.extend(corrected_batch)

    end_time = time.time()  # Record end time
    elapsed_time = end_time - start_time  # Calculate elapsed time
    print("Elapsed time:", elapsed_time, "seconds")  # Print elapsed time

    return corrected_words

