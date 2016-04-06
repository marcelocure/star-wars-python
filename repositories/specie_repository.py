from base_repository import get, get_all
from models.specie import Specie

endpoint_name = 'species'


def get_specie(id):
    return Specie(get(endpoint_name, id))

def get_species():
    return map(lambda s: Specie(s), get_all(endpoint_name))