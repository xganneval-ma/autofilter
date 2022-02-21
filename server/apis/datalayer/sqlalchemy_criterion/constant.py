from typing import Any
from autofilter.criterion import constant
from . import is_operator


@is_operator("sqlalchemy")
class CriterionConstant(constant.CriterionConstant):
    def execute(self, *args, **kwargs) -> Any:
        return self.value


@is_operator("sqlalchemy")
class AttributeAcesser(constant.AttributeAcesser):
    def execute(self, *args, **kwargs) -> Any:
        return self.value
