import stripe
import os
from dotenv import load_dotenv
from fastapi import HTTPException

load_dotenv()
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

DOMAIN = "http://localhost:8000"

def create_checkout_session(amount_cents: int, currency="usd"):
    try:
        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[{
                "price_data": {
                    "currency": currency,
                    "product_data": {
                        "name": "Custom Payment"
                    },
                    "unit_amount": amount_cents,
                },
                "quantity": 1
            }],
            mode="payment",
            success_url=f"{DOMAIN}/success",
            cancel_url=f"{DOMAIN}/cancel",
        )
        return session.url
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
