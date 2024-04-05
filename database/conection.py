from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from os import getenv as os_getenv

host = os_getenv("HOST_DB")
username = os_getenv("USERNAME_DB")
password = os_getenv("PASSWDORD_DB")
name_database = os_getenv("NAME_DB")

password = f":{password}" if password else ""

try:

    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{
        username}{password}@{host}/{name_database}'
    engine = create_engine(SQLALCHEMY_DATABASE_URI)

    Session = sessionmaker(bind=engine)
    session = Session()
    Base = declarative_base()

except Exception as err:
    raise AssertionError("Error de conexion", str(err))
