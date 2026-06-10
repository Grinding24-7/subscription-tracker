KNOWN_SERVICES = [
    "Netflix",
    "Spotify",
    "YouTube",
    "Google",
    "Google One",
    "Amazon",
    "Prime",
    "Canva",
    "Adobe",
    "Microsoft",
    "OpenAI",
    "ChatGPT",
    "Disney",
    "Hotstar",
    "Apple",
    "iCloud",
    "LinkedIn Premium",
    "Notion",
    "GitHub",
    "Figma"
]


def find_subscriptions(service):

    results = service.users().messages().list(
        userId="me",
        maxResults=200
    ).execute()

    messages = results.get("messages", [])

    subscriptions = []

    for msg in messages:

        try:
            data = service.users().messages().get(
                userId="me",
                id=msg["id"]
            ).execute()

            headers = data["payload"].get("headers", [])

            subject = ""
            sender = ""

            for header in headers:

                if header["name"] == "Subject":
                    subject = header["value"]

                if header["name"] == "From":
                    sender = header["value"]

            text = f"{subject} {sender}"

            for service_name in KNOWN_SERVICES:

                if service_name.lower() in text.lower():

                    subscriptions.append({
                        "service": service_name,
                        "subject": subject,
                        "sender": sender
                    })

                    break

        except Exception:
            pass

    return subscriptions