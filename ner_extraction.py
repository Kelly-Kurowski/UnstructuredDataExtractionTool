import spacy

def load_package(lang):
    if lang == 'nl':
        return spacy.load('nl_core_news_lg')
    elif lang == 'en':
        return spacy.load('en_core_web_trf')
    else:
        raise ValueError(f"Unsupported language: {lang}")




