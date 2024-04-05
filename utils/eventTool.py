from json import dumps as json_dumbs, loads as json_loads


def json_response(statusCode, message, data=[]):
    body = {
        "statusCode": statusCode,
        "msg": message
    }

    if data:
        body["data"] = data

    response = {
        "statusCode": statusCode,
        "body": json_dumbs(body)

    }

    return response


def lamda_response(function):
    def validation(event, context):
        statusCode = 200
        msg = "Ok"
        data = []

        try:
            data = function(event, context)
            if data and type(data) is dict:
                if "statusCode" in data:
                    statusCode = data["statusCode"]

                    if "msg" in data:
                        msg = data["msg"]

                    if "data" in data:
                        data = data["data"]

                    else:
                        data = []
        except Exception as err:
            print(str(err))
            statusCode = 400
            msg = str(err)

        return json_response(statusCode, msg, data)
    return validation


def get_event_data(event: dict) -> dict:

    data = {}

    requestContext = event["requestContext"]
    http = requestContext["http"]

    if event["body"]:
        data = json_loads(event["body"])

    if event["queryStringParameters"]:
        data = event["queryStringParameters"]

    if "access_data" in event:
        data = {
            **event["access_data"],
            **data
        }
    # Get api data
    data["method"] = http["method"]
    data["path"] = http["path"]

    return data
