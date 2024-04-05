from database.conection import session
from utils.passwordEncript import PasswordEncrypt
from models.User import UserModel


class User:

    def create_new_user(self, data: dict) -> dict:
        user_name = data["user_name"]
        password_user = data["password"]

        self.validate_user_exist(user_name)

        password_encrypt = PasswordEncrypt()
        passwordEncrypt = password_encrypt.encrypt(password_user)
        data["password"] = passwordEncrypt

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

    def desactivateUser(self, data):
        user_name = data["user_name"]
        desactivateUser = session.query(UserModel).filter(
            UserModel.user_name == user_name,
        ).first()
        if desactivateUser:
            desactivateUser.active = 0
            session.commit()
            return {
                "message": "Usuario desactivado exitosamente"
            }
        else:
            return {
                "message": "Error al momento de desactivar el usuario"
            }

    def updateUser(self, data):
        user_name = data["user_name"]
        password_user = data["password"]

        passwordEncript = PasswordEncrypt()
        update_new_user = session.query(UserModel).filter(
            UserModel.user_name == user_name
        ).first()

        if not update_new_user:
            raise AssertionError("Usuario no encontrado")

        update_new_user.user_name = data["user_name"].title()
        update_new_user.full_name = data["full_name"]
        update_new_user.email = data["email"]
        update_new_user.mobile_phone = data["mobile_phone"]
        update_new_user.password = data["password"]
        
        session.commit()

        passwordEncrypt = passwordEncript.encrypt(password_user)
        data["password"] = passwordEncrypt
        # update_user = UserModel(data)
        # session.commit()

        return {
            "message": "Usuario Actualizado correctamente",
            "data": update_new_user.__repr__()
        }

    def get_users(self, data):

        users = session.query(UserModel).filter(
            UserModel.active == 1
        ).all()

        data_response = [user.__repr__() for user in users]

        return data_response
