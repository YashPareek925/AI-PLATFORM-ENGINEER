def generate_schema(system_design: dict):
    db_tables = []

    for entity in system_design["entities"]:
        db_tables.append({
            "table_name": entity,
            "fields": [
                "id",
                "created_at"
            ]
        })

    api_endpoints = []

    for entity in system_design["entities"]:
        api_endpoints.append({
            "endpoint": f"/{entity}",
            "method": "GET"
        })

    ui_pages = [
        "home",
        "dashboard"
    ]

    return {
        "ui_schema": {
            "pages": ui_pages
        },
        "api_schema": {
            "endpoints": api_endpoints
        },
        "db_schema": {
            "tables": db_tables
        },
        "auth_schema": {
            "roles": [
                "admin",
                "user"
            ]
        }
    }
