from pydantic import BaseModel

class CreateCampaign(BaseModel):
    title: str
    description: str
    cover: str
    price: int
    start_at: int
    end_at: int
    social_media: str
    service_type: str
    terms_and_condition: str
    created_by: str

