from enum import Enum

from neomodel import db


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


def identity(**kwargs):
    return kwargs


def inflate_query_result(query_result, model=identity):
    data, columns = query_result
    return [
        model(**{column: value for column, value in zip(columns, row)}) for row in data
    ]


def get_query_response(query, params={}, model=identity):
    return inflate_query_result(db.cypher_query(query, params), model)


def str_enum_to_choices(enum):
    return {item.value: key for key, item in enum.__members__.items()}
