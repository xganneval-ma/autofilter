from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship

from ..base import Base

def _resolve_email():
     from .address import Email
     return Email


def _resolve_cellphone():
     from .address import Cellphone
     return Cellphone

class Gender(Base):
    __tablename__ = "gender"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    value = Column(String, nullable=False, index=True, unique=True)


class Person(Base):
    __tablename__ = "person"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    name = Column(String, nullable=False)
    birthdate = Column(Date, nullable=False)

    gender_id = Column(Integer, ForeignKey("gender.id"), index=True, nullable=False)
    gender = relationship("Gender")

    emails = relationship(_resolve_email())
    cellphones = relationship(_resolve_cellphone())

