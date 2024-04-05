from database.conection import Base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql.functions import current_timestamp


class ContactModel (Base):

    __tablename__ = 'contactlist'

    id_contact = Column(Integer, nullable=False,
                        primary_key=True, autoincrement=True)
    type_contact = Column(String, nullable=False)
    number_contact = Column(String, nullable=False)
    name_contact = Column(String, nullable=False)
    created_at = Column(DateTime, default=current_timestamp())
    update_at = Column(DateTime, default=current_timestamp(),
                       onupdate=current_timestamp())

    def __init__(self, data):
        self.type_contact = data.get('type_contact')
        self.number_contact = data.get('number_contact')
        self.name_contact = data.get('name_contact').title()
        print(data)

    def __repr__(self):
        return {
            'type_contact': self.type_contact,
            'number_contact': self.number_contact,
            'name_contact': self.name_contact,
        }
