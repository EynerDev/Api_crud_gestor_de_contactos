from sqlalchemy import Column, Integer, String
from database.conection import Base


class typeContactsModel (Base):
    __tablename__ = "typesContacts"
    id_type = Column(Integer, autoincrement=True, primary_key=True),
    description = Column(String, nullable=False),
