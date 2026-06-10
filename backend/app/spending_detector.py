import re


PAYMENT_KEYWORDS = [
    "paid",
    "payment",
    "invoice",
    "receipt",
    "charged",
    "debited",
    "transaction",
    "renewal",
]


def extract_amount(text):

    patterns = [
        r"₹\s?(\d+(?:,\d+)*(?:\.\d+)?)",
        r"Rs\.?\s?(\d+(?:,\d+)*(?:\.\d+)?)",
        r"INR\s?(\d+(?:,\d+)*(?:\.\d+)?)",
    ]

    for pattern in patterns:

        match = re.search(pattern, text)

        if match:
            amount = match.group(1).replace(",", "")

            try:
                return float(amount)
            except:
                pass

    return None


def detect_spending(service):

    results = service.users().messages().list(
        userId="me",
        maxResults=100
    ).execute()

    messages = results.get("messages", [])

    total = 0
    transactions = []

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

            subject = ""

            for h in headers:

                if h["name"] == "Subject":
                    subject = h["value"]

            subject_lower = subject.lower()

            if not any(
                word in subject_lower
                for word in PAYMENT_KEYWORDS
            ):
                continue

            amount = extract_amount(subject)

            if amount:

                total += amount

                transactions.append({
                    "subject": subject,
                    "amount": amount
                })

        except Exception:
            pass

    return {
        "total_spend": round(total, 2),
        "transactions": transactions[:20]
    }