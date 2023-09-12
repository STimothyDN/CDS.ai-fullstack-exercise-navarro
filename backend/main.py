from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import os

# FastAPI application from example on their website
# https://fastapi.tiangolo.com/#example
app = FastAPI()

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

@app.get("/census")
def read_item():
    
    # use pathing to get the path to the census.csv file
    # this may be different locally vs in docker!
    census_path = f"{os.path.join(os.path.dirname(__file__))}/census.csv"
    
    # read CSV file using pandas
    # https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html
    census_csv = pd.read_csv(census_path)

    # convert to dict so that we return json to the frontend
    # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_dict.html
    census_csv = census_csv.to_dict(orient="records")
    
    # return to frontend
    return census_csv

@app.get("/summary-stats")
def get_summary_stats():
    return {}