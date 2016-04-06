from repositories import vehicle_repository, people_repository
from people_organizer import sort_by_specie, group_by_species

person_ids = [1, 42, 5, 5, 1, 45, 33, 50, 55, 66, 67, 68, 80]


def main():
    vehicle = vehicle_repository.get_vehicle(72)
    people = get_people()
    people = sort_by_specie(people)
    print group_by_species(people)


def get_people():
    return map(lambda person_id: people_repository.get_person(person_id), set(person_ids))


if __name__ == '__main__':
    main()
