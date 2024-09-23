from fastapi import FastAPI
from model import TextData
from service import summarize_text

app = FastAPI()
@app.get("/")
def home():
    return {"message": "This is a Text Summarization tool built with python, pytorch & transformers which utilizes the google/pegasus-xsum model."}


@app.post("/summarize")
async def summarize(data: TextData):
    summary = summarize_text(data.text)
    return {"summary": summary}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)