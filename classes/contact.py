from database.conection import session
from models.Contact import ContactModel


class Contact:
    def contactList(self, data):
        number_contact = data["number_contact"]
        contacts = session.query(ContactModel).filter(
            ContactModel.number_contact == number_contact).all()

        if contacts:
            for contact in contacts:
                return {
                    "type_contact": contact.type_contact,
                    "name_contact": contact.name_contact,
                    "number_contact": contact.number_contact
                }
        elif not contacts:
            raise AssertionError("No se encontro usuario registrado",
                                 "con ese numeros")
    def created_contact(self, data: dict) -> dict:        
        type_contact = data["type_contact"]
        number_contact = data["number_contact"]
        name_contact = data["name_contact"]
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
        type_contact = data["type_contact"]
        number_contact = data["number_contact"]
        name_contact = data["name_contact"]
        update_contact_User = session.query(ContactModel).filter(
            ContactModel.name_contact == name_contact
        ).first()
        if not update_contact_User:
            return{"message": "No existe usuario registrado con ese nombre "}
        else:
            update_Contact = ContactModel(data)
            session.add(update_Contact)
            session.commit()

            return {
                "message": "Contacto Actualizado"}