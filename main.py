from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from google import genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = FastAPI()

# ✅ CORS (IMPORTANT - must be after app = FastAPI())
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For testing. In production, replace with frontend domain.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Get API Key safely
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY is not set in environment variables.")

# ✅ Initialize Gemini client
client = genai.Client(api_key=GOOGLE_API_KEY)


@app.get("/")
def home():
    return {"message": "Backend running 🚀"}


@app.get("/ask")
def ask(question: str = ""):
    if not question.strip():
        return {"error": "Question cannot be empty"}

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",  # stable model
            contents=question
        )

        return {"answer": response.text}

    except Exception as e:
        return {"error": str(e)}