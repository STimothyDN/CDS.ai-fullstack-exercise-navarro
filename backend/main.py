from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pandas as pd
import os

# FastAPI application from example on their website
# https://fastapi.tiangolo.com/#example
app = FastAPI()

# use pathing to get the path to the census.csv file
# this may be different locally vs in docker!
census_path = f"{os.path.join(os.path.dirname(__file__))}/census.csv"

origins = [
    "http://localhost",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# set up postgresql database
Base = declarative_base()

DATABASE_URL = "postgresql://timothyrjs:Tarheel1@localhost/mydb"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

class CensusModel(Base):
    __tablename__ = 'census_data'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    age = Column(Integer)
    education_level = Column(String)
    race = Column(String)
    sex = Column(String)
    over_50k = Column(Integer)
    over_50k_text = Column(String)
    count = Column(Integer)

Base.metadata.create_all(bind=engine)

# load CSV into database
def load_csv_to_db():
    data = pd.read_csv(census_path)
    session = SessionLocal()
    for index, row in data.iterrows():
        entry = CensusModel(age = row['age'], education_level = row['education_level'], race = row['race'], sex = row['sex'], over_50k = row['over_50k'], over_50k_text = row['over_50k_text'], count = row['count'])
        session.add(entry)
    session.commit()
    session.close()

@app.get("/load-csv")
def load_csv_endpoint():
    load_csv_to_db()
    return {"status": "Data loaded succesfully"}

@app.get("/census")
def read_item():
    session = SessionLocal()
    census_data = session.query(CensusModel).all()
    result = [{"age": item.age, "education_level": item.education_level, "race": item.race, "sex": item.sex, "over_50k": item.over_50k, "over_50k_text": item.over_50k_text, "count": item.count} for item in census_data]
    session.close()
    return result

@app.get("/summary-stats")
def get_summary_stats():
    return {}