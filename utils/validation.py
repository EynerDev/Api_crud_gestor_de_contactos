class Validation:
    def param_data(
            self, data: dict, field: str, _type: str, required=True,
            max_len=0, min_len=0) -> list:

        return {

            "field": field,
            "value": data.get(field, ""),
            "type": _type,
            "required": required,
            "max_len": max_len,
            "min_len": min_len
        }

    def validate(self, list_validation: list):

        for value in list_validation:
            field = value["field"]
            val = value["value"]
            required = value["required"]
            max_len = value["max_len"]
            min_len = value["min_len"]

            if val == "" and required:
                error_message = (f"El campo {field} no puede estar vacio")
                raise AssertionError(error_message)

            if type(val) is not value["type"]:
                error_message = (f"El typo de dato del campo {
                                 field} es incorrecto")
                raise AssertionError(error_message)

            if max_len != 0 and len(val) > max_len:
                error_message = (f"El campo {field} no puede tener mas de {
                                 max_len} caracteres")
                raise AssertionError(error_message)

            if min_len != 0 and len(val) < min_len:
                error_message = (f"El campo {field} no puede ser menor de {
                                 min_len} caracteras")
                raise AssertionError(error_message)
