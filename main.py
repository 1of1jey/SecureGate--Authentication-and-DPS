import os, secrets, base64
import pytop
from itsdangerous import TimestampSigner, BadSignature, SignatureExpired

signer = TimestampSigner(os.environ.get("MAGIC_KEY", "supersecret"))

#MAGIC LINKS TO BE USED
def create_a_magic_token(email:str) -> str:
    payload = f"{email}:{secrets.token_urlsafe(32)}"
