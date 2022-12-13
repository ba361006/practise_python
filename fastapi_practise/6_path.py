# -*- coding: utf-8 -*-
from fastapi import Body
from fastapi import FastAPI
from fastapi import Path
from fastapi import Query

# enter python3 -m uvicorn fastapi_practise.6_path:app --reload
app = FastAPI()


@app.get("/path/{data}")
async def path(data: int = Path(..., ge=0, le=100)):
    """
    open http://127.0.0.1:8000/path/3 at browser
    /path is the path; /3 is the Path parameter
    thanks to type annotation `: int`,
    read_item will receive item_id as 3 in int, not a string "3",

    Path function provides validation to path parameter and return clear info if error occurs
    """
    print("path: ", data, data.__class__)
    return {"data": data}


@app.get("/query")
async def query(data: str = Query(..., min_length=2, max_length=10)):
    """
    open http://127.0.0.1:8000/query?data=hello at browser
    /query is the path; ? is the query operator; data=1 is the query parameter

    Query function almost the same with Path function,
    it provides validation to query parameter and return clear info if error occurs
    """
    print("query: ", data, data.__class__)
    return {"data": data}
