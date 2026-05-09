def generate_system_design(intent_data: dict):
    entities = []

    if "contacts" in intent_data["features"]:
        entities.append("contacts")

    entities.append("users")

    flows = []

    if "login" in intent_data["features"]:
        flows.append("authentication_flow")

    if "dashboard" in intent_data["features"]:
        flows.append("dashboard_flow")

    permissions = {
        "admin": [
            "create",
            "update",
            "delete"
        ],
        "user": [
            "read"
        ]
    }

    return {
        "entities": entities,
        "flows": flows,
        "permissions": permissions
    }
