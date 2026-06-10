from collections import Counter
import re


IGNORE_KEYWORDS = [
    "upstox",
    "nse",
    "mutual fund",
    "gamma",
    "kickresume",
    "linkedin",
    "instagram",
    "chatgpt",
    "bse",
]

SUBSCRIPTION_WORDS = [
    "subscription",
    "premium",
    "membership",
    "invoice",
    "receipt",
    "renewal",
    "payment",
    "billing"
]

def extract_sender_name(sender):

    # Example:
    # Netflix <info@netflix.com>
    # returns "Netflix"

    if "<" in sender:
        return sender.split("<")[0].strip()

    # Example:
    # billing@spotify.com
    # returns "spotify"

    if "@" in sender:
        return sender.split("@")[1].split(".")[0]

    return sender


def detect_recurring_services(service):

    results = service.users().messages().list(
        userId="me",
        maxResults=300
    ).execute()

    messages = results.get("messages", [])

    senders = []

    for msg in messages:

        try:

            data = service.users().messages().get(
                userId="me",
                id=msg["id"]
            ).execute()

            headers = data["payload"].get(
                "headers",
                []
            )

            sender = ""
            subject = ""

            for h in headers:

                if h["name"] == "From":
                    sender = h["value"]

                elif h["name"] == "Subject":
                    subject = h["value"]

            if not sender:
                continue

            sender_lower = sender.lower()

            # Skip obvious non-subscription sources
            if any(
                keyword in sender_lower
                for keyword in IGNORE_KEYWORDS
            ):
                continue

            clean_sender = extract_sender_name(sender)

            senders.append(clean_sender)

        except Exception:
            pass

    counts = Counter(senders)

    recurring = []

    for sender, count in counts.items():

        if count >= 3:

            score = min(count * 10, 100)

            recurring.append({
                "sender": sender,
                "count": count,
                "confidence": score
            })

    recurring.sort(
        key=lambda x: x["count"],
        reverse=True
    )

    return recurring[:20]
