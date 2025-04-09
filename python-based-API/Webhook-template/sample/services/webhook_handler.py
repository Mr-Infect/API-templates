import hmac
import hashlib
import os
from fastapi import HTTPException, Request
from dotenv import load_dotenv
load_dotenv()

SECRET = os.getenv("WEBHOOK_SECRET", "defaultsecret")


def verify_signature(request: Request, body: bytes):
    received_sig = request.headers.get("X-Signature")
    if not received_sig:
        raise HTTPException(status_code=400, detail="Missing signature header")

    computed_sig = hmac.new(SECRET.encode(), body, hashlib.sha256).hexdigest()
    if not hmac.compare_digest(received_sig, computed_sig):
        raise HTTPException(status_code=403, detail="Invalid signature")

    return True
