
import requests
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200

    
app = FastAPI(
    title="SubTrack Lite",
    description="AI-powered Subscription Tracker",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

translations = {
    "en": {
        "welcome": "Subscription analysis complete",
        "suggestion": "Consider cancelling unused subscriptions."
    },
    "hi": {
        "welcome": "सब्सक्रिप्शन विश्लेषण पूरा हुआ",
        "suggestion": "अनुपयोगी सदस्यताओं को रद्द करने पर विचार करें।"
    },
    "te": {
        "welcome": "సబ్‌స్క్రిప్షన్ విశ్లేషణ పూర్తయింది",
        "suggestion": "వినియోగంలో లేని సభ్యత్వాలను రద్దు చేయడం గురించి ఆలోచించండి."
    }
}


@app.get("/")
def root():
    return {
        "app": "SubTrack Lite",
        "status": "running",
        "features": [
            "Subscription Analysis",
            "AI Suggestions",
            "Hindi Support",
            "Telugu Support",
            "Ollama",
            "BYOK"
        ]
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/analyze")
def analyze(data: dict):

    text = data.get("text", "")
    language = data.get("language", "en")

    total = 0
    subscriptions = []

    for line in text.splitlines():

        words = line.split()

        if len(words) >= 2:
            try:
                amount = int(words[-1])
                total += amount

                subscriptions.append({
                    "name": " ".join(words[:-1]),
                    "amount": amount
                })

            except:
                pass

    lang = translations.get(language, translations["en"])

    return {
        "message": lang["welcome"],
        "monthly_total": total,
        "subscriptions": subscriptions,
        "suggestion": lang["suggestion"]
    }


@app.post("/ai")
def ai(data: dict):

    prompt = data.get("prompt", "")
    provider = data.get("provider", "local")

    if provider == "local":

        try:
            response = requests.post(
                "http://localhost:11434/api/generate",
                json={
                    "model": "llama3",
                    "prompt": prompt,
                    "stream": False
                },
                timeout=30
            )

            return {
                "provider": "ollama",
                "response": response.json().get("response")
            }

        except:
            return {
                "provider": "ollama",
                "response": "Ollama is not running."
            }

    elif provider == "byok":

        api_key = data.get("api_key")

        if not api_key:
            return {
                "error": "API key required."
            }

        return {
            "provider": "BYOK",
            "message": "API key received successfully."
        }

    return {
        "error": "Unsupported provider."
    }