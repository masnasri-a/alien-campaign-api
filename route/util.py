
from service.utils import social_media as social_media_service
from fastapi import APIRouter

app = APIRouter()

@app.get("/social_media")
def social_media():
    return social_media_service()
