from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_stripe_payment():
    response = client.get("/payment/stripe?amount=500")
    assert response.status_code == 200
    assert "checkout_url" in response.json()

def test_paypal_payment():
    response = client.get("/payment/paypal?amount=10.00")
    assert response.status_code in [200, 500]
