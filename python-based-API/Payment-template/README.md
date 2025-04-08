# 💸 Payment API Template (Python)

A production-ready FastAPI-based payment integration module with Stripe and PayPal support.

## ⚙️ Features
- Create Stripe Checkout sessions
- Create PayPal Orders via REST API
- `.env` configuration for secrets
- Swagger UI and Pytest support

## 🔌 Endpoints
- `/payment/stripe?amount=500` (amount in cents)
- `/payment/paypal?amount=10.00`

## 🔐 .env Setup
```env
STRIPE_SECRET_KEY=sk_test_xxxx
PAYPAL_CLIENT_ID=xxxxx
PAYPAL_CLIENT_SECRET=xxxxx
```

## 🧪 Run Locally
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```
Visit [http://localhost:8000/docs](http://localhost:8000/docs) for Swagger UI
