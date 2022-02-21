from typing import Any, List
from .base_operator import BaseOperator

class QueryFilter:
    @classmethod
    def from_str(cls, value: str, operators: List[BaseOperator]) -> BaseOperator:
        #on fait des trucs ici
        return cls()
