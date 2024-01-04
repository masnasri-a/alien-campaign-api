from fastapi import APIRouter
from model.campaign import CreateCampaign
from service import campaign

app = APIRouter()

@app.post("/create")
def create(model: CreateCampaign):
    return campaign.create_campaign(model)

@app.put("/edit")
def edit(id_campaign: str, model: CreateCampaign):
    return campaign.edit_campaign(id_campaign, model)