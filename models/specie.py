class Specie(object):
    def __init__(self, specie_dict):
        self.id = self.extract_id_from_url(specie_dict['url'])
        self.name = specie_dict['name']
        self.classification = specie_dict['classification']
        self.designation = specie_dict['designation']
        self.average_height = specie_dict['average_height']
        self.skin_colors = specie_dict['skin_colors']
        self.hair_colors = specie_dict['hair_colors']
        self.eye_colors = specie_dict['eye_colors']
        self.average_lifespan = specie_dict['average_lifespan']
        self.homeworld = specie_dict['homeworld']
        self.language = specie_dict['language']
        self.people = specie_dict['people']
        self.films = specie_dict['films']

    def extract_id_from_url(self, url):
        res = url[url.find('species') + 8:]
        return res[0:len(res) - 1]
