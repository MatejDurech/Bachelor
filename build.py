from random import randrange
import random
import math

from floor import Floor
from elevator import Elevator
from algorithm import algorithm_nearest_elevator
from algorithm import Fuzzy


class Build(object):

    def __init__(self, total_floors, total_elevator, list_of_value, algorithm):
        self.floors = list()
        self.elevators = list()
        self.algorithm = algorithm
        self.total_floors = total_floors
        self.total_elevator = total_elevator
        self.total_passenger = random.randint(3, 7)
        print(self.total_passenger)
        self.generated_person = 0
        self.removed_person = 0
        self.generate_elevators()
        self.generate_floors()
        self.one_floor_person = 0
        self.num_pred_padom = self.removed_person
        self.counter_pred_padom = 0
        self.list_of_value = list_of_value
        self.fuzzy = Fuzzy(self.list_of_value, self.total_floors, self.total_elevator)

    def get_Total_floors(self):
        return self.total_floors

    def get_Total_elevator(self):
        return self.total_elevator

    def get_generate_passenger(self):
        return self.generated_person

    def generate_floors(self):
        counter = 0
        while counter < self.total_floors:
            self.floors.append(Floor(counter))
            counter += 1

    def generate_elevators(self):
        counter = 0
        while counter < self.total_elevator:
            self.elevators.append(Elevator(randrange(10), counter, 9))
            counter += 1

    def generate_person(self):
        counter_person = randrange(3) + 1
        if self.get_generate_passenger() + counter_person >= self.total_passenger:
            return
        self.generated_person += counter_person
        counter = 0
        # id_elevator = 0
        while counter < counter_person:
            counter_floor = randrange(self.total_floors)
            floor = self.floors.__getitem__(counter_floor)
            next_floor = randrange(self.total_floors)
            while next_floor == counter_floor:
                next_floor = randrange(self.total_floors)
            person = floor.person_add(counter_floor, next_floor)
            # if self.algorithm == 'nearest car':
            #    id_elevator = algorithm_nearest_elevator(person, self.elevators, self.get_Total_floors())
            # if self.algorithm == 'fuzzy':
            #    id_elevator = self.fuzzy.algorithm_fuzzy_logic(person, self.elevators)
            # person.set_Tag(id_elevator)
            counter += 1

    def call_algorithm(self):
        array = list()
        counter = 0
        id_elevator = 0
        while counter < self.get_Total_floors():
            array.append(counter)
            counter += 1
        random.shuffle(array)
        for number in array:
            floor = self.floors.__getitem__(number)
            persons = floor.get_waiting_person()
            counter = 0
            while len(persons) > counter:
                person = persons.__getitem__(counter)
                if self.algorithm == 'nearest car':
                    id_elevator = algorithm_nearest_elevator(person, self.elevators, self.get_Total_floors())
                if self.algorithm == 'fuzzy':
                    id_elevator = self.fuzzy.algorithm_fuzzy_logic(person, self.elevators)
                if self.algorithm == 'random':
                    id_elevator = self.fuzzy.algorithm_fuzzy_logic(person, self.elevators)
                person.set_Tag(id_elevator)
                counter += 1

    def one_step(self):
        counter = 0
        while counter < self.total_elevator:
            elevator = self.elevators.__getitem__(counter)
            persons = elevator.get_person_from_elevator()
            counter_persons = 0
            while counter_persons < elevator.get_count_person():
                person = persons.__getitem__(counter_persons)
                person.one_step()
                counter_persons += 1
            counter += 1
        counter = 0
        while counter < self.total_floors:
            floor = self.floors.__getitem__(counter)
            persons = floor.get_waiting_person()
            counter_persons = 0
            while counter_persons < floor.get_count_person():
                person = persons.__getitem__(counter_persons)
                person.one_step()
                counter_persons += 1
            counter += 1

    def person_control(self, elevator):
        counter_control_person = 0
        if elevator.get_current_position() % 1 == 0:
            floor = self.floors.__getitem__(int(elevator.get_current_position()))
            persons = floor.get_waiting_person()
            counter_persons = 0
            while counter_persons < floor.get_count_person():
                person = persons.__getitem__(counter_persons)
                if elevator.get_count_person() == 0 and elevator.get_id_elevator() == person.get_tag() and elevator.is_not_full():
                    elevator.person_add(person)
                    floor.person_remove(counter_persons)
                    self.call_algorithm()
                    counter_control_person += 1
                elif elevator.get_direction() == person.get_direction() and elevator.get_id_elevator() == person.get_tag() and elevator.is_not_full():
                    elevator.person_add(person)
                    floor.person_remove(counter_persons)
                    self.call_algorithm()
                    counter_control_person += 1
                counter_persons += 1
            persons = elevator.get_travel_person()
            counter_persons = 0
            while counter_persons < elevator.get_count_person():
                person = persons.__getitem__(counter_persons)
                if int(elevator.get_current_position()) == person.get_Goal():
                    person_for_sum = elevator.person_remove(counter_persons)
                    if person_for_sum.get_actual_floor() > person_for_sum.get_Goal():
                        distance = person_for_sum.get_actual_floor() - person_for_sum.get_Goal()
                    else:
                        distance = person_for_sum.get_Goal() - person_for_sum.get_actual_floor()
                    self.one_floor_person += person.get_stepper() / distance
                    self.removed_person += 1
                    self.call_algorithm()
                    counter_control_person += 1
                counter_persons += 1
        if counter_control_person > 0:
            return True
        else:
            return False

    def exist_up_person(self, elevator):
        if not elevator.is_empty_elevator():
            return True
        counter = math.floor(elevator.get_current_position()) + 1
        while counter < self.get_Total_floors():
            floor = self.floors.__getitem__(counter)
            persons = floor.get_waiting_person()
            counter_person = 0
            while counter_person < floor.get_count_person():
                person = persons.__getitem__(counter_person)
                if person.get_tag() == elevator.get_id_elevator() and person.get_direction() == elevator.get_direction():
                    return True
                counter_person += 1
            counter += 1
        elevator.set_direction('waiting')
        return False

    def exist_down_person(self, elevator):
        if not elevator.is_empty_elevator():
            return True
        counter = 0
        while counter < elevator.get_current_position():
            floor = self.floors.__getitem__(counter)
            persons = floor.get_waiting_person()
            counter_person = 0
            while counter_person < floor.get_count_person():
                person = persons.__getitem__(counter_person)
                if person.get_tag() == elevator.get_id_elevator() and person.get_direction() == elevator.get_direction():
                    return True
                counter_person += 1
            counter += 1
        elevator.set_direction('waiting')
        return False

    def exist_down_person_with_zero(self, elevator):
        counter = 0
        while counter < elevator.get_current_position():
            floor = self.floors.__getitem__(counter)
            persons = floor.get_waiting_person()
            counter_person = 0
            while counter_person < floor.get_count_person():
                person = persons.__getitem__(counter_person)
                if person.get_tag() == elevator.get_id_elevator():
                    return True
                counter_person += 1
            counter += 1
        elevator.set_direction('waiting')
        return False

    def exist_up_person_with_zero(self, elevator):
        counter = math.floor(elevator.get_current_position()) + 1
        while counter < self.total_floors:
            floor = self.floors.__getitem__(counter)
            persons = floor.get_waiting_person()
            counter_person = 0
            while counter_person < floor.get_count_person():
                person = persons.__getitem__(counter_person)
                if person.get_tag() == elevator.get_id_elevator():
                    return True
                counter_person += 1
            counter += 1
        elevator.set_direction('waiting')
        return False

    def step(self, elevator):
        if elevator.get_direction() == 'waiting':
            num_of_floor = self.get_Total_floors()
            num = -1
            counter = 0
            help_num_of_floor = 0
            while counter < self.total_floors:
                floor = self.floors.__getitem__(counter)
                persons = floor.get_waiting_person()
                counter_person = 0
                while counter_person < floor.get_count_person():
                    person = persons.__getitem__(counter_person)
                    if person.get_tag() == elevator.get_id_elevator() and elevator.get_current_position() > person.get_actual_floor():
                        help_num_of_floor = elevator.get_current_position() - person.get_actual_floor()
                    if person.get_tag() == elevator.get_id_elevator() and elevator.get_current_position() < person.get_actual_floor():
                        help_num_of_floor = person.get_actual_floor() - elevator.get_current_position()
                    if help_num_of_floor < num_of_floor:
                        num_of_floor = help_num_of_floor
                        num = counter
                    counter_person += 1
                counter += 1
            if num > elevator.get_current_position():
                elevator.goUp()
            elif elevator.get_current_position() > num > 0:
                elevator.goDown()
            elif num == -1:
                return
        elif elevator.get_direction() == 'up' and self.exist_up_person(elevator):
            elevator.goUp()
        elif elevator.get_direction() == 'up' and self.exist_up_person_with_zero(
                elevator) and elevator.get_count_person() == 0:
            elevator.goUp()
        elif elevator.get_direction() == 'down' and self.exist_down_person(elevator):
            elevator.goDown()
        elif elevator.get_direction() == 'down' and self.exist_down_person_with_zero(
                elevator) and elevator.get_count_person() == 0:
            elevator.goDown()

    def helper(self):
        self.counter_pred_padom += 1
        if self.counter_pred_padom == 40 or self.counter_pred_padom == 80 or self.counter_pred_padom == 120 or self.counter_pred_padom == 160:
            self.call_algorithm()
        elevator1 = self.elevators.__getitem__(0)
        elevator2 = self.elevators.__getitem__(1)
        elevator3 = self.elevators.__getitem__(2)
        if self.counter_pred_padom > 180 and elevator1.get_count_person() == 0 and elevator2.get_count_person() == 0 and elevator3.get_count_person() == 0:
            return True
        else:
            return False

    def main_loop(self):
        counter_of_steps = 0
        while self.get_generate_passenger() + 1 < self.total_passenger or self.get_generate_passenger() > self.removed_person:
            random_generator_for_generate_person = randrange(5)
            if random_generator_for_generate_person == 3:
                self.generate_person()
                self.call_algorithm()
            counter = 0
            while counter < self.get_Total_elevator():
                elevator = self.elevators.__getitem__(counter)
                if not self.person_control(elevator):
                    self.step(elevator)
                counter += 1
            self.one_step()
            if self.num_pred_padom < self.removed_person:
                self.num_pred_padom = self.removed_person
                self.counter_pred_padom = 0
            if self.helper():
                return 0
            counter_of_steps += 1
            elevator1 = self.elevators.__getitem__(0)
            elevator2 = self.elevators.__getitem__(1)
            elevator3 = self.elevators.__getitem__(2)
            print('elevator1: ', elevator1.get_count_person())
            print('elevator2: ', elevator2.get_count_person())
            print('elevator3: ', elevator3.get_count_person())
            print('step:', counter_of_steps)
            print('removed :', self.removed_person)

        print(self.total_passenger)
        print(self.generated_person)
        print(self.removed_person)
        return self.one_floor_person / self.removed_person
