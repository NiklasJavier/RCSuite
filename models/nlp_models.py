from pydantic import BaseModel

class TextAnalysisRequest(BaseModel):
    text: str

class TextAnalysisResponse(BaseModel):
    word_count: int
    text_length: int
