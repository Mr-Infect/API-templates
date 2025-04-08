from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_item():
    res = client.post("/items/", json={"name": "Book", "description": "A test book"})
    assert res.status_code == 200
    assert res.json()["name"] == "Book"

def test_get_items():
    res = client.get("/items/")
    assert res.status_code == 200
    assert isinstance(res.json(), list)

