import logging
import os
from functools import cache

import semver
import toml


@cache
def get_version():
    pyproject_path = os.path.join(os.path.dirname(__file__), "../../pyproject.toml")
    with open(pyproject_path, "r") as f:
        pyproject_data = toml.load(f)
    return pyproject_data["project"]["version"]


_VERSION = get_version()
VERSION = semver.Version.parse(_VERSION)


LOGGING_LEVEL: int = logging.INFO
DATABASE_URL = "sqlite:///test.db"

SWAGGER_TAGS = [
    {
        "name": "Chat",
        "description": "Get help messages from the chatbot",
    },
]
