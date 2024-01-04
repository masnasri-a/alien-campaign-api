import json

from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from model import auth
from service.auth import RegisterService, LoginService
from config.redis import connect as redis_connect

app = APIRouter()

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
