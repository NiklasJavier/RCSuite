from pydantic import BaseModel

class NLPRequest(BaseModel):
    text: str

class NLPResponse(BaseModel):
    result: list
