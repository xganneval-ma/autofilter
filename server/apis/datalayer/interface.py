
from .datalayer import Datalayer, QueryOptions, SqlQueryFilter

from sqlalchemy.orm import Session

def get_one(id, model, session):
    datalayer = Datalayer(session, model)
    item = datalayer.get_one(id)
    return item

def get_all(model, offset: int, limit: int, q: str, session: Session):
    datalayer = Datalayer(session, model)
    query_filter = SqlQueryFilter.from_str(q)
    options = QueryOptions(
        fields=None, offset=offset, filters=query_filter, limit=limit
    )
    items = datalayer.get_all(options)
    return items