from passenger import Passenger


class Elevator(object):
    UP = 'up'
    DOWN = 'down'
    WAITING = 'waiting'

    def __init__(self, position, id, capacity):
        self.current_position = position
        self.end_point = position
        self.id = id
        self.count_person = 0
        self.stack_persons = list()
        self.nearest_floors = list()
        self.capacity = capacity
        self.direction = self.WAITING

    def get_direction(self):
        return self.direction

    def get_capacity(self):
        return self.capacity

    def get_current_position(self):
        return self.current_position

    def is_not_full(self):
        if self.get_capacity() == self.get_count_person():
            return False
        else:
            return True

    def is_empty_elevator(self):
        if self.get_count_person() == 0:
            return True
        else:
            return False

    def get_person_from_elevator(self):
        return self.stack_persons

    def get_id_elevator(self):
        return self.id

    def get_count_person(self):
        return self.count_person

    def set_direction(self, direction):
        self.direction = direction

    def set_current_position(self, current_position):
        self.current_position = current_position

    def goUp(self):
        self.set_direction(self.UP)
        self.set_current_position(round(self.get_current_position() + 0.2, 1))
        print(self.get_id_elevator(), " Actualy i go UP to: ", self.get_current_position())

    def goDown(self):
        self.set_direction(self.DOWN)
        self.set_current_position(round(self.get_current_position() - 0.2, 1))
        print(self.get_id_elevator(), " Actualy i go Down to: ", self.get_current_position())

    def person_add(self, person):
        self.stack_persons.append(person)
        self.count_person = self.get_count_person() + 1
        if self.get_count_person() == 1:
            person = self.stack_persons.__getitem__(0)
            self.set_direction(person.get_direction())
        print("Add person: ", self.current_position)

    def person_remove(self, index):
        person = self.stack_persons.__getitem__(index)
        self.stack_persons.pop(index)
        self.count_person = self.get_count_person() - 1
        if self.get_count_person() == 0:
            self.set_direction('waiting')
        print("Remove person: ", self.current_position)
        return person

    def get_travel_person(self):
        return self.stack_persons

    # def get_endpoint(self):
    #     global endpoint
    #     counter = 0
    #     if len(self.stack_persons) > 0:
    #         person = self.stack_persons.__getitem__(0)
    #         endpoint = person.get_Goal()
    #     else:
    #         endpoint = self.get_current_position()
    #     while len(self.stack_persons) > counter:
    #         person = self.stack_persons.__getitem__(counter)
    #         if self.UP == self.get_direction():
    #             if endpoint < person.get_Goal():
    #                 endpoint = person.get_Goal()
    #         if self.DOWN == self.get_direction():
    #             if endpoint > person.get_Goal():
    #                 endpoint = person.get_Goal()
    #         counter += 1
    #     return endpoint
