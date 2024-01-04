import time
import traceback

from model.campaign import CreateCampaign
from fastapi.exceptions import HTTPException
from config import mongo
from bson import ObjectId
from util.response import ResponseResult


def create_campaign(model: CreateCampaign):
    try:
        client, coll = mongo.connect('campaign')
        with client:
            data = {
                "_id": str(ObjectId()),
                **model.model_dump(),
                "status":"ACTIVE",
                "created_at": int(time.time()),
                "updated_at": int(time.time())

            }
            coll.insert_one(data)
            raise ResponseResult(201, user_response={"message": "Campaign Berhasil Dibuat", "data": data},
                                 server_response={"message": "Created", "data": data})
    except HTTPException as e:
        return e

    except Exception:
        traceback.print_exc()
        raise ResponseResult(500, user_response={"message": "Lagi ada gangguan nih di server :) ", "data": None},
                             server_response={"message": "Internal Server Error", "data": None})



def edit_campaign(id_campaign: str, model: CreateCampaign):
    try:
        client, coll = mongo.connect('campaign')
        with client:
            data = {
                "$set": {
                    **model.model_dump(),
                    "updated_at": int(time.time())
                }
            }
            coll.update_one({"_id": id_campaign}, data)
            raise ResponseResult(200, user_response={"message": "Campaign Berhasil Diubah", "data": data},
                                 server_response={"message": "OK", "data": data})
    except HTTPException as e:
        return e
    except Exception:
        traceback.print_exc()
        raise ResponseResult(500, user_response={"message": "Lagi ada gangguan nih di server :) ", "data": None},
                             server_response={"message": "Internal Server Error", "data": None})

def delete_campaign(id_campaign):
    try:
        client, coll = mongo.connect('campaign')
        with client:
            data = {"$set":{"status":"DELETED","updated_at": int(time.time())}}
            coll.update_one({"_id":id_campaign}, data)
            raise ResponseResult(200, user_response={"message": "Campaign Berhasil Dihapus", "data": data},
                         server_response={"message": "OK", "data": data})
    except HTTPException as e:
        return e
    except Exception:
        traceback.print_exc()
        raise ResponseResult(500, user_response={"message": "Lagi ada gangguan nih di server :) ", "data": None},
                             server_response={"message": "Internal Server Error", "data": None})


