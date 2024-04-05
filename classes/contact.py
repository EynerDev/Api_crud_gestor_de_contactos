from database.conection import session
from models.Contact import ContactModel


class Contact:
    def get_contacts(self, data):

        contacts = session.query(ContactModel).all()
        contacts_data = [contact.__repr__() for contact in contacts]

        return contacts_data

    def created_contact(self, data: dict) -> dict:
        # type_contact = data["type_contact"]
        number_contact = data["number_contact"]
        # name_contact = data["name_contact"]
        self.validate_contact_exist(number_contact)

        new_contact = ContactModel(data)
        session.add(new_contact)
        session.commit()

        return {"statusCode": 201, "data": {"message": "Contacto Registrado",
                                            "numero": data["number_contact"]}}

    def validate_contact_exist(self, number_contact: str):
        validate_contact = session.query(ContactModel).filter(
            ContactModel.number_contact == number_contact
        ).all()

        if validate_contact:
            raise AssertionError(
                "Ya existe contacto regsitrado con ese numero"
            )

    def updateContact(self, data):
        # type_contact = data["type_contact"]
        # number_contact = data["number_contact"]
        name_contact = data["name_contact"]
        update_contact_User = session.query(ContactModel).filter(
            ContactModel.name_contact == name_contact
        ).first()

        if not update_contact_User:
            return {"message": "No existe usuario registrado con ese nombre "}

        update_contact_User.name_contact = data["name_contact"]
        update_contact_User.number_contact = data["number_contact"]
        update_contact_User.type_contact = data["type_contact"]
        session.commit()

        return {
            "message": "Contacto Actualizado"}

    def delete_contacts(self, data):
        Contact_name = data["contact_name"]

        delete_user = session.query(ContactModel).filter(
            ContactModel.name_contact == Contact_name
        ).all()

        ContactModel.remove(delete_user)
        session.commit()

        return {
            "statusCode": 200,
            "message": "usuario Eliminado exitosamente"

        }
