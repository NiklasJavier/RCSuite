import pytest
from services.nlp_service import NLPService

@pytest.fixture
def nlp_service():
    return NLPService()

def test_analyze(nlp_service):
    text = "This is a test text."
    result = nlp_service.analyze(text)
    assert result["word_count"] == 5
    assert result["text_length"] == len(text)
