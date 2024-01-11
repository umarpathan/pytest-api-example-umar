pet = {
    "type": "object",
    "required": ["name", "photoUrls"],
    "properties": {
        "id": {
            "type": "integer"
        },
        "name": {
            "type": "integer"
        },
        "category": {
            "type": "array",
            "properties": {
                "id": {
                    "type": "integer"
                },
                "name": {
                    "type": "string"
                }
            }
        },
        "photoUrls": {
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "tags": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "integer"
                    },
                    "name": {
                        "type": "string"
                    }
                }
            }
        },
        "status": {
            "type": "string",
            "enum": ["available", "pending", "sold"]
        }
    }
}
