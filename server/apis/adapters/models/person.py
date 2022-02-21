from datetime import date
from pydantic import BaseModel
from typing import List, Optional


class Gender(BaseModel):
    class Config:
        orm_mode = True

    id: int
    value: str


class Person(BaseModel):
    class Config:
        orm_mode = True

    id: int
    first_name: str
    name: str
    birthdate: date
    gender: Gender
    emails: List["Email"]
    cellphones: Optional[List["Cellphone"]]


class Address(BaseModel):
    class Config:
        orm_mode = True

    id: int
    type: str
    value: str
    is_public: bool


class Email(Address):
    pass


class Cellphone(Address):
    pass


Person.update_forward_refs()
