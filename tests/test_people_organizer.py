import unittest
import json
from models.person import Person
from people_organizer import sort_by_specie



class TestSortBySpecie(unittest.TestCase):
    people = []

    def setUp(self):
        people_json = reduce(lambda prev, next: prev + ' ' + next,open('fixtures/people.json').readlines())
        self.people = build_people(people_json)

    def test_sort_by_specie(self):
        result = sort_by_specie(self.people)
        assert result


def build_people(people_json):
    people_dict = json.loads(people_json)['results']
    return map(lambda p: Person(p), people_dict)

if __name__ == '__main__':
    unittest.main()