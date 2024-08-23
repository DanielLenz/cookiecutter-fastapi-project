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

def test_update_user(client: TestClient):
    user = UserCreate(name="Another Test User")
    response = client.post("/v0/users/", json=user.model_dump())
    user_id = response.json()["id"]

    response = client.put(
        f"/v0/users/{user_id}",
        json={"name": "Bob"},
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["name"] == "Bob"
    assert data["id"] == user_id


def test_delete_item(client: TestClient):
    user = UserCreate(name="Another Test User")
    response = client.post("/v0/users/", json=user.model_dump())
    user_id = response.json()["id"]

    response = client.delete(f"/v0/users/{user_id}")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["id"] == user_id
    # Try to get the deleted item
    response = client.get(f"/v0/users/{user_id}")
    assert response.status_code == 404, response.text