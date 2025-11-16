from fastapi import APIRouter
from app.services.llm_service import ask_llm

router = APIRouter()

@router.get("/health")
def health_check():
    return {"status": "healthy"}

@router.post("/ask")
def ask_model(payload: dict):
    question = payload.get("question")
    if not question:
        return {"error": "Missing 'question' field"}
    
    answer = ask_llm(question)
    return {"answer": answer}
