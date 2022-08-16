from subprocess import SubprocessError
from fastapi import FastAPI
from fastapi import HTTPException
from sqlalchemy import create_engine

app = FastAPI()

db_name = 'database'
db_user = 'username'
db_pass = 'secret'
db_host = 'playground_db'
db_port = '5432'

# Connecto to the database
db_string = f"postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"
db = create_engine(db_string)

@app.get("/",responses={404: {"description": "Not Found"}, 503: {}})
async def root():
    return db.execute("SELECT * FROM accounts;").all()
    

# enter uvicorn entry:app --reload