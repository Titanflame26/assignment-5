from pydantic import BaseSettings

class Settings(BaseSettings):
    OLLAMA_MODEL: str = "llama3.2"
    OLLAMA_HOST: str = "http://localhost:11434"

    class Config:
        env_file = ".env"

settings = Settings()
