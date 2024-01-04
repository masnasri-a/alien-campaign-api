from model.response import ResponseModel
from fastapi.exceptions import HTTPException

def ResponseResult(status_code: int, user_response: ResponseModel, server_response: ResponseModel):
    raise HTTPException(status_code=status_code,detail={
        "user_response": user_response,
        "server_response": server_response
    })
