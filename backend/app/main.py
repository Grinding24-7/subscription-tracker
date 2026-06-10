from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import engine
from app.models import Base
from app.gmail_service import get_gmail_service
from app.email_reader import get_recent_emails
from app.subscription_detector import find_subscriptions
from app.recurring_detector import detect_recurring_services
from fastapi.middleware.cors import CORSMiddleware
from app.summary import get_dashboard_summary
from app.spending_detector import detect_spending

Base.metadata.create_all(bind=engine)

app = FastAPI(title="SubTrack Lite")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "SubTrack Lite API Running"}


@app.get("/emails")
def read_emails():

    service = get_gmail_service()

    return get_recent_emails(
        service,
        max_results=20
    )

@app.get("/subscriptions")
def subscriptions():

    gmail = get_gmail_service()

    return find_subscriptions(gmail)

@app.get("/debug")
def debug():

    service = get_gmail_service()

    results = service.users().messages().list(
        userId="me",
        maxResults=50
    ).execute()

    messages = results.get("messages", [])

    output = []

    for msg in messages[:20]:

        data = service.users().messages().get(
            userId="me",
            id=msg["id"]
        ).execute()

        headers = data["payload"].get("headers", [])

        subject = ""
        sender = ""

        for h in headers:

            if h["name"] == "Subject":
                subject = h["value"]

            if h["name"] == "From":
                sender = h["value"]

        output.append({
            "subject": subject,
            "sender": sender
        })

    return output

@app.get("/recurring")
def recurring():

    gmail = get_gmail_service()

    return detect_recurring_services(gmail)

@app.get("/summary")
def summary():

    gmail = get_gmail_service()

    return get_dashboard_summary(gmail)

@app.get("/spending")
def spending():

    gmail = get_gmail_service()

    return detect_spending(gmail)