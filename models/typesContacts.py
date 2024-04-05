from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database.conection import Base


class typeContactsModel (Base):
    __tablename__ = "typesContacts"
    id_type = relationship(Integer, autoincrement=True, primary_key=True),
    description = Column(String, nullable=False),
