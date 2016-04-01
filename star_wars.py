from repositories import vehicle_repository, people_repository, specie_repository
from itertools import groupby

person_ids = [1, 42, 5, 5, 1, 45, 33, 50, 55, 66, 67, 68, 80]


def main():
    vehicle = vehicle_repository.get_vehicle(72)
    people = get_people()
    people = sorted(people, key=lambda k: k['species'])
    print group_by_species(people)


def group_by_species(people):
    people_grouped = []
    for specie, specie_people in groupby(people, lambda x: x['species']):
        if len(specie) > 0:
            specie_info = specie_repository.get_specie(extract_specie_id(specie))['name']
            group = {'specie': specie_info, 'people': map(lambda x: x, specie_people)}
            people_grouped.append(group)
    return people_grouped


def extract_specie_id(specie):
    first = specie[0]
    res = first[first.find('species')+8:]
    return res[0:len(res)-1]


def get_people():
    people = map(lambda person_id: people_repository.get_person(person_id), set(person_ids))
    return map(lambda p: {'name': p['name'], 'mass': p['mass'], 'gender': p['gender'], 'species': p['species'] }, people)


if __name__ == '__main__':
    main()
