# from typing import List
# from pydantic import BaseModel
# from ..db.base import SessionLocal, engine, Base
# from ..datalayer import Datalayer, QueryOptions
# from ..datalayer.datalayer import SqlQueryFilter
# from sqlalchemy.orm import Session
# from fastapi import Depends
# from fastapi_utils.cbv import cbv

# # Dependency
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# class Ressource():
#     db_model: Base
#     path: str
#     response_model: BaseModel
#     methods = List[str]
#     session: Session = Depends(get_db)

#     def declare_endpoints(self, app):
#         if "GET_ONE" in self.methods:
#             app.get("/%s/{id}" % self.path , response_model=self.response_model)(self.get_one)
#         if "GET_ALL" in self.methods:
#             app.get("/%s/" % self.path , response_model=self.response_model)(self.get_all)
    
#     def get_one(self, id):
#         datalayer = Datalayer(self.session, self.db_model)
#         item = datalayer.get_one(id)
#         return item

#     def get_all(self, offset: int = 0, limit: int = 10, q: str = ""):
#         datalayer = Datalayer(self.session, self.db_model)
#         query_filter = SqlQueryFilter.from_str(q)
#         options = QueryOptions(
#             fields=None, offset=offset, filters=query_filter, limit=limit
#         )
#         items = datalayer.get_all(options)
#         return items