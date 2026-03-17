from fastapi import FastAPI
from pydantic import BaseModel
from utils import summarize_text

# Initialize app
app = FastAPI()

# Request schema
class InputText(BaseModel):
    text: str

# Root endpoint (for testing)
@app.get("/")
def home():
    return {"message": "AI Summarizer API is running 🚀"}

# Summarization endpoint
@app.post("/summarize")
def summarize(input: InputText):
    summary = summarize_text(input.text)
    
    return {
        "original_length": len(input.text),
        "summary": summary
    }
