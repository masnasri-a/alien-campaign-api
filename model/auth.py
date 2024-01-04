from pydantic import BaseModel, field_validator
from util.security import hash_string


class LoginModel(BaseModel):
    username: str
    password: str

    @field_validator('password')
    def validate(cls, value):
        return hash_string(value)


class RegisterModel(BaseModel):
    username: str
    email: str
    phone_number: str
    password: str

    @field_validator('password')
    def validate(cls, value):
        return hash_string(value)
