from sqlalchemy import Integer, String, Column, DateTime
from database.conection import Base
from sqlalchemy.sql.functions import current_timestamp


class UserModel(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String, nullable=False)
    user_name = Column(String, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, nullable=True)
    mobile_phone = Column(Integer)
    active = Column(Integer, server_default="1")
    created_at = Column(DateTime, default=current_timestamp())
    update_at = Column(DateTime, default=current_timestamp(),
                       onupdate=current_timestamp())

    def __init__(self, data):
        self.full_name = data.get("full_name").title()
        self.user_name = data.get("user_name").title()
        self.password = data.get("password")
        self.email = data.get("email")
        self.mobile_phone = data.get("mobile_phone")

    def __repr__(self):
        return {
            "full_name": self.full_name,
            "user_name": self.user_name,
            "email": self.email,
        }
