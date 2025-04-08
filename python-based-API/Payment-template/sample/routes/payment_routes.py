from fastapi import APIRouter, Query
from app.payments.stripe_payments import create_checkout_session
from app.payments.paypal_payments import create_paypal_order

router = APIRouter()

@router.get("/payment/stripe")
def create_stripe_link(amount: int = Query(..., description="Amount in cents")):
    return {"checkout_url": create_checkout_session(amount)}

@router.get("/payment/paypal")
def create_paypal_link(amount: float = Query(...)):
    return create_paypal_order(str(amount))
