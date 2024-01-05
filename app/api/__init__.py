import sqlalchemy
from fastapi import FastAPI

app = FastAPI()
app.config['SQLALCHEMY_DATABASE_URL'] = "sqlite:///./sql_app.db"
db = sqlalchemy(app)

@app.get("/")
def read_root():
    return {"Hello": "World"}