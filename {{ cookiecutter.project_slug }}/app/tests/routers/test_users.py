from fastapi.testclient import TestClient

from app.common.interfaces import UserCreate


def test_create_user(client: TestClient):
    user = UserCreate(name="Test User")
    response = client.post("/v0/users/", json=user.model_dump())

    assert response.status_code == 200

    data = response.json()
    assert data["name"] == user.name
    assert "id" in data


def test_get_user(client: TestClient):
    user = UserCreate(name="Another Test User")
    response = client.post("/v0/users/", json=user.model_dump())
    user_id = response.json()["id"]

    response = client.get(f"/v0/users/{user_id}")
    assert response.status_code == 200

    data = response.json()
    assert data["name"] == user.name
    assert data["id"] == user_id
