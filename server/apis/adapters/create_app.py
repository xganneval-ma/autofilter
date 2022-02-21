from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from ..autofilter.query_filter import QueryFilter

from .models import person
from ..datalayer import Datalayer, QueryOptions
from ..db.base import SessionLocal, engine, Base
from ..db.models.person import Person

Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/person/{person_id}", response_model=person.Person)
def read_person(person_id: int, db: Session = Depends(get_db)):
    datalayer = Datalayer(db, Person)
    item = datalayer.get_one(person_id)
    return item


@app.get("/person/", response_model=list[person.Person])
def read_persons(
    offset: int = 0, limit: int = 10, q: str = "", db: Session = Depends(get_db)
):
    datalayer = Datalayer(db, Person)
    query_filter = QueryFilter.from_str(q, [])
    options = QueryOptions(
        fields=None, offset=offset, filters=query_filter, limit=limit
    )
    items = datalayer.get_all(options)
    return items
