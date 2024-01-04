import traceback
from fastapi.exceptions import HTTPException
from model.auth import LoginModel, RegisterModel
from model.response import ResponseModel
from config import mongo
from bson import ObjectId
from util.response import ResponseResult


def LoginService(model: LoginModel):
    try:
        client, coll = mongo.connect('account')
        result = None
        with client:
            body = {"$and":[{'username': model.username}, {'password': model.password}]}
            result = coll.find_one(body)
            if not result:
                user_response: ResponseModel = {'message':'pengguna tidak ditemukan', 'data': None}
                server_response: ResponseModel = {'message':'user not found', 'data': None}
                raise ResponseResult(401, user_response, server_response)

        del result['password']
        user_response: ResponseModel = {'message':'Berhasil Masuk', 'data':result}
        server_response: ResponseModel = {'message':'OK', 'data':result}
        raise ResponseResult(200, user_response, server_response)

    except HTTPException as e:
        raise e
    except Exception:
        traceback.print_exc()
        user_response: ResponseModel = {'message': 'Server dalam maintance', 'data': None}
        server_response: ResponseModel = {'message': 'Internal Server Error', 'data': None}
        raise ResponseResult(500, user_response, server_response)


def RegisterService(model: RegisterModel):
    try:
        client, coll = mongo.connect('account')
        with client:
            data = coll.find_one({"$or": [{'username': model.username}, {"email": model.email}]})
            if data:
                user_response: ResponseModel = {'message': 'User Telah Register', 'data': None}
                server_response: ResponseModel = {'message': 'Conflict', 'data': None}
                return ResponseResult(409, user_response, server_response)
            else:
                body = {
                    "_id": str(ObjectId()),
                    **model.model_dump()
                }
                coll.insert_one(
                    body
                )
                user_response: ResponseModel = {'message': 'User Berhasil Mendaftar', 'data': None}
                server_response: ResponseModel = {'message': 'OK', 'data': None}
                return ResponseResult(200, user_response, server_response)
    except:
        user_response: ResponseModel = {'message': 'Server dalam maintance', 'data': None}
        server_response: ResponseModel = {'message': 'Internal Server Error', 'data': None}
        return ResponseResult(500, user_response, server_response)
