from enum import Enum


def deflate_request(object, keys):
    result = {}

    if not isinstance(object, dict):
        object = object.__dict__

    for key in keys:
        if isinstance(key, tuple):
            getter_key, result_key = key
        else:
            getter_key = result_key = key

        value = object[getter_key]
        if isinstance(value, Enum):
            value = value.value

        result[result_key] = value

    return result
