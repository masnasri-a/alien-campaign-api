from pydantic import BaseModel
from typing import Any

class ResponseModel(BaseModel):
    message: str
    data: Any