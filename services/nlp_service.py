class NLPService:
    def analyze(self, text: str) -> dict:
        # Example analysis logic
        word_count = len(text.split())
        return {"word_count": word_count, "text_length": len(text)}
