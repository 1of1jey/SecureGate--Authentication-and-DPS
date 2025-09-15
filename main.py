from fastapi import FastAPI, HTTPException, Request, Form
from fastapi.responses import JSONResponse
from auth_security import create_a_magic_token, verify_magic_token, generate_totp_secret,  get_totp_uri, verify_totp
from data_security import encrypt, decrypt, mask_email

app = FastAPI()

users = {}

app.post("/login/request")
async def request_login(email: str = Form(...)):
    token = create_a_magic_token(email)
    return {"message": "Magic link generated", "link": f"http://localhost:8000/login/verify?token={token}"}

app.get("/login/verify")
async def verify_login(token: str):
    email = verify_magic_token(token)
    if not email:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    # Create the account if it's the first login
    if email not in users:
        users[email] = {"totp_secret": None}
    return {"message": "Logged in successfully", "email": email}

@app.post("/mfa/setup")
async def setup_mfa(email: str = Form(...)):
    if email not in users:
        raise HTTPException(status_code=404, detail="User not found")
    secret = generate_totp_secret()
    users[email]["totp_secret"] = secret
    uri = get_totp_uri(secret, email)
    return {"secret": secret, "provisioning_uri": uri}

@app.post("/mfa/verify")
async def verify_mfa(email: str = Form(...), code: str = Form(...)):
    secret = users.get(email, {}).get("totp_secret")
    if not secret:
        raise HTTPException(status_code=400, detail="No TOTP set up")
    if verify_totp(secret, code):
        return {"message": "2FA success"}
    raise HTTPException(status_code=401, detail="Invalid code")

@app.post("/secure/store")
async def secure_store(data: str = Form(...)):
    encrypted = encrypt(data)
    return {"encrypted": encrypted}

@app.post("/secure/retrieve")
async def secure_retrieve(cipher: str = Form(...)):
    try:
        plain = decrypt(cipher)
        return {"decrypted": plain}
    except Exception:
        raise HTTPException(status_code=400, detail="Decryption failed")


@app.get("/mask")
async def mask(email: str):
    return {"masked": mask_email(email)}
