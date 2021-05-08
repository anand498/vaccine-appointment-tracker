from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
# from app.config import app_config 

SQLALCHEMY_DATABASE_URL='postgresql://postgres:1234@localhost/postgres'

engine=create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base= declarative_base()