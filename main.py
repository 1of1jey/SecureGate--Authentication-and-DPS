from fastapi import FastAPI, HTTPException, Request, Form
from fastapi.responses import JSONResponse
from auth_security import create_a_magic_token, verify_magic_token, generate_totp_secret
from data_security import