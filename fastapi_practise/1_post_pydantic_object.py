from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


app = FastAPI()


@app.get("/")
async def create_item(item: Item):
    print("get item: ", item.__class__)
    return item

# python3 -m uvicorn fastapi_practise.1_post_pydantic_object:app --reload