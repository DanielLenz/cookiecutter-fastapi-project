import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


@pytest.fixture(autouse=True, scope="module")
def setup_and_teardown():
    pass
    yield
    pass


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "App is running"
