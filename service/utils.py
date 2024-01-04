from config.redis import connect as redis_connect
from config.mongo import connect as mongo_connect
import json
from util.response import ResponseResult
import traceback
from fastapi.exceptions import HTTPException

def social_media():
    try:
        red = redis_connect(1)
        response = red.get('social_media')
        if response:
            results = str(response).replace("'",'"')
            results = json.loads(results)
            raise ResponseResult(200, user_response={'message': 'data ditemukan', 'data': results},
                              server_response={'message': 'OK', 'data': results})

        client, coll = mongo_connect('social_media')
        with client:
            data = coll.find()
            result = []
            if data:
                for item in data:
                    print(item)
                    del item['_id']
                    result.append(item)
                red.setex('social_media', 3600, str(result))
                raise ResponseResult(200, user_response={'message':'data ditemukan', 'data':result}, server_response={'message':'OK', 'data':result})
            else:
                raise ResponseResult(404, user_response={'message':'data tidak ditemukan', 'data':None}, server_response={'message':'Not Found', 'data':None})
    except HTTPException as e:
        return e
    except Exception:
        traceback.print_exc()
        raise ResponseResult(500, user_response={'message': 'ada gangguan nih', 'data': None},
                             server_response={'message': 'Internal Server Error', 'data': None})