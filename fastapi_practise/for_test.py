from typing import Optional
import fastapi

# python3 -m uvicorn fastapi_practise.for_test:app --reload

app = fastapi.FastAPI()

@app.get("/")
async def root():
    return {"message": "nothing"}

