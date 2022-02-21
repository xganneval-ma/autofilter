from apis.autofilter.criterion import OPERATORS
from apis.autofilter.query_filter import BoolQueryFilter
from ast import parse

# from apis.autofilter.criterion.criterion import Criterion

filters = [
    "Eq(False, False)",
    "Eq(True, False)",
    "Eq('toto', 'toto')",
    "Eq(False, Eq('toto', 'tutu'))",
    "Eq(False, Eq(toto, 'tutu'))",
    "Lte(15, 56)",
    "Lte(56, 15)",
    "And(True, False, None)",
]

for filter in filters:
    # node = parse(filter).body[0].value
    query_filter = BoolQueryFilter.from_str(filter)
    print(filter, ":", query_filter.execute())
