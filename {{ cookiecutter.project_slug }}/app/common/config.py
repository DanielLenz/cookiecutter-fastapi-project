import logging

import semver

_VERSION: str = "0.1.0"
VERSION = semver.Version.parse(_VERSION)


LOGGING_LEVEL: int = logging.INFO

SWAGGER_TAGS = [
    {
        "name": "Chat",
        "description": "Get help messages from the chatbot",
    },
]
