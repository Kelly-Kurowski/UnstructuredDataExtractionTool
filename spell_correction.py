from spellchecker import SpellChecker
from joblib import Parallel, delayed
import math


def correct_words_batch(spell_checker, words):
    corrected_batch = []
    for word in words:
        # Skip processing for capitalized words
        if not (word.isupper() or word[0].isupper()):
            corrected_word = spell_checker.correction(word)
            word = word if corrected_word is None else corrected_word
        corrected_batch.append(word)
    return corrected_batch


def correct_misspelled_words(extracted_words: list, lang: str, batch_size: int = 75) -> list:

    # Initialize spell checker once
    spell_checker = SpellChecker(language=lang)

    if len(extracted_words) < 220:
        batch_size = 30

    # Calculate the number of batches needed
    num_batches = math.ceil(len(extracted_words) / batch_size)

    # Correct words in each batch in parallel
    corrected_batches = Parallel(n_jobs=-1)(
        delayed(correct_words_batch)(
            spell_checker, extracted_words[i * batch_size:min((i + 1) * batch_size, len(extracted_words))]
        ) for i in range(num_batches)
    )

    # Flatten the list of lists into a single list
    corrected_words = [word for batch in corrected_batches for word in batch]

    return corrected_words
