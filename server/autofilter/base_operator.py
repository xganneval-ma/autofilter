from abc import abstractmethod, ABC
from typing import Type, TypeVar

Query = TypeVar('Query')
Entity = TypeVar('Entity')

class BaseOperator(ABC):
    @abstractmethod
    def execute(self, entity: Type[Entity], query: Type[Query]) -> Query:
        ...