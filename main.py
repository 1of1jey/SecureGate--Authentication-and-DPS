from fastapi import FastAPI, HTTPException, Request, Form
from fastapi.responses import JSONResponse
from auth_security import create_a_magic_token, verify_magic_token, generate_totp_secret,  get_totp_uri, verify_totp
from data_security import encrypt, decrypt, mask_email

app = FastAPI()

users = {}

app.post("/login/request")
async def request_login(email: str = form(...)):
    token = create_a_magic_token()
    return {"message": "Magic link generated", "link": f"http://localhost:8000/login/verify?token={token}"}

app.get("/login/verify")
async def verify_login(token: str):
    email = verify_magic_token(token)
    if not email:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    # Create account if first login
    if email not in users:
        users[email] = {"totp_secret": None}
    return {"message": "Logged in successfully", "email": email}

