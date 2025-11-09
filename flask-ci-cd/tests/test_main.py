import json
from app.main import create_app

def test_health():
    client = create_app().test_client()
    resp = client.get("/health")
    assert resp.status_code == 200
    data = json.loads(resp.data)
    assert data["status"] == "ok"

def test_hello():
    client = create_app().test_client()
    resp = client.get("/hello/Tester")
    assert resp.status_code == 200
    data = json.loads(resp.data)
    assert data["message"] == "Hello, Tester!"
