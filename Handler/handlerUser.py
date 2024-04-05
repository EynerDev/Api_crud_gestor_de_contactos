from utils.validation import Validation
from classes.user import User
from utils.eventTool import get_event_data, lamda_response

val = Validation()
user = User()


@lamda_response
def create_user(event, context):
    data = get_event_data(event)

    list_validation = [
        val.param_data(data, "full_name", str),
        val.param_data(data, "user_name", str, True, 20, 8),
        val.param_data(data, "password", str, True, 16, 8),
        val.param_data(data, "email", str, True),
        val.param_data(data, "mobile_phone", int, False),
    ]

    val.validate(list_validation)
    result = user.create_new_user(data)
    return result


@lamda_response
def login_user(event, context):
    data = get_event_data(event)

    list_validation = [
        val.param_data(data, "user_name", str),
        val.param_data(data, "password", str)
    ]
    val.validate(list_validation)

    result = user.login_user(data)
    return result


@lamda_response
def desactivate_user(event, context):
    data = get_event_data(event)
    result = user.desactivateUser(data)
    return result


@lamda_response
def UpdateUser(event, context):
    data = get_event_data(event)
    result = user.updateUser(data)
    return result


def getUser(event, context):
    data = get_event_data(event)
    result = user.get_users(data)
    return result
