# -*- coding: utf-8 -*-
from sqlalchemy import BigInteger
from sqlalchemy import Column
from sqlalchemy import DECIMAL
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_method
from sqlalchemy.ext.hybrid import hybrid_property

Base = declarative_base()


class Sample(Base):  # pylint: disable=too-many-instance-attributes
    __tablename__ = "vms"

    id = Column(BigInteger, primary_key=True, index=True)
    name = Column(String, nullable=False)
    mgmt_ip = Column(String)
    num = Column(DECIMAL(2))

    @hybrid_property
    def lb_addr(self) -> str:
        return "lb_addr"

    @property
    def vm_addr(self) -> str:
        return "vm_addr"
