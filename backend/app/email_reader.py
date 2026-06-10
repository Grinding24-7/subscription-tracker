def get_recent_emails(service, max_results=20):

    results = service.users().messages().list(
        userId="me",
        maxResults=max_results
    ).execute()

    messages = results.get("messages", [])

    emails = []

    for msg in messages:

        data = service.users().messages().get(
            userId="me",
            id=msg["id"]
        ).execute()

        headers = data["payload"].get("headers", [])

        subject = ""

        for header in headers:
            if header["name"] == "Subject":
                subject = header["value"]

        emails.append({
            "id": msg["id"],
            "subject": subject
        })

    return emails