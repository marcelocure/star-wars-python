from repositories.specie_repository import get_specie

class Person(object):
    def __init__(self, person_dict):
        self.id = self.extract_id_from_key(person_dict['url'], 'people')
        self.name = person_dict['name']
        self.height = person_dict['height']
        self.mass = person_dict['mass']
        self.hair_color = person_dict['hair_color']
        self.skin_color = person_dict['skin_color']
        self.eye_color = person_dict['eye_color']
        self.birth_year = person_dict['birth_year']
        self.gender = person_dict['gender']
        self.homeworld = person_dict['homeworld']
        self.films = person_dict['films']
        self.specie = self.get_first_specie_name(map(lambda s: get_specie(self.extract_id_from_key(s, 'species')), person_dict['species']))
        self.vehicles = person_dict['vehicles']
        self.starships = person_dict['starships']

    def extract_id_from_key(self, url, key):
        res = url[url.find(key) + 8:]
        return res[0:len(res) - 1]

    def get_first_specie_name(self, species):
        specie_info = 'N/A'
        if len(species) > 0:
            specie_info = species[0].name
        return specie_info