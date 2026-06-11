from fastapi import FastAPI
import requests

app = FastAPI(title="SubTrack Lite")

translations = {
    "en": {
        "welcome": "Subscription analysis complete"
    },
    "hi": {
        "welcome": "सब्सक्रिप्शन विश्लेषण पूरा हुआ"
    },
    "te": {
        "welcome": "సబ్‌స్క్రిప్షన్ విశ్లేషణ పూర్తయింది"
    }
}


@app.get("/")
def root():
    return {
        "app": "SubTrack Lite",
        "status": "running"
    }


@app.post("/analyze")
def analyze(data: dict):

    text = data.get("text", "")
    language = data.get("language", "en")

    total = 0

    for line in text.splitlines():
        words = line.split()

        if len(words) >= 2:
            try:
                total += int(words[-1])
            except:
                pass

    return {
        "message": translations.get(language, translations["en"])["welcome"],
        "monthly_total": total,
        "suggestion": "Cancel unused subscriptions."
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
                "response": "Ollama not running."
            }

    return {
        "provider": "BYOK",
        "message": "Use your own API key."
    }
