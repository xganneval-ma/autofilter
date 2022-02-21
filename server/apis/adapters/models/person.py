from datetime import date
from pydantic import BaseModel
from typing import List


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
    cellphones: List["Cellphone"]


class Address(BaseModel):
    class Config:
        orm_mode = True

    id: int
    type: str
    value: str
    is_public: bool
    owner: "Person"


class Email(Address):
    owner: "Person"


class Cellphone(Address):
    owner: "Person"
