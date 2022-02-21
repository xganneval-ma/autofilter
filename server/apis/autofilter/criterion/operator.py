from typing import Any
from .criterion import Criterion
from . import is_operator


class Operator(Criterion):
    field: Criterion
    value: Criterion
    type: str

    @classmethod
    def from_node(cls, node, operators):
        field = cls.init_child(node.args[0], operators)
        value = cls.init_child(node.args[1], operators)
        return cls(field, value)

    def __init__(self, field, value):
        self.field = field
        self.value = value

    def execute(self, *args, **kwargs) -> Any:
        field = self.field.execute(*args, **kwargs)
        value = self.value.execute(*args, **kwargs)
        return self._execute(value, field)


@is_operator("bool")
class Equal(Operator):
    type = "Eq"

    def _execute(self, value, field, *args, **kwargs):
        return field == value


@is_operator("bool")
class LowerThan(Operator):
    type = "Lt"

    def _execute(self, value, field, *args, **kwargs):
        return field < value


@is_operator("bool")
class LowerThanOrEq(Operator):
    type = "Lte"

    def _execute(self, value, field, *args, **kwargs):
        return field <= value


@is_operator("bool")
class GreaterThan(Operator):
    type = "Gt"

    def _execute(self, value, field, *args, **kwargs):
        return field > value


@is_operator("bool")
class GreaterThan(Operator):
    type = "Gte"

    def _execute(self, value, field, *args, **kwargs):
        return field >= value


@is_operator("bool")
class GreaterThan(Operator):
    type = "Like"

    def _execute(self, value: str, field, *args, **kwargs):
        if value.startswith("%") and value.endswith("%"):
            return value[1:-1] in field
        if value.startswith("%"):
            return value[1:] in field
        if value.startswith("%"):
            return value[0:-1] in field
