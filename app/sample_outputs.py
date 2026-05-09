sample_intent = {
    "app_name": "CRM",
    "features": [
        "login",
        "dashboard",
        "contacts"
    ],
    "roles": [
        "admin",
        "user"
    ]
}


sample_design = {
    "entities": [
        "users",
        "contacts"
    ],
    "flows": [
        "login_flow",
        "contact_management"
    ],
    "permissions": {
        "admin": [
            "view_dashboard",
            "manage_contacts"
        ],
        "user": [
            "view_contacts"
        ]
    }
}
