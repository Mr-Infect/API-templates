
### app/auth/oauth_auth.py
from fastapi import APIRouter, Depends, Request
from starlette.responses import RedirectResponse
import httpx

router = APIRouter()

CLIENT_ID = "your-client-id"
CLIENT_SECRET = "your-client-secret"
REDIRECT_URI = "http://localhost:8000/auth/oauth/callback"

@router.get("/auth/oauth/login")
def oauth_login():
    return RedirectResponse(
        f"https://github.com/login/oauth/authorize?client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}"
    )

@router.get("/auth/oauth/callback")
async def oauth_callback(code: str):
    async with httpx.AsyncClient() as client:
        token_res = await client.post(
            "https://github.com/login/oauth/access_token",
            headers={"Accept": "application/json"},
            data={
                "client_id": CLIENT_ID,
                "client_secret": CLIENT_SECRET,
                "code": code,
                "redirect_uri": REDIRECT_URI,
            },
        )
        token_json = token_res.json()
        access_token = token_json.get("access_token")
        user_data = await client.get("https://api.github.com/user", headers={"Authorization": f"token {access_token}"})
        return {"token": access_token, "user": user_data.json()}
