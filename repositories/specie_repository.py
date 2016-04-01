from base_repository import get

endpoint_name = 'species'


def get_specie(id):
    return get(endpoint_name, id)
