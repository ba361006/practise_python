from __future__ import annotations

import logging
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple, Type, cast

from fastapi import Request
from sqlalchemy import Column, asc, desc
from sqlalchemy.orm import Query


class ModelBaseFilter(ABC):

    field: Column[Any]

    def __init__(self, value: Any) -> None:
        self.value: Any = self.get_field().type.python_type(value)

    @abstractmethod
    def apply(self, query: Query[Any]) -> Query[Any]:
        raise NotImplementedError(f"Method in {self.__class__.__name__} not implemented: apply")

    @classmethod
    def new_class(cls, field: Column[Any]) -> Type[ModelBaseFilter]:
        """
        make a new class with the given field
        """
        # type(__object_name__, __bases__, __dict__)
        # type with three arguments will assign the given arguments to cooresponding attributes
        # and return a new type object (class)
        
        # cast(type, value)
        # cast will cast the given type's attributes to the value, but the attributes provided by
        # the type is only for preview, it have no actually effect and will raise an error if it's invoked
        new_cls = cast(Type[ModelBaseFilter], type(f"ModelBaseFilter{field}", (cls, object), {}))
        new_cls.field = field
        return new_cls

    # work around for SqlAlchemy Column
    @classmethod
    def get_field(cls) -> Column[Any]:
        return cls.field

    @classmethod
    def _get_field_name(cls, field_name: Optional[str]) -> str:
        if field_name is None:
            return cls.get_field().key
        return field_name

    @classmethod
    def gen_field_mapping(
        cls, field_name: Optional[str] = None
    ) -> Dict[str, Type[ModelBaseFilter]]:
        return {cls._get_field_name(field_name): cls}


class Filters:
    def __init__(self) -> None:
        self.filters_list: List[ModelBaseFilter] = []

    def add_filter(self, query_filter: ModelBaseFilter) -> None:
        self.filters_list.append(query_filter)

    def apply(self, query: Query[Any]) -> Query[Any]:
        for query_filter in self.filters_list:
            query = query_filter.apply(query)
        return query

    @classmethod
    def parse(
        cls, query_fields: Dict[str, Type[ModelBaseFilter]], query_params: Dict[str, str]
    ) -> Tuple[Filters, Dict[str, str]]:
        filters = cls()
        for key, filter_cls in query_fields.items():
            value = query_params.get(key)
            if value is not None:
                query_filter = filter_cls(value)
                filters.add_filter(query_filter)
                query_params.pop(key)
        return filters, query_params



class FilterLike(ModelBaseFilter):
    def apply(self, query: Query[Any]) -> Query[Any]:
        return query.filter(self.get_field().ilike(f"%{self.value}%"))



class QueryRule:
    # fields: {fielname: value of field name for specific Rule}
    fields: Dict[str, Column[Any]] = {}
    
    # query_fields: {fieldname: ModelBaseFilterFIELDNAME}
    query_fields: Dict[str, Type[ModelBaseFilter]] = {}

    def __init_subclass__(cls) -> None:
        """
        separate the fields and query_fields in HypervisorRule into two different dicts
        """
        # vars will return argument's __dict__(fields name and value)
        for name, value in vars(cls).items():
            
            # value has inherited from ModelBaseFilter when casting type[ModelBaseFilter]
            # so only the casted fields will be added to query_fields
            if isinstance(value, ModelBaseFilter.__class__):  # type: ignore
                # get field name of the value
                cls.fields[name] = value.get_field()

                # update {fieldname: ModelBaseFilterFIELDNAME} to query_fields
                cls.query_fields.update(value.gen_field_mapping(name))

    def __init__(
        self,
        filters: Filters,
        sorter: Sorter,
        pagination: FilterPagination,
        should_return_empty_list: bool,
    ) -> None:
        self.filters = filters
        self.sorter = sorter
        self.pagination = pagination
        self.should_return_empty: bool = should_return_empty_list

    @classmethod
    def parse(cls, req: Request) -> QueryRule:
        req_params: Dict[str, str] = req
        # req_params: Dict[str, str] = dict(req.query_params.multi_items())
        filters, req_params = Filters.parse(cls.query_fields, req_params)
        sorters, req_params = Sorter.parse(cls.fields, req_params)
        pagination, req_params = FilterPagination.parse(req_params)
        # if req_params still have context remaining after parsing it means the query keyword
        # is not in the defined whitelist, should return empty list
        should_return_empty_list = bool(req_params)
        return QueryRule(filters, sorters, pagination, should_return_empty_list)

import sqlalchemy
class Hypervisor:
    hostname = sqlalchemy.Column("hypervisor_hostname")

class HypervisorRule(QueryRule):
    # pylint: disable=too-many-instance-attributes
    hostname = FilterLike.new_class(Hypervisor.hostname)
    # mgmt_ip = FilterEqual.new_class(Hypervisor.mgmt_ip)
    # virtualization_provider = FilterEqual.new_class(Hypervisor.virtualization_provider)
    # provisioned_status = FilterEqual.new_class(Hypervisor.provisioned_status)
    # os_state = FilterEqual.new_class(Hypervisor.os_state)
    # total_vcpus = FilterMinMax.new_class(Hypervisor.total_vcpus)
    # total_memory = FilterMinMax.new_class(Hypervisor.total_memory)

resquest = {"hostname": "resquest_hostname"}

HypervisorRule.parse(resquest)