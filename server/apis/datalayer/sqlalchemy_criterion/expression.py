from operator import and_
from typing import Any, List
from ...autofilter.criterion import expression
from . import is_operator
from sqlalchemy import and_, or_, not_


@is_operator("sqlalchemy")
class AndExpression(expression.AndExpression):
    def execute(self, *args, **kwargs) -> Any:
        return and_(
            True, *(criterion.execute(*args, **kwargs) for criterion in self.criteria)
        )


@is_operator("sqlalchemy")
class OrExpression(expression.OrExpression):
    def execute(self, *args, **kwargs) -> Any:
        return or_(
            False, *(criterion.execute(*args, **kwargs) for criterion in self.criteria)
        )


@is_operator("sqlalchemy")
class NotExpression(expression.NotExpression):
    def execute(self, *args, **kwargs) -> Any:
        return not_(self.criterion.execute(*args, **kwargs))
