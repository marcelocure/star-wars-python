from base_repository import get, get_all
from models.person import Person

endpoint_name = 'people'


def get_person(id):
    return Person(get(endpoint_name, id))

def get_people():
    return map(lambda p: Person(p), get_all(endpoint_name))