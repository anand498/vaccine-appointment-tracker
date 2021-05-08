import os
# import numpy as np
from datetime import datetime
from app.config.dbconfig import SessionLocal
from fastapi.responses import JSONResponse
from fastapi import status
import requests





def get_db():
    db = None
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def jsonresponse(reasonCode,status,reasonText,responseObject,totalRecords,responseListObject):
    json={
        "reasonCode":reasonCode,
        "status":status,
        "reasonText":reasonText,
        "responseObject":responseObject,
        "totalRecords":totalRecords,
        "responseListObject":responseListObject
    }
    return json

serviceurl="https://cdn-api.co-vin.in/api"
headerdata={ "accept": "application/json", "Content-type":"application/json"}


def generateotp(mobilenumber):
    """
    to get otp for mobile
    """
    apiresponse=requests.post(serviceurl+'/v2/auth/public/generateOTP',
    headers=headerdata,
    json={
        "mobile": str(mobilenumber)
    })
    apiresponse=apiresponse.json()
    return apiresponse


def getstatelist():
    """
    to get otp for mobile 
    """
    url=serviceurl+'/v2/admin/location/states'
    apiresponse=requests.get(url,headers=headerdata)
    apiresponse=apiresponse.json()
    return apiresponse['states']

def getdistrictsbyid(statecode):
    """
    to get otp for mobile 
    """
    headerdata={"Content-type":"application/json"}
    url=serviceurl+'/v2​/admin​/location​/districts​/{}'.format(statecode)
    print(url)
    apiresponse=requests.get(url,headers=headerdata)
    apiresponse=apiresponse.json()
    print(apiresponse)
    return apiresponse


def getvaccineslotbydistrict(district):
    
    parameters={"Accept-Language": "en_US", "district_id": district,"date": '03-04-2021'}
    url=serviceurl+'/v2/appointment/sessions/public/findByDistrict'
    apiresponse=requests.get( url,headers=headerdata,params=parameters)
    print(apiresponse)
    apiresponse=apiresponse.json()
    return apiresponse


def getvaccineslotbypin(pin,date):
    parameters={"Accept-Language": "en_US",  "pincode": pin,"date": date}
    url=serviceurl+'/v2/appointment/sessions/public/findByPin'
    apiresponse=requests.get(url,headers=headerdata,params=parameters)
    apiresponse=apiresponse.json()
    return apiresponse






def payloadcheck(requestInfo):
        try:
            buid=int(requestInfo.buId)
        except:
            return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,content=jsonresponse("400","fail","BuId is Invalid","","",""))
        
        try:
            subBuId=int(requestInfo.subBuId)
        except:
            return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,content=jsonresponse("400","fail","SubBuId is Invalid","","",""))
        
        try:
            userid=int(requestInfo.userId)
        except:
            return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,content=jsonresponse("400","fail","Userid is Invalid","","",""))
        
        try:
            applicationId=int(requestInfo.applicationId)
        except:
            return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,content=jsonresponse("400","fail","ApplicationId is Invalid","","",""))
        
        if requestInfo.environment is None or requestInfo.environment=="":
            return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,content=jsonresponse("400","fail","Environment is Invalid","","",""))
        
        if requestInfo.userLogin is None or requestInfo.userLogin =="":
            return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,content=jsonresponse("400","fail","UserLogin is Invalid","","",""))
        
     
        if requestInfo.action is None:
            return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,content=jsonresponse("400","fail","Action is Invalid","","",""))
        
        if requestInfo.issuer is None:
            return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,content=jsonresponse("400","fail","Issuer is Invalid","","",""))
        
        if requestInfo.token is None:
            return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,content=jsonresponse("400","fail","Token is Invalid","","",""))
        
        if requestInfo.jtitoken is None:
            return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,content=jsonresponse("400","fail","Token is Invalid","","",""))

        return JSONResponse(status_code=status.HTTP_200_OK,content=jsonresponse("400","fail","Payload Valid","","",""))



