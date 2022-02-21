from typing import List, Type, TypeVar
from dataclasses import dataclass
from autofilter.query_filter import QueryFilter
from sqlalchemy.orm import Session


Unset = object()

T = TypeVar("T")
M = TypeVar("M")


@dataclass
class QueryOptions:
    limit: int
    offset: int
    page_size: int
    filters: QueryFilter
    fields: List[str]


@dataclass
class Collection:
    items: List[Type[T]]
    count: int
    page_size: int
    offset: int


# Crud interface for sqlalchemy
class Datalayer:
    def __init__(self, session: Session, entity_cls: Type[T]) -> None:
        self.session = session
        self.entity_cls = entity_cls

    def delete(self, id) -> None:
        self.session.query(self.entity_cls).filter(self.entity_cls.id == id).delete()
        self.session.commit()

    def update(self, id: int, item: Type[M]) -> M:
        to_update_item = (
            self.session.query(self.entity_cls).filter(self.entity_cls.id == id).one()
        )
        for key, value in item.to_dict():
            if value is not Unset:
                setattr(to_update_item, key, value)
        self.session.merge(to_update_item)
        return to_update_item

    def create(self, item: Type[M]) -> M:
        new_item = self.entity_cls(**item.to_dict())
        self.session.add(new_item)
        self.session.commit()
        return new_item

    def get_one(self, id: int) -> Type[T]:
        return self.session.query(self.entity_cls).filter(self.entity_cls.id == id)

    def get_all(self, options: QueryOptions) -> Collection:
        query = self.session.query(self.entity_cls)
        query = options.filters.execute(query)
        total = query.count()
        query = query.offset(options.offset).limit(options.page_size)
        return Collection(
            items=query.all(),
            count=total,
            page_size=options.page_size,
            offset=options.offset,
        )