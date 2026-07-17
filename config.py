import os
from dotenv import load_dotenv

# .env file se variables load karta hai
load_dotenv()

class Config:
    # API Key ko environment variable se uthayega (security ke liye best hai)
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    
    # Model name
    LLM_MODEL = "llama-3.3-70b-versatile"