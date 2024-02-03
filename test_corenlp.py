from nlplogic.corenlp import get_phrase_blob

def test_get_phrase():
    assert 'golden state' in get_phrase_blob('Golden State Warriors')