from textblob import TextBlob
import wikipedia


def search_wikipedia(name):
    """Functiion to search wikipedia"""
    print(f"Searching for name: {name}")
    return wikipedia.search(name)


def summarize_wikipedia(name):
    """Functiion to summarize wikipedia"""
    print(f"Summarizing for name: {name}")
    return wikipedia.summary(name)


def get_text_blob(text):
    """Functiion  to get text and return blob"""
    blob = TextBlob(text)
    return blob


def get_phrase_blob(name):
    """Find wikipedia name and  return back phrases"""
    text = summarize_wikipedia(name)
    blob = get_text_blob(text)
    phrases = blob.noun_phrases
    return phrases
