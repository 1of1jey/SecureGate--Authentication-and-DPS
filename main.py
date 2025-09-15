import os, secrets, base64
import pytop
from itsdangerous import TimestampSigner, BadSignature, SignatureExpired

signer = TimestampSigner(os.environ.get("MAGIC_KEY", "supersecret"))
