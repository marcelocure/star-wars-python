from itertools import groupby


def sort_by_specie(people):
    return sorted(people, key=lambda x: x.specie)


def group_by_species(people):
    people_grouped = []
    for specie, specie_people in groupby(people, lambda x: x.specie):
        people_grouped.append({'specie': specie, 'people': specie_people})
    return people_grouped