from . import is_operator
from ...autofilter.criterion import operator


@is_operator("sqlalchemy")
class Equal(operator.Equal):
    def _execute(self, field, value, *args, **kwargs):
        return field == value


@is_operator("sqlalchemy")
class LowerThan(operator.LowerThan):
    type = "Lt"

    def _execute(self, field, value, *args, **kwargs):
        return field < value


@is_operator("sqlalchemy")
class LowerThanOrEq(operator.LowerThanOrEq):
    type = "Lte"

    def _execute(self, field, value, *args, **kwargs):
        return field <= value


@is_operator("sqlalchemy")
class GreaterThan(operator.GreaterThan):
    type = "Gt"

    def _execute(self, field, value, *args, **kwargs):
        return field > value


@is_operator("sqlalchemy")
class GreaterThan(operator.GreaterThan):
    type = "Gte"

    def _execute(self, field, value, *args, **kwargs):
        return field >= value


@is_operator("sqlalchemy")
class Like(operator.Like):
    type = "Like"

    def _execute(self, field, value: str, *args, **kwargs):
        return field.like(value)

@is_operator("sqlalchemy")
class Between(operator.Between):
    def _execute(self, field, left_value, right_value, *args, **kwargs):
        return field.between(left_value, right_value)