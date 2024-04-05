from models.userRolesModel import UserRolesModel
from database.conection import session


class UserRoles:
    def register_user_roles(self, data: dict) -> dict:
        data["role_name"] = data["role_name"].upper()
        self.validate_user_rol_name_exists(data["role_name"])

        insert_role = UserRolesModel(data)
        session.add(insert_role)
        session.commit()

        data_response = {
            "user_role_id": insert_role.user_role_id

        }

        return {
            "status_code": 201, "data": data_response
        }
