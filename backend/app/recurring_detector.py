from collections import Counter


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

            for h in headers:
                if h["name"] == "From":
                    sender = h["value"]

            if sender:
                senders.append(sender)

        except Exception:
            pass

    counts = Counter(senders)

    recurring = []

    for sender, count in counts.items():

        if count >= 3:

            recurring.append({
                "sender": sender,
                "count": count
            })

    recurring.sort(
        key=lambda x: x["count"],
        reverse=True
    )

    return recurring[:20]