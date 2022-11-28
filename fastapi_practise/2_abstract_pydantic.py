# -*- coding: utf-8 -*-
from typing import List
from typing import Union

import pydantic
from fastapi import FastAPI


class VMsKVMInterface(pydantic.BaseModel):
    name: str = pydantic.Field(...)
    vlan: int = pydantic.Field(...)


class VMsVmwareInterface(pydantic.BaseModel):
    name: str = pydantic.Field(...)
    portgroup: str = pydantic.Field(...)


class VMsBaseSchema(pydantic.BaseModel):
    vms_base_field: int = pydantic.Field(...)


class VMsKVMPostRequest(VMsBaseSchema):
    interfaces: List[VMsKVMInterface] = pydantic.Field(...)


class VMsVmwarePostRequest(VMsBaseSchema):
    interfaces: List[VMsVmwareInterface] = pydantic.Field(...)


app = FastAPI()


@app.post("/items/")
async def create_item(req: Union[VMsKVMPostRequest, VMsVmwarePostRequest]) -> str:
    print("request: ", req)
    print("kvm: ", isinstance(req.interfaces, VMsKVMInterface))
    print("vmware: ", isinstance(req.interfaces, VMsVmwareInterface))
    print(all([isinstance(interface, VMsKVMInterface) for interface in req.interfaces]))
    return "got ya bitch"
