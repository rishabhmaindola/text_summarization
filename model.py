from pydantic import BaseModel

class SummarizationRequest(BaseModel):
    text: str
    summary_type: str 
