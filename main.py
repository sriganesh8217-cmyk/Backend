from fastapi import FastAPI
from google import genai
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
import os


load_dotenv()

app = FastAPI()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (adjust for production)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

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