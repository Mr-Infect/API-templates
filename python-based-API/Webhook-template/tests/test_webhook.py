from fastapi.testclient import TestClient
from app.main import app
import hmac
import hashlib

client = TestClient(app)

SECRET = "supersecretwebhookkey"

def generate_signature(body):
    return hmac.new(SECRET.encode(), body.encode(), hashlib.sha256).hexdigest()

def test_webhook_receiver():
    payload = '{"source": "GitHub", "type": "push"}'
    sig = generate_signature(payload)
    response = client.post(
        "/webhook/",
        headers={"X-Signature": sig, "Content-Type": "application/json"},
        data=payload
    )
    assert response.status_code == 200
    assert response.json()["status"] == "received"
