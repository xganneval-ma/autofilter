from typing import Any, List
from .criterion import Criterion
from ast import parse


class QueryFilter:
    @classmethod
    def from_str(cls, value: str, operators: List[Criterion]) -> Criterion:
        # on fait des trucs ici
        node = parse(value).body[0].value
        return Criterion.init_child(node, operators)
