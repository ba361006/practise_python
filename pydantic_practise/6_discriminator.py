# -*- coding: utf-8 -*-
from typing import Literal
from typing import Union

from pydantic import BaseModel
from pydantic import Field
from pydantic import ValidationError


class Cat(BaseModel):
    pet_type: Literal["cat"]
    meows: int


class Dog(BaseModel):
    pet_type: Literal["dog"]
    barks: float


class Lizard(BaseModel):
    pet_type: Literal["reptile", "lizard"]
    scales: bool


class Model(BaseModel):
    pet: Union[Cat, Dog, Lizard] = Field(..., discriminator="pet_type")
    n: int


print(Model(pet={"pet_type": "dog", "barks": 3.14}, n=1))
# > pet=Dog(pet_type='dog', barks=3.14) n=1
try:
    Model(pet={"pet_type": "dog"}, n=1)
except ValidationError as e:
    print(e)
    """
    1 validation error for Model
    pet -> Dog -> barks
      field required (type=value_error.missing)
    """
