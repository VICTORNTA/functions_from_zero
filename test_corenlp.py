from nlplogic.corenlp import search_wikipedia,summarize_wikipedia,get_text_blob,get_phrase_blob

def test_get_phrase():
    assert 'golden state' in get_phrase_blob('Golden State Warriors')