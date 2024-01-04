from fastapi import APIRouter
from model.campaign import CreateCampaign
from model.base import BasePagination
from service import campaign

app = APIRouter()

@app.post("/create")
def create(model: CreateCampaign):
    return campaign.create_campaign(model)

@app.put("/edit")
def edit(id_campaign: str, model: CreateCampaign):
    return campaign.edit_campaign(id_campaign, model)

@app.get("/list_campaign")
def list_campaign(page: int, limit: int, search: str):
    return campaign.list_campaign(page, limit, search)

@app.get("/detail")
def detail_campaign(id_campaign: str):
    return campaign.get_detail_campaign(id_campaign)