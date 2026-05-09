def repair_schema(schema: dict, errors: list):
    repaired_schema = schema.copy()

    for error in errors:
        if "ui_schema" in error:
            repaired_schema.setdefault("ui_schema", {
                "pages": []
            }
            )

        if "api_schema" in error:
            repaired_schema["api_schema"] = {
                "endpoints": []
            }

        if "db_schema" in error:
            repaired_schema["db_schema"] = {
                "tables": []
            }

        if "auth_schema" in error:
            repaired_schema["auth_schema"] = {
                "roles": []
            }

    return repaired_schema
