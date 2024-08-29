import spacy

class NLPService:
    def __init__(self, model_name: str = "en_core_web_sm"):
        self.model = spacy.load(model_name)

    def analyze_text(self, text: str):
        doc = self.model(text)
        return [(ent.text, ent.label_) for ent in doc.ents]

def get_nlp_service():
    return NLPService()
