from neomodel import db

from ..helpers.conversion import identity, inflate_query_result


def update_node(node, data):
    with db.transaction:
        for key, value in data.items():
            setattr(node, key, value)
        node.save()


def get_query_response(query, params={}, model=identity):
    return inflate_query_result(db.cypher_query(query, params), model)
