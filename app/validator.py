required_keys = [
    "ui_schema",
    "api_schema",
    "db_schema",
    "auth_schema"
]


def validate_schema(schema: dict):
    errors = []

    for key in required_keys:
        if key not in schema:
            errors.append(f"Missing key: {key}")

    if "db_schema" in schema:
        tables = schema["db_schema"].get("tables", [])

        if len(tables) == 0:
            errors.append("No database tables found")

    if "api_schema" in schema:
        endpoints = schema["api_schema"].get("endpoints", [])

        if len(endpoints) == 0:
            errors.append("No API endpoints found")

    return errors
