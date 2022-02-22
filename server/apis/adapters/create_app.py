
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from ..datalayer.interface import get_one, get_all

from .models import person
from ..db.base import SessionLocal, engine, Base
from ..db.models.person import Person
from ..db.models.address import Email

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

@app.get("/person/{person_id}", response_model=person.Person)
def read_person(person_id: int, session: Session = Depends(get_db_session)):
    return get_one(person_id, Person, session)



@app.get("/person/", response_model=list[person.Person])
def read_persons(
    offset: int = 0, limit: int = 10, q: str = "", session: Session = Depends(get_db_session)
):
    return get_all(Person, offset, limit, q, session)


@app.get("/email/{email_id}", response_model=person.Email)
def read_email(email_id: int, session: Session = Depends(get_db_session)):
    return get_one(email_id, Email, session)


@app.get("/email/", response_model=list[person.Email])
def read_emails(
    offset: int = 0, limit: int = 10, q: str = "", session: Session = Depends(get_db_session)
):
    return get_all(Email, offset, limit, q, session)




# class PersonView(Ressource):
#     db_model = Person
#     path = 'person'
#     response_model = person.Person
#     methods = ['GET_ONE', 'GET_ALL']

# class EmailView(Ressource):
#     db_model = Email
#     path = 'email'
#     response_model = person.Email
#     methods = ['GET_ONE', 'GET_ALL']

# person_view = PersonView().declare_endpoints(app)
# email_view = EmailView().declare_endpoints(app)
