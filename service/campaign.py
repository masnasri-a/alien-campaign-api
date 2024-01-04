import traceback

from model.campaign import CreateCampaign
from config import mongo
from bson import ObjectId
from util.response import ResponseResult


def create_campaign(model: CreateCampaign):
    try:
        client, coll = mongo.connect('campaign')
        with client:
            data = {
                "_id": str(ObjectId()),
                **model.model_dump()
            }
            coll.insert_one(data)
            raise ResponseResult(201, user_response={"message": "Campaign Berhasil Dibuat", "data": data},
                                 server_response={"message": "Created", "data": data})
    except Exception:
        traceback.print_exc()
        raise ResponseResult(500, user_response={"message": "Lagi ada gangguan nih di server :) ", "data": None},
                             server_response={"message": "Internal Server Error", "data": None})


def edit_campaign(id_campaign: str, model: CreateCampaign):
    try:
        client, coll = mongo.connect('campaign')
        with client:
            data = {
                "$set": model.model_dump()
            }
            coll.update_one({"_id": id_campaign}, data)
            raise ResponseResult(200, user_response={"message": "Campaign Berhasil Diubah", "data": data},
                                 server_response={"message": "OK", "data": data})
    except Exception:
        traceback.print_exc()
        raise ResponseResult(500, user_response={"message": "Lagi ada gangguan nih di server :) ", "data": None},
                             server_response={"message": "Internal Server Error", "data": None})
