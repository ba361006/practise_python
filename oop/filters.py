import json
import logging
from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum
from typing import Any, NamedTuple, Optional, Tuple, Type

from cso.api.common import CommonQuery
from cso.db.database import Base
from sqlalchemy import Column, String, desc
from sqlalchemy.exc import DataError, ProgrammingError
from sqlalchemy.orm import Query
from sqlalchemy_filters import (apply_filters,  # type: ignore
                                apply_pagination, apply_sort)

APPLOG = logging.getLogger(__name__)


class Pagination(NamedTuple):
    page_number: int
    page_size: int
    num_pages: int
    total_results: int


def apply_cso_filters(
    db_query: Any,
    base_model: Type[Base],
    query_modifiers: Optional[CommonQuery] = None,
    default_sort_column: Any = "id",
) -> Tuple[Any, Pagination]:
    # pylint: disable=too-many-branches,too-many-locals
    # This ensures the Enums nested in the `CommonQuerySchema` come back as strings.
    pagination_spec = {}
    if not query_modifiers:
        db_query, pagination = apply_pagination(db_query)
        return db_query, pagination

    query_modifiers_dict = json.loads(query_modifiers.json())

    filter_spec = query_modifiers_dict["filters"]
    if filter_spec:
        for i, spec in enumerate(filter_spec):
            column_name = spec["field"]
            query_value = spec["value"]
            column = base_model.__dict__.get(column_name)
            column_type = column.type if column is not None else None

            if isinstance(column_type, String) and not isinstance(query_value, str):
                filter_spec[i]["value"] = str(query_value)

            if filter_spec[i]["op"] == "like" and not isinstance(column_type, String):
                APPLOG.warning(
                    "The query with 'LIKE' operator only support column type of string: "
                    "%s type of %s was selected.",
                    column_name,
                    column_type,
                )
                filter_spec[i]["op"] = "eq"

            if filter_spec[i]["op"] == "like" and isinstance(column_type, String):
                filter_spec[i]["value"] = "%" + filter_spec[0]["value"] + "%"

        # add model to our filters
        filter_spec = [
            {**item, **{"model": base_model.__name__}} for item in filter_spec
        ]
        db_query = apply_filters(db_query, filter_spec)

    sort_spec = query_modifiers_dict["sorters"]
    if sort_spec:
        # add model to our filters
        sort_spec = [{**item, **{"model": base_model.__name__}} for item in sort_spec]

        db_query = apply_sort(db_query, sort_spec)
    else:
        db_query = db_query.order_by(desc(default_sort_column))

    pagination_modifiers = query_modifiers_dict["pagination"]
    if pagination_modifiers and not pagination_modifiers.pop("all", True):
        page = pagination_modifiers.pop("page", None)
        if page:
            pagination_modifiers["page_number"] = page
        pagination_spec.update(pagination_modifiers)

    try:
        db_query, pagination = apply_pagination(db_query, **pagination_spec)
    except ProgrammingError as pe:
        APPLOG.warning(
            "Error while executing the query with modifier -> %s, err -> %s",
            query_modifiers_dict,
            str(pe),
        )
        pagination = Pagination(
            page_size=0, total_results=0, page_number=1, num_pages=0
        )
    except DataError:
        APPLOG.warning(
            "Invalid input data %s for %s type",
            str(query_value),
            str(column_type),
        )
        pagination = Pagination(
            page_size=0, total_results=0, page_number=1, num_pages=0
        )

    return db_query, pagination


class Filter(ABC):
    def __init__(self, field: Column[Any], value: Any):
        self.field: Column[Any] = field
        self.value: Any = value

    @abstractmethod
    def apply(self, query):
        ...


class FilterLike(Filter):
    def apply(self, query: Query):
        query.filter(self.field.ilike(f"%{self.value}%"))


class FilterEqual(Filter):
    def apply(self, query: Query):
        query.filter(self.field == self.value)


class FilterMin(Filter):
    def appy(self, query: Query):
        query.filter(self.field >= self.value)


class FilterMax(Filter):
    def appy(self, query: Query):
        query.filter(self.field <= self.value)


class Filters:
    def __init__(self):
        self.filters = []

    def add_filter(self, filter: Filter):
        self.filters.append(filter)

    def apply(self, query: Query):
        for filter in self.filters:
            filter.apply(query)

    @classmethod
    def parse(cls, request):
        filters = cls()
        # do parse work
        return filters


class MyFilters(Filters):
    hostname: FilterLike
    ip: FilterEqual
    min_vcpu: FilterMin
    max_vcpu: FilterMax


MyFilters.parse
