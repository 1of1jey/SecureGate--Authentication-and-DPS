##SecureGate Authentication and Data Protection System

SecureGate is a security-focused framework built with FastAPI that provides:

🔐 Passwordless login (magic link authentication)

✅ Optional 2FA (TOTP-based) for stronger security

🧩 Data encryption and decryption using AES-GCM

🕵️‍♂️ Sensitive data masking (like emails)

It is designed to help developers quickly add robust authentication and privacy protection to their systems.

⚙️ Features

Magic link login – eliminates the need for passwords

Two-Factor Authentication (2FA) – TOTP-based one-time codes

AES encryption & decryption – protects sensitive data

Data masking utilities – hides sensitive parts of data before display

In-memory user storage – can be swapped out with a real database

📁 Project Structure
SecureGate--Authentication-and-DPS/
├── main.py              # FastAPI app entrypoint
├── auth_security.py     # Handles authentication (magic links, 2FA)
└── data_security.py     # Handles data encryption, decryption, masking

🚀 Getting Started
1. Install dependencies
pip install fastapi uvicorn pyotp itsdangerous cryptography

2. Set environment variables

Create a .env or set these in your shell:

export MAGIC_KEY="supersecret"     # for signing magic links
export DATA_KEY="changeme"         # for AES encryption key

3. Run the server
uvicorn main:app --reload


Server runs on: http://localhost:8000

🧪 API Endpoints
Endpoint  Method  Description
/login/request  POST  Request a magic login link (provide email in form data)
/login/verify  GET  Verify a magic link token and log in
/mfa/setup  POST  Enable 2FA for a user (returns provisioning URI for authenticator apps)
/mfa/verify  POST  Verify a TOTP 2FA code
/secure/store  POST  Encrypt data
/secure/retrieve  POST  Decrypt data
/mask  GET  Mask an email address
📌 Example Usage

Login:

POST /login/request with email=test@example.com

Open the returned link to verify and log in

2FA:

POST /mfa/setup with email to get a TOTP URI

Scan it in Google Authenticator or Authy

POST /mfa/verify with the code

Data Security:

POST /secure/store with data → get encrypted value

POST /secure/retrieve with that value → get original

⚡️ Roadmap

 Addition of database-backed user storage

 Addition JWT-based session tokens

 Addition of rate limiting and brute-force protection

 Building a front-end UI
