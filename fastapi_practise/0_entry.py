from subprocess import SubprocessError
from fastapi import FastAPI
from fastapi import HTTPException
app = FastAPI()


@app.get("/",responses={404: {"description": "Not Found"}, 503: {}})
async def root():
    try:
        raise SubprocessError("bitch")
    except ValueError as err:
        raise HTTPException(status_code=503, detail="some shit happened") from err
    finally:
        print("do shit")
    return {"message": "Hello World"}

# enter python3 -m uvicorn fastapi_practise.0_entry:app --reload