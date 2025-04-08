import os
import requests
from dotenv import load_dotenv
from fastapi import HTTPException

load_dotenv()

CLIENT_ID = os.getenv("PAYPAL_CLIENT_ID")
CLIENT_SECRET = os.getenv("PAYPAL_CLIENT_SECRET")
BASE_URL = "https://api-m.sandbox.paypal.com"


def get_paypal_access_token():
    auth_response = requests.post(
        f"{BASE_URL}/v1/oauth2/token",
        headers={"Accept": "application/json"},
        auth=(CLIENT_ID, CLIENT_SECRET),
        data={"grant_type": "client_credentials"},
    )
    if auth_response.status_code != 200:
        raise HTTPException(status_code=401, detail="PayPal auth failed")
    return auth_response.json()["access_token"]

def create_paypal_order(amount: str):
    token = get_paypal_access_token()
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    order_data = {
        "intent": "CAPTURE",
        "purchase_units": [{"amount": {"currency_code": "USD", "value": amount}}],
        "application_context": {
            "return_url": "http://localhost:8000/success",
            "cancel_url": "http://localhost:8000/cancel"
        }
    }
    response = requests.post(f"{BASE_URL}/v2/checkout/orders", json=order_data, headers=headers)
    if response.status_code != 201:
        raise HTTPException(status_code=500, detail="PayPal order creation failed")
    return response.json()
