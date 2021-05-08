from app.config.dbconfig import Base
from sqlalchemy import Column, Integer, String, DateTime,BigInteger,Boolean
from pydantic import BaseModel,Field
from datetime import datetime
class VaccineModel(Base):
    __tablename__="vaccine_info"
    vaccine_id=Column(BigInteger,primary_key=True)
    state_name=Column(String(50),nullable=False)
    state_id=Column(String,nullable=False)
    district_id=Column(String,nullable=False)
    district_name=Column(String,nullable=False)
    center_name=Column(String,nullable=False)
    age_limit=Column(String,nullable=False)
    vaccine_name=Column(String,nullable=False)
    number_of_slots=Column(String,nullable=False)
    vaccine_cost=Column(String,nullable=False)
    date=Column(DateTime)

    
