from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends, Request
from fastapi.responses import JSONResponse
from app.Vaccination.utils import get_db,jsonresponse
from app.config import schemas
from app.Vaccination.cowin import updatedata
from fastapi.templating import Jinja2Templates
from app.Vaccination.model import VaccineModel
route = APIRouter(prefix="/cowin")

templates = Jinja2Templates(directory="app/templates")



@route.get("/")
async def homepage(request: Request,state= None,district=None,Vaccine_Cost=None,Above_45=None,db:Session=Depends(get_db)):
    vaccineslots = db.query(VaccineModel)
    if state:
        vaccineslots = vaccineslots.filter(VaccineModel.state_name == state)
    if district:
        vaccineslots = vaccineslots.filter(VaccineModel.district_name == district)
    if Vaccine_Cost:
        vaccineslots = vaccineslots.filter(VaccineModel.vaccine_cost == 'Free')
    if Above_45:
        vaccineslots = vaccineslots.filter(VaccineModel.age_limit =='18')

    vaccineslots = vaccineslots.all()
    return templates.TemplateResponse("home.html", {
        "request": request, 
        "state": state,
        "district": district,
        "Vaccine_Cost":Vaccine_Cost,
        "Above_45":Above_45,
        "vaccineslots": vaccineslots
    })



@route.get("/_updatedata")
async def getuserPhrase(db:Session=Depends(get_db)):
    response=updatedata(db)
    return response







