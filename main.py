from fastapi import FastAPI
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

@app.get("/")
def home():
    return {"message": "Backend running 🚀"}

@app.get("/ask")
def ask(question: str):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=question
    )
    return {"answer": response.text}