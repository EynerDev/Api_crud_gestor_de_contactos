from sqlalchemy import Column, Integer, String, DateTime
from database.conection import Base
from sqlalchemy.sql.functions import current_timestamp


class userPermissonModel(Base):
    __tablename__ = "usser_permison"

    user_permisson_id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer, nullable=False)
    function_id = Column(Integer, nullable=True)
    active = Column(Integer, nullable=True, default=1)
    created_at = Column(DateTime, default=current_timestamp())
    update_at = Column(DateTime, default=current_timestamp(),
                       onupdate=current_timestamp())

    def __init__(self, data):
        self.user_id = data.get("user_id")
        self.function_id = data.get("function_id")

    def __repr__(self):
        return {
            "user_permisson_id": self.user_permisson_id,
            "user_id": self.user_id,
            "function_id": self.function_id
        }
