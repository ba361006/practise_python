# -*- coding: utf-8 -*-
import enum
from typing import List
from typing import Literal
from typing import Union

import pydantic
from fastapi import FastAPI
from typing_extensions import Annotated


class Provider(str, enum.Enum):
    KVM = "kvm"
    Vmware = "vmware"


class Id(pydantic.BaseModel):
    id: int

    class Config:
        extra = "forbid"


class VmwareDefaults(Id):
    datastore: str


class KVMRequest(pydantic.BaseModel):
    provider: Literal[Provider.KVM]
    data: List[Id]

    @pydantic.validator("data")
    def validate_empty_data(cls, data: List[Id]) -> None:
        if len(data) < 1:
            raise ValueError(
                "at least one hypervisor is required to create a hypervisor group"
            )
        return data


class VmwareRequest(pydantic.BaseModel):
    provider: Literal[Provider.Vmware]
    data: List[VmwareDefaults]

    @pydantic.validator("data")
    def validate_empty_data(cls, data: List[Id]) -> None:
        if len(data) < 1:
            raise ValueError(
                "at least one hypervisor is required to create a hypervisor group"
            )
        return data


RequestType = Annotated[
    Union[KVMRequest, VmwareRequest], pydantic.Field(..., discriminator="provider")
]

app = FastAPI()


@app.post("/")
def root(req: RequestType) -> str:
    print(req.__class__)
    for i in req.data:
        print(i)
    return "Hello"


# python3 -m uvicorn fastapi_practise.8_type_annotated:app --reload

"""
# should validate empty
vmware_ok = {"provider":"vmware", "data":[{"id":1, "datastore":"hello"}]}
vmware_mixed = {"provider":"vmware", "data":[{"id":1}, {"id":1, "datastore":"hello"}]}
vmware_wrong_key = {"provider":"vmware", "data":[{"id":1, "datastore1111":"hello"}]}
vmware_empty = {"provider":"vmware", "data":[]}

# should validate kvm mixed
# should validate empty
kvm_ok = {"provider":"kvm", "data":[{"id":1}]}
kvm_mixed = {"provider":"kvm", "data":[{"id":1}, {"id":1, "datastore":"hello"}]}
kvm_wrong_key = {"provider":"kvm", "data":[{"id123":1]}
kvm_empty = {"provider":"kvm", "data":[]}
"""
