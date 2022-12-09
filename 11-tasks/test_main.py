from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_all_posts():
    response = client.get("/blog/all")
    assert response.status_code == 200
