from utils.eventTool import get_event_data, lamda_response
from utils.validation import Validation
from classes.contact import Contact

val = Validation()
contact = Contact()


@lamda_response
def create_new_contact(event, context):
    data = get_event_data(event)
    list_validation = [
        val.param_data(data, "type_contact", str, True),
        val.param_data(data, "number_contact", str, True),
        val.param_data(data, "name_contact", str, True)
        ]
    val.validate(list_validation)
    result = contact.created_contact(data)
    return result
@lamda_response
def update_contact(event, context):
    data = get_event_data(event)
    result = contact.updateContact(data)
    return result
@lamda_response
def contactList(event, context):
    data = get_event_data(event)
    result = contact.contactList(data)
    return result