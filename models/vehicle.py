class Vehicle(object):
    def __init__(self, vehicle_dict):
        self.id = self.extract_id_from_url(vehicle_dict['url'])
        self.name = vehicle_dict['name']
        self.model = vehicle_dict['model']
        self.manufacturer = vehicle_dict['manufacturer']
        self.cost_in_credits = vehicle_dict['cost_in_credits']
        self.length = vehicle_dict['length']
        self.max_atmosphering_speed = vehicle_dict['max_atmosphering_speed']
        self.crew = vehicle_dict['crew']
        self.passengers = vehicle_dict['passengers']
        self.cargo_capacity = vehicle_dict['cargo_capacity']
        self.consumables = vehicle_dict['consumables']
        self.vehicle_class = vehicle_dict['vehicle_class']
        self.pilots = vehicle_dict['pilots']
        self.films= vehicle_dict['films']

    def extract_id_from_url(self, url):
        res = url[url.find('vehicles') + 8:]
        return res[0:len(res) - 1]
