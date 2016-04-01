from base_repository import get

endpoint_name = 'vehicles'


def get_vehicle(id):
    return get(endpoint_name, id)
