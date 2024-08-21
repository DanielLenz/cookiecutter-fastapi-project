import logging

import semver

_VERSION: str = "0.1.0"
VERSION = semver.Version.parse(_VERSION)


LOGGING_LEVEL: int = logging.INFO
DATABASE_URL = "sqlite:///test.db"

SWAGGER_TAGS = [
    {
        "name": "Chat",
        "description": "Get help messages from the chatbot",
    },
]
