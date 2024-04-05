from sqlalchemy import Column, String, DateTime, Integer
from database.conection import Base
from os import getenv as os_getenv
from sqlalchemy.sql.functions import current_timestamp

root = os_getenv("ROOT")
admin = os_getenv("ADMIN")
support = os_getenv("SUPPORT")
developer = os_getenv("DEVELOPER")


class UserRolesModel(Base):
    __tablename__ = "user_roles"

    user_rol_id = Column(Integer, primary_key=True, autoincrement=True)
    role_name = Column(String(50), nullable=False)
    active = Column(Integer, default=1)
    created_at = Column(DateTime, default=current_timestamp())
    update_at = Column(DateTime, default=current_timestamp(),
                       onupdate=current_timestamp())

    def __init__(self, data):
        self.role_name = data.get("role_name").upper()

    def __repr__(self):
        return {
            "user_rol_id": self.user_rol_id,
            "role_name": self.role_name
        }
