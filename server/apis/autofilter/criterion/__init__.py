OPERATORS = {}


def is_operator(type: str):
    def _is_operator(cls):
        OPERATORS.setdefault(type, [])
        OPERATORS[type].append(cls)
        return cls

    return _is_operator


from .operator import *
from .constant import *
from .expression import *
