import json

from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from model import auth
from service.auth import RegisterService, LoginService
from config.redis import connect as redis_connect
from starlette.requests import Request
from fastapi_sso.sso.google import GoogleSSO

app = APIRouter()
CLIENT_ID = "121932817010-7jdgl74ed42lsb78oqd0ps046lnfhlq2.apps.googleusercontent.com"
CLIENT_SECRET = "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"
google_sso = GoogleSSO(CLIENT_ID, CLIENT_SECRET, "http://localhost:9001/auth/google/callback")

@app.post("/login")
def loginRoute(model: auth.LoginModel):
    red = redis_connect(0)
    keys = model.username+":"+model.password
    check = red.get(keys)
    if check:
        raise HTTPException(status_code=200, detail=json.loads(str(check).replace("'",'"')))
    result = LoginService(model)
    if result.status_code == 200:
        red.setex(keys, 3600, str(result.detail))
    return result

@app.post("/register")
def registerRoute(model: auth.RegisterModel):
    return RegisterService(model)

@app.get("/google/login")
async def google_login():
    with google_sso:
        return await google_sso.get_login_redirect()

@app.get("/google/callback")
async def google_callback(request: Request):
    with google_sso:
        user = await google_sso.verify_and_process(request)
    return user

