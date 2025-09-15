import os, secrets, base64
import pytop
from itsdangerous import TimestampSigner, BadSignature, SignatureExpired

signer = TimestampSigner(os.environ.get("MAGIC_KEY", "supersecret"))

#MAGIC LINKS TO BE USED
def create_a_magic_token(email:str) -> str:
    user = f"{email}:{secrets.token_urlsafe(32)}"
    return signer.sign(user)

def verify_magic_token(token: str, max_age=900) -> str | None:
    try:
        raw_info = signer.unsign(token, max_age=max_age)
        email, _ =raw.split(":", 1)
        return email
    except (SignatureExpired: