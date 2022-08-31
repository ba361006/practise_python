from datetime import datetime, date
from fastapi import FastAPI, Depends, Query
from pydantic import BaseModel, Field, validator
from typing import Generic, Optional, Dict, Any, TypeVar, Union, Type
import enum

# python3 -m uvicorn fastapi_practise.for_test:app --reload

class UnprocessableEntityError(Exception):
    pass

app = FastAPI()

class Keys(str, enum.Enum):
    sort = "sort"
    page = "page"

T = TypeVar("T", bound=enum.Enum)

class CommonParams(Generic[T]): # Use generic to accept different Keys(subnet, hypervisor, vm ...)
    def __init__(self, values: Type[T]):
        # this will be called when instantiating the subnet_params function
        self.values = values

    def __call__(
        self,
        sort: str, # type annotation here will be showed on the openapi
        page: str, # type annotation here will be showed on the openapi
    ):
        # this will be called when api is called
        return (Keys(sort), Keys(page))
        
class ListSubnetParams(BaseModel):
    created_at_after: Union[None, datetime, date]
    created_at_before: Union[None, datetime, date]
    name: Optional[str]
    subnet_cidr: Optional[str]
    start_ip: Optional[str]
    end_ip: Optional[str]
    gateway_ip: Optional[str]
    sort: Optional[str]
    page: Optional[str]     
        
    @validator("created_at_before")
    def check_created_at_before(
        cls,
        v: Optional[datetime],
        values: Dict[str, Any],
    ):
        created_after = values["created_at_after"]
        if created_after and v:
            if isinstance(created_after, datetime):
                created_after = created_after.date()
            if isinstance(v, datetime):
                created_before = v.date()
            else:
                created_before = v
            if created_before < created_after:
                raise UnprocessableEntityError 
        return v
    


def subnet_params(
    created_at_after: Union[None, datetime, date],
    created_at_before: Union[None, datetime, date],
    name: Optional[str] = None,
    subnet_cidr: Optional[str] = None,
    start_ip: Optional[str] = None,
    end_ip: Optional[str] = None,
    gateway_ip: Optional[str] = None,
    params: CommonParams = Depends(CommonParams(Keys))
) -> ListSubnetParams:
    print(params[0], params[1])
    try:
        return ListSubnetParams(
            created_at_after=created_at_after,
            created_at_before=created_at_before,
            name=name,
            subnet_cidr=subnet_cidr,
            start_ip=start_ip,
            end_ip=end_ip,
            gateway_ip=gateway_ip,
            sort=params[0],
            page=params[1],
        )
    except Exception as err:
        raise UnprocessableEntityError from err
    
@app.get(
    "/",
    response_model=ListSubnetParams
)
async def root(req: ListSubnetParams = Depends(subnet_params)):
    """
    openapi will show this
    created_at_after: str
    created_at_before: str
    name: str
    subnet_cidr: str
    start_ip: str
    end_ip: str
    gateway_ip: str
    sort: str
    page: int
    """
    print("created_at_after: ", req.created_at_after)
    print("created_at_before: ", req.created_at_before)
    print("name: ", req.name)
    print("subnet_cidr: ", req.subnet_cidr)
    print("start_ip: ", req.start_ip)
    print("end_ip: ", req.end_ip)
    print("gateway_ip: ", req.gateway_ip)
    return req

