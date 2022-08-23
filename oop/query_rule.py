from __future__ import annotations

import logging
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple, Type, cast

from fastapi import Request
from sqlalchemy import Column, asc, desc
from sqlalchemy.orm import Query


APPLOG = logging.getLogger(__name__)


class ModelBaseFilter(ABC):

    field: Column[Any]

    def __init__(self, value: Any) -> None:
        self.value: Any = self.get_field().type.python_type(value)

    @abstractmethod
    def apply(self, query: Query[Any]) -> Query[Any]:
        raise NotImplementedError(f"Method in {self.__class__.__name__} not implemented: apply")

    @classmethod
    def new_class(cls, field: Column[Any]) -> Type[ModelBaseFilter]:
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


class FilterLike(ModelBaseFilter):
    def apply(self, query: Query[Any]) -> Query[Any]:
        return query.filter(self.get_field().ilike(f"%{self.value}%"))


class FilterEqual(ModelBaseFilter):
    def apply(self, query: Query[Any]) -> Query[Any]:
        return query.filter(self.get_field() == self.value)


class FilterMinMax(ModelBaseFilter, ABC):
    class _FilterMin(ModelBaseFilter):
        def apply(self, query: Query[Any]) -> Query[Any]:
            return query.filter(self.get_field() >= self.value)

    class _FilterMax(ModelBaseFilter):
        def apply(self, query: Query[Any]) -> Query[Any]:
            return query.filter(self.get_field() <= self.value)

    @classmethod
    def gen_field_mapping(
        cls, field_name: Optional[str] = None
    ) -> Dict[str, Type[ModelBaseFilter]]:
        field_name = cls._get_field_name(field_name)
        return {
            "min_" + field_name: cls._FilterMin.new_class(cls.get_field()),
            "max_" + field_name: cls._FilterMax.new_class(cls.get_field()),
        }


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


class Sorter:
    def __init__(self) -> None:
        self.sorter_list: List[Tuple[Column[Any], SortDirection]] = []

    def add(self, field: Column[Any], direction: SortDirection) -> None:
        self.sorter_list.append((field, direction))

    def apply(self, query: Query[Any]) -> Query[Any]:
        for field, direction in self.sorter_list:
            if direction == SortDirection.DESC:
                query = query.order_by(desc(field))
            else:
                query = query.order_by(asc(field))
        return query

    @classmethod
    def parse(
        cls, fields: Dict[str, Column[Any]], query_params: Dict[str, str]
    ) -> Tuple[Sorter, Dict[str, str]]:
        sorts = cls()
        sort_str = query_params.get(Sorts.sort)
        field_strs = sort_str.split(",") if sort_str else []
        dir_str = query_params.get(Sorts.sort_direction)
        dir_strs = dir_str.split(",") if dir_str else []
        if sort_str is not None:
            query_params.pop(Sorts.sort)
        if dir_str is not None:
            query_params.pop(Sorts.sort_direction)
        for i, field_strs in enumerate(field_strs):  # type: ignore
            field = fields[field_strs]  # type: ignore
            dir_str = dir_strs[i] if i < len(dir_strs) else Sorts.asc
            sorts.add(field, SortDirection(dir_str))

        return sorts, query_params


@dataclass
class PaginationResult:
    page_number: int
    page_size: int
    num_pages: int
    total_results: int


class FilterPagination:
    def __init__(
        self,
        page_size: Optional[int] = None,
        page_number: Optional[int] = None,
    ) -> None:
        self.page_size = page_size
        self.page_number = page_number

    def apply(self, query: Query[Any]) -> Tuple[Query[Any], PaginationResult]:
        total_results = query.count()
        if self.page_size is not None:
            if self.page_size < 0:
                raise BadRequestException(
                    detail=f"Page size should not be negative: {self.page_size}"
                )
            query = query.limit(self.page_size)
        if self.page_size is None or (self.page_size > total_results > 0):
            self.page_size = total_results

        if self.page_number is not None:
            if self.page_number < 1:
                raise BadRequestException(
                    detail=f"Page number should not be negative: {self.page_number}"
                )
            query = query.offset((self.page_number - 1) * self.page_size)

        if self.page_number is None:
            self.page_number = 1

        num_pages = calculate_num_pages(self.page_size, total_results)
        return query, PaginationResult(self.page_number, self.page_size, num_pages, total_results)

    @classmethod
    def parse(cls, query_params: Dict[str, str]) -> Tuple[FilterPagination, Dict[str, str]]:
        page = query_params.get(Pagination.page)
        page_size = query_params.get(Pagination.page_size)
        _all = query_params.get(Pagination.all)

        if page:
            query_params.pop(Pagination.page)
        if page_size:
            query_params.pop(Pagination.page_size)
        if _all:
            query_params.pop(Pagination.all)
            if _all.lower() == "true":
                return FilterPagination(), query_params

        if page and page_size:
            return FilterPagination(page_number=int(page), page_size=int(page_size)), query_params
        return FilterPagination(), query_params


class QueryRule:
    fields: Dict[str, Column[Any]] = {}
    query_fields: Dict[str, Type[ModelBaseFilter]] = {}

    def __init_subclass__(cls) -> None:
        for name, value in vars(cls).items():
            if isinstance(value, ModelBaseFilter.__class__):  # type: ignore
                cls.fields[name] = value.get_field()
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
        req_params: Dict[str, str] = dict(req.query_params.multi_items())
        filters, req_params = Filters.parse(cls.query_fields, req_params)
        sorters, req_params = Sorter.parse(cls.fields, req_params)
        pagination, req_params = FilterPagination.parse(req_params)
        # if req_params still have context remaining after parsing it means the query keyword
        # is not in the defined whitelist, should return empty list
        should_return_empty_list = bool(req_params)
        return QueryRule(filters, sorters, pagination, should_return_empty_list)
