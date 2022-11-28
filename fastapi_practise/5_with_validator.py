# -*- coding: utf-8 -*-
import fastapi
import pydantic

# python3 -m uvicorn fastapi_practise.5_with_validator:app --reload

app = fastapi.FastAPI()


class UserBase(pydantic.BaseModel):
    username: str


class UserIn(UserBase):
    password: str

    @pydantic.validator("password")
    def password_match(cls, v):
        print("v: ", v)
        raise ValueError("must contain a space")


# if the input data doesn't pass the pydantic.validator
# it will raise an 422 Unprocessable Entity error
@app.get("/", response_model=UserBase)
async def root(user_in: UserIn):
    return user_in
