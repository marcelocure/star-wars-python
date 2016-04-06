from base_repository import get, get_all
from models.vehicle import Vehicle

endpoint_name = 'vehicles'


def get_vehicle(id):
    return Vehicle(get(endpoint_name, id))

def get_vehicles():
    return map(lambda v: Vehicle(v), get_all(endpoint_name))