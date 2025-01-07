from fastapi import FastAPI, HTTPException
from service import summarize_text
from model import SummarizationRequest

app = FastAPI()

@app.get("/")
async def root():
    return {
        "message": "Welcome to the Text Summarization API!",
        "endpoints": {
            "/summarize": "POST - Provide text and summary type ('short' or 'points') to get a summary.",
        },
        "example_request": {
            "text": "FastAPI is a modern, fast web framework for building APIs with Python.",
            "summary_type": "points",
        }
    }
    
@app.post("/summarize")
async def summarize(request: SummarizationRequest):
    if not request.text.strip():
        raise HTTPException(status_code=400, detail="Input text cannot be empty.")
    if request.summary_type not in ["short", "points"]:
        raise HTTPException(status_code=400, detail="Invalid summary type. Use 'short' or 'points'.")
    try:
        summary = summarize_text(request.text, request.summary_type)
        return {"summary": summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")