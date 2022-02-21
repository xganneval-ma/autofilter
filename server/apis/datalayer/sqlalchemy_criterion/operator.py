from . import is_operator
from autofilter.criterion import operator


@is_operator("sqlalchemy")
class Equal(operator.Equal):
    def _execute(self, value, field, *args, **kwargs):
        return field == value


@is_operator("sqlalchemy")
class LowerThan(operator.LowerThan):
    type = "Lt"

    def _execute(self, value, field, *args, **kwargs):
        return field < value


@is_operator("sqlalchemy")
class LowerThanOrEq(operator.LowerThanOrEq):
    type = "Lte"

    def _execute(self, value, field, *args, **kwargs):
        return field <= value


@is_operator("sqlalchemy")
class GreaterThan(operator.GreaterThan):
    type = "Gt"

    def _execute(self, value, field, *args, **kwargs):
        return field > value


@is_operator("sqlalchemy")
class GreaterThan(operator.GreaterThan):
    type = "Gte"

    def _execute(self, value, field, *args, **kwargs):
        return field >= value


@is_operator("sqlalchemy")
class Like(operator.GreaterThan):
    type = "Like"

    def _execute(self, value: str, field, *args, **kwargs):
        return field.like(value)
