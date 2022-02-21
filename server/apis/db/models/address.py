from enum import auto
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..base import Base


class Address(Base):
    __tablename__ = "address"

    def __init__(self, type=None, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
        self.type = self.__mapper_args__["polymorphic_identity"]

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    type = Column(String, index=True)
    value = Column(String, nullable=False, index=True)
    is_public = Column(Boolean, nullable=False, index=True)
    owner_id = Column(Integer, ForeignKey("person.id"), index=True)
    __mapper_args__ = {"polymorphic_on": type}


class Email(Address):
    __mapper_args__ = {"polymorphic_identity": "email"}
    owner = relationship("Person", back_populates="emails")


class Cellphone(Address):
    __mapper_args__ = {"polymorphic_identity": "cellphone"}
    owner = relationship("Person", back_populates="cellphones")
