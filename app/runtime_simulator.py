def simulate_runtime(schema: dict):
    result = {
        "valid": True,
        "issues": []
    }

    endpoints = schema.get("api_schema", {}).get("endpoints", [])

    if len(endpoints) == 0:
        result["valid"] = False
        result["issues"].append("No endpoints available")

    return result
