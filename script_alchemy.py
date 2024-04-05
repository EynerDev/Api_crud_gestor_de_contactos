from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Crea un engine para conectarte a la base de datos MySQL
engine = create_engine('mysql+mysqlconnector://root@localhost/prueba')

Base = declarative_base()

# Definir una tabla


class Usuario(Base):
    __tablename__ = 'users'
    id_user = Column(Integer, primary_key=True)
    user_name = Column(String(50))
    password_user = Column(String(200))
    email = Column(String(200))


# Crea las tablas en la base de datos
# Base.metadata.create_all(engine)

# Crea una sesión para interactuar con la base de datos
Session = sessionmaker(bind=engine)
session = Session()

# Crear un nuevo usuario
nuevo_usuario = Usuario(
    user_name='Ejemplo',
    password_user="123450",
    email="ejemplo@email.com"
)

session.add(nuevo_usuario)
session.commit()

print("insert nuevo >>>> ", nuevo_usuario.id_user)
