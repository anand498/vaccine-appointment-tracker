from fastapi import FastAPI,Response
import uvicorn
from app.config import app_config 
from app.route import route



app=FastAPI()


app.include_router(route, tags=["Vaccine Tracker"])



    
if __name__=='__main__':
    uvicorn.run("main:app",host=app_config.HOST,port=app_config.PORT,debug=app_config.DEBUGMODE)
