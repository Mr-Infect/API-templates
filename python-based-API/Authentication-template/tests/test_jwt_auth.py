# tests/test_jwt_auth.py
from app.auth.jwt_auth import create_access_token, decode_access_token

def test_jwt_token_lifecycle():
    data = {"sub": "testuser"}
    token = create_access_token(data)
    decoded = decode_access_token(token)
    assert decoded["sub"] == "testuser"
