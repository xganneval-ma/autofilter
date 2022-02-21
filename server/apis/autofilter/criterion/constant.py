from ast import Constant, Name
from typing import Any

from .criterion import Criterion
from . import is_operator


@is_operator("bool")
class CriterionConstant(Criterion):
    value: str

    def __init__(self, value) -> None:
        self.value = value

    @classmethod
    def match(cls, node, operators):
        return isinstance(node, Constant)

    @classmethod
    def from_node(cls, node: Any, operators: Any):
        return cls(node.value)

    def execute(self, *args, **kwargs) -> Any:
        return self.value


@is_operator("bool")
class AttributeAcesser(CriterionConstant):
    @classmethod
    def from_node(cls, node: Any, operators: Any):
        return cls(node.id)

    @classmethod
    def match(cls, node, operators):
        return isinstance(node, Name)

    def execute(self, *args, **kwargs) -> Any:
        # to redifined
        return self.value
