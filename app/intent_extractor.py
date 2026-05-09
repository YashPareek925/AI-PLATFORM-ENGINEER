import re


def extract_intent(prompt: str):
    prompt_lower = prompt.lower()

    features = []

    possible_features = [
        "login",
        "dashboard",
        "contacts",
        "payments",
        "analytics",
        "chat",
        "admin panel"
    ]

    for feature in possible_features:
        if feature in prompt_lower:
            features.append(feature)

    app_name = "Custom Application"

    crm_keywords = ["crm", "customer"]

    for word in crm_keywords:
        if word in prompt_lower:
            app_name = "CRM System"

    roles = ["admin", "user"]

    return {
        "app_name": app_name,
        "features": features,
        "roles": roles
    }
