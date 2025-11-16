import requests
from app.core.config import settings

def ask_llm(prompt: str):
    """
    Sends a prompt to the local Ollama server and returns the model's response.
    """
    url = f"{settings.OLLAMA_HOST}/api/generate"

    payload = {
        "model": settings.OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(url, json=payload)
    response.raise_for_status()

    data = response.json()
    return data.get("response")
