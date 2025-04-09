# 📬 Webhook API Template (Python)

Receive and verify webhook events from external services like GitHub, Stripe, or PayPal.

## ✅ Features
- Signature verification using HMAC SHA-256
- SQLite storage of all events
- FastAPI routing and validation
- Postman + Pytest test cases

## 📦 Endpoints
- `POST /webhook/` — Receives and logs event with signature check

## 📄 Headers
- `X-Signature: hmac-sha256-encoded`

## 🔐 .env Setup
```env
WEBHOOK_SECRET=supersecretwebhookkey
```

## 🧪 Run Locally
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```
Go to [http://localhost:8000/docs](http://localhost:8000/docs)
