from datetime import datetime
from app.Vaccination.utils import *
from fastapi import status
from fastapi.responses import JSONResponse
from app.Vaccination import model
import urllib.request
from sqlalchemy import exc
from app.Vaccination.utils import getstatelist
import urllib.request, json
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from time import sleep
from app.Vaccination.model import VaccineModel
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session




def updatedata(db):   
    statelist=getstatelist()
    
    for state in statelist:
        with urllib.request.urlopen("https://cdn-api.co-vin.in/api/v2/admin/location/districts/{}".format(str(state['state_id']))) as url:
            data = json.loads(url.read().decode())
        data=data['districts']
        
        for district in data:
            district_id=district['district_id']
            data=getvaccineslotbydistrict(district_id)['sessions']
            for session in data:
                db_user = model.VaccineModel(
                state_id=state['state_id'],
                state_name=state['state_name'],
                district_id=district['district_id'],
                district_name=district['district_name'],
                center_name=session['name'],
                age_limit=session['min_age_limit'],
                vaccine_name=session['vaccine'],
                number_of_slots=session['available_capacity'],
                vaccine_cost=session['fee_type'],
                date=session['date']
                )
                db.add(db_user)
    # try: 
        db.commit()
        # except exc.IntegrityError:
        #     return JSONResponse(status_code=status.HTTP_404_NOT_FOUND,content=jsonresponse("404",'fail','Data error','','',''))
    
    return JSONResponse( status_code=status.HTTP_201_CREATED,content=jsonresponse("200",'success','Database has been registered','','',''))






