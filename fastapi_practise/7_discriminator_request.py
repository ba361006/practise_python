# -*- coding: utf-8 -*-
import enum
from typing import List
from typing import Literal
from typing import Union

import pydantic
from fastapi import FastAPI


class PetType(str, enum.Enum):
    cat = "cat"
    dog = "dog"


class CatData(pydantic.BaseModel):
    id: int


class DogData(pydantic.BaseModel):
    name: str


class Cat(pydantic.BaseModel):
    pet_type: Literal[PetType.cat]
    data: List[CatData]


class Dog(pydantic.BaseModel):
    pet_type: Literal[PetType.dog]
    data: List[DogData]


class RequestModel(pydantic.BaseModel):
    pet: Union[Cat, Dog] = pydantic.Field(..., discriminator="pet_type")


app = FastAPI()


@app.get("/", response_model=RequestModel)
def root(req: RequestModel) -> RequestModel:
    pet = req.pet
    print(pet.__class__)
    for i in pet.data:
        print(i)
    return req


# enter python3 -m uvicorn fastapi_practise.7_discriminator_request:app --reload

# postman: Body/raw/json
# {
#     "pet":{
#         "pet_type": "cat",
#         "data": [
#             {"id":1},
#             {"id":2}
#         ]
#     }
# }

# or

# {
#     "pet":{
#         "pet_type": "dog",
#         "data": [
#             {"name":"Zheng"},
#             {"name":"Gao"}
#         ]
#     }
# }
