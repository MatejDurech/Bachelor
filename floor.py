from passenger import Passenger


class Floor(object):

    def __init__(self, number):
        self.id = number
        self.count_person = 0
        self.list_of_persons = list()

    def get_id(self):
        return self.id

    def person_add(self, actualy, goal):
        self.list_of_persons.append(Passenger(actualy, goal))
        self.count_person = self.get_count_person() + 1
        # return self.list_of_persons.__getitem__(-1)

    def person_remove(self, index):
        self.list_of_persons.pop(index)
        self.count_person = self.get_count_person() - 1

    def get_count_person(self):
        return self.count_person

    def get_waiting_person(self):
        return self.list_of_persons

