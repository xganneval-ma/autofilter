from apis.autofilter.criterion import OPERATORS
from apis.autofilter.query_filter import QueryFilter
from ast import parse

filters = [
    # "Eq(False, False)",
    # "Eq(True, False)",
    # "Eq('toto', 'toto')",
    # "Eq(False, Eq('toto', 'tutu'))",
    # "Eq(False, Eq(toto, 'tutu'))",
    # "Lte(15, 56)",
    # "Lte(56, 15)",
    "And(10, 20, 30)"
]
filter = "Eq(False, 'Eq('toto', 'tutu')')"
filter = "Eq(False, Eq('toto', 'tutu'))"
filter = "Eq(False, Eq(toto, 'tutu'))"
# filter = "Lte(15, 56)"
# node = parse(filter).body[0]
# test = Equal.from_node(node)
# print(test.execute())
for filter in filters:
    query_filter = QueryFilter.from_str(filter, OPERATORS["bool"])
    print(filter, ":", query_filter.execute())
