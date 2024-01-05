import sqlalchemy
from fastapi import FastAPI

app = FastAPI()
db = sqlalchemy(app)

@app.get("/")
def read_root():
    return {"Hello": "World"}