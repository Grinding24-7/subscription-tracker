from app.recurring_detector import detect_recurring_services


def get_dashboard_summary(gmail):

    services = detect_recurring_services(gmail)

    return {
        "total_services": len(services),
        "top_service": services[0]["sender"] if services else "None",
        "total_emails": sum(
            service["count"]
            for service in services
        )
    }