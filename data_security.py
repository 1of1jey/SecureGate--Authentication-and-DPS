import os, base64, secrets, hashlib, re
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

def _get_key() -> bytes:
    key_material = os.environ.get("DATA_KEY", "changeme").encode()
    return hashlib.sha256(key_material).digest()

def encrypt(plaintext: str) -> str:
    key = _get_key()
    aes = AESGCM(key)
    nonce = secrets.token_bytes(12)
    ct = aes.encrypt(nonce, plaintext.encode(), None)
    return base64.b64encode(nonce + ct).decode()

def decrypt(ciphertext_b64: str) -> str:
    data = base64.b64decode(ciphertext_b64)
    nonce, ct = data[:12], data[12:]
    aes = AESGCM(_get_key())
    return aes.decrypt(nonce, ct, None).decode()