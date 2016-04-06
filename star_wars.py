from repositories import vehicle_repository, people_repository, specie_repository
from itertools import groupby

person_ids = [1, 42, 5, 5, 1, 45, 33, 50, 55, 66, 67, 68, 80]


def main():
    vehicle = vehicle_repository.get_vehicle(72)
    people = get_people()
    people = sorted(people, key=lambda x: x.specie)
    print group_by_species(people)


def group_by_species(people):
    people_grouped = []
    for specie, specie_people in groupby(people, lambda x: x.specie):
        people_grouped.append({'specie': specie, 'people': specie_people})
    return people_grouped


def get_people():
    return map(lambda person_id: people_repository.get_person(person_id), set(person_ids))


if __name__ == '__main__':
    main()
