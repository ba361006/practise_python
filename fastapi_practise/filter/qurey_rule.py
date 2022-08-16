from __future__ import annotations
import abc
import typing
import sqlalchemy
import fastapi
from sqlalchemy.orm import Query


class ModelBaseFilter(abc.ABC):
    field: sqlalchemy.Column[typing.Any]
    
    def __init__(self, value: typing.Any) -> None:
        self.value: typing.Any = self.get_field().type.python_type(value)
    
    @abc.abstractmethod
    def apply(self, query: Query[typing.Any]) -> Query[typing.Any]:
        raise NotImplementedError(f"Method in {self.__class__.__name__} not implemented: apply")
    
    @classmethod
    def new_class(cls, field: sqlalchemy.Column[typing.Any]) -> typing.Type[ModelBaseFilter]:
        new_cls = typing.cast(
            typing.Type[ModelBaseFilter],
            type(f"ModelBaseFilter{field}", (cls, object), {})
        )
        new_cls.field = field
        return new_cls

    @classmethod
    def get_field(cls) -> sqlalchemy.Column[typing.Any]:
        return cls.field

    @classmethod
    def _get_field_name(cls, field_name: typing.Optional[str]) -> str:
        if field_name is None:
            return cls.get_field().key
        return field_name

    @classmethod
    def gen_field_mapping(
        cls, field_name: typing.Optional[str] = None
    ) -> typing.Dict[str, typing.Type[ModelBaseFilter]]:
        return {cls._get_field_name(field_name): cls}

class FilterLike(ModelBaseFilter):
    def apply(self, query: Query[typing.Any]) -> Query[typing.Any]:
        print(f"FilterLike get {query}, apply!")

class FilterEqual(ModelBaseFilter):
    def apply(self, query: Query[typing.Any]) -> Query[typing.Any]:
        print(f"FilterEqual get {query}, apply!")

class Filters:
    def __init__(self) -> None:
        self.filters_list: typing.List[ModelBaseFilter] = []

    def add_filter(self, query_filter: ModelBaseFilter) -> None:
        self.filters_list.append(query_filter)
    
    def apply(self, query: Query[typing.Any]) -> Query[typing.Any]:
        for query_filter in self.filters_list:
            query = query_filter.apply(query)
        return query

    @classmethod
    def parse(
        cls, 
        query_fields: typing.Dict[str, typing.Type[ModelBaseFilter]],
        query_params: typing.Dict[str, str]
    ):
        filters = cls()
        for key, filter_cls in query_fields.items():
            value = query_params.get(key)
            if value is not None:
                query_filter = filter_cls(value)
                filters.add_filter(query_filter)
                query_params.pop(key)
        return filters, query_params


class QueryRule:
    fields: typing.Dict[str, sqlalchemy.Column[typing.Any]] = {}
    query_fields: typing.Dict[str, typing.Type[ModelBaseFilter]] = {}
    
    def __init_subclass__(cls) -> None:
        for name, value in vars(cls).items():
            if isinstance(value, ModelBaseFilter.__class__):
                cls.fields[name] = value.get_field()
                cls.query_fields.update(value.gen_field_mapping(name))

    def __init__(
        self,
        filters,
        sorter,
        pagination,
        should_return_empty_list: bool,
    ) -> None:
        self.filters = filters
        self.sorter = sorter
        self.pagination = pagination
        self.should_return_empty: bool = should_return_empty_list
        
    @classmethod
    def parse(cls, req: fastapi.Request):
        req_params: typing.Dict[str, str] = dict(req.query_params.multi_items())
        filters, req_params = Filters.parse(cls.query_fields, req_params)
        filters.apply("query")


