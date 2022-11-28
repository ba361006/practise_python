# -*- coding: utf-8 -*-
import fastapi
import pydantic

# python3 -m uvicorn fastapi_practise.4_response_model:app --reload

app = fastapi.FastAPI()


class UserBase(pydantic.BaseModel):
    username: str


class UserIn(UserBase):
    password: str


# response example on openapi will only show username(but actually it
# still returns both username and password)
@app.get("/", response_model=UserBase)
async def root(user_in: UserIn):
    return user_in
