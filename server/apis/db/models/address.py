from enum import auto
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..base import Base

class Email(Base):
    __tablename__ = "email"

    def __init__(self, type=None, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
        self.type = self.__tablename__

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    type = Column(String, index=True)
    value = Column(String, nullable=False, index=True)
    is_public = Column(Boolean, nullable=False, index=True)
    owner_id = Column(Integer, ForeignKey("person.id"), index=True)
    owner = relationship("Person", back_populates="email", uselist=False)
    # __mapper_args__ = {"polymorphic_identity": "email", 'polymorphic_load': 'inline'}


class Cellphone(Base):
    __tablename__ = "address"

    def __init__(self, type=None, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
        self.type = self.__tablename__
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    type = Column(String, index=True)
    value = Column(String, nullable=False, index=True)
    is_public = Column(Boolean, nullable=False, index=True)
    owner_id = Column(Integer, ForeignKey("person.id"), index=True)
    owner = relationship("Person", back_populates="cellphones")
    # __mapper_args__ = {"polymorphic_identity": "cellphone", 'polymorphic_load': 'inline'}
