from database.conection import session
from utils.passwordEncript import PasswordEncrypt
from models.User import UserModel


class User:

    def create_new_user(self, data: dict) -> dict:
        user_name = data["user_name"]
        password = data["password"]

        self.validate_user_exist(user_name)

        password_encrypt = PasswordEncrypt()
        password_hash = password_encrypt.encrypt(password)
        data["password"] = password_hash

        new_user = UserModel(data)
        session.add(new_user)
        session.commit()

        return {"statusCode": 201, "data": {"message": "Usuario Registrado"}}

    def validate_user_exist(self, user_name: str):
        validate_user = session.query(UserModel).filter(
            UserModel.user_name == user_name
        ).all()

        if validate_user:
            raise AssertionError(
                "Ya existe un usuario con ese nombre de usuario"
            )

    def login_user(self, data: dict) -> dict:
        user_name = data["user_name"]
        password = data["password"]

        autentication_user = session.query(UserModel).filter(
            UserModel.user_name == user_name,
        ).first()
        if not autentication_user:
            return {
                "message":
                    "No se a encontrado un usuario con este nombre de usuario"
            }

        # user_authentication = autentication_user.user_name,
        hash_pass = autentication_user.password
        password_autentication = PasswordEncrypt()

        if not password_autentication.validate(password, hash_pass):
            raise AssertionError("Contraseña incorrecta")
        return {"message": "Usuario Logeado"}   
