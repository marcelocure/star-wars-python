from base_repository import get

endpoint_name = 'people'


def get_person(id):
    return get(endpoint_name, id)
