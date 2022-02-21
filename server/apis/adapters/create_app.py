from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import models
from db.datalayer import Datalayer, QueryOptions
from db.base import SessionLocal, engine, Base
from db.models.person import Person

Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/person/", response_model=models.Person)
def create_person(person: models.Person, db: Session = Depends(get_db)):
    data_layer = Datalayer(entity_cls=Person, session=db)
    person = data_layer.create(person)
    return person


@app.get("/user/", response_model=list[models.Person])
def read_persons(
    offset: int = 0, page_size: int = 100, query: str = "", fields: str = None, db: Session = Depends(get_db)
):
    data_layer = Datalayer(entity_cls=Person, session=db)
    query = query
    query_option = QueryOptions(offset=offset, page_size=page_size, query=query, fields=fields)
    users = data_layer.get_all(query_option)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/users/{user_id}/items/", response_model=schemas.Item)
def create_item_for_user(
    user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    return crud.create_user_item(db=db, item=item, user_id=user_id)


@app.get("/items/", response_model=list[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items
