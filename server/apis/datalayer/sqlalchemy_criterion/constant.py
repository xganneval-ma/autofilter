from typing import Any
from ...autofilter.criterion import constant
from . import is_operator


@is_operator("sqlalchemy")
class CriterionConstant(constant.CriterionConstant):
    def execute(self, *args, **kwargs) -> Any:
        return self.value


@is_operator("sqlalchemy")
class AttributeAcesser(constant.AttributeAcesser):
    def execute(self, entity_cls, *args, **kwargs) -> Any:
        path = self.value.split('.')
        current_leaf = entity_cls
        for leaf in path:
            current_leaf = getattr(current_leaf, leaf)
        return current_leaf
