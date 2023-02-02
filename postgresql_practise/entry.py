# -*- coding: utf-8 -*-
from fastapi import FastAPI
from sqlalchemy import create_engine

app = FastAPI()


db_name = "database"  # nosec
db_user = "username"  # nosec
db_pass = "secret"  # nosec
db_host = "playground_db"  # nosec
db_port = "5432"  # nosec

# Connecto to the database
db_string = f"postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"
db = create_engine(db_string)


@app.get("/", responses={404: {"description": "Not Found"}, 503: {}})
async def root():
    return db.execute("SELECT * FROM accounts;").all()


# enter uvicorn entry:app --reload
