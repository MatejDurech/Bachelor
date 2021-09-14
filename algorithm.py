import skfuzzy as fuzzy
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt


class Fuzzy(object):
    def __init__(self, list_of_value, num_of_floor, capacity):
        self.f1_array = list_of_value.__getitem__(0)
        self.f3_array = list_of_value.__getitem__(1)
        self.f4_array = list_of_value.__getitem__(2)
        self.num_of_floor = num_of_floor
        distance_between_elevator_and_person_goal_variable = ctrl.Antecedent([1, 2, 5, 15, num_of_floor + 1],
                                                                             'distance_between_elevator_and_person_goal_variable')
        # distance_between_elevator_and_person_goal_variable.automf(3)
        distance_between_elevator_and_person_goal_variable['poor'] = fuzzy.trapmf(
            distance_between_elevator_and_person_goal_variable.universe, [1, 1, self.f1_array[0], self.f1_array[1]])
        distance_between_elevator_and_person_goal_variable['average'] = fuzzy.trimf(
            distance_between_elevator_and_person_goal_variable.universe,
            [self.f1_array[2], self.f1_array[3], self.f1_array[4]])
        distance_between_elevator_and_person_goal_variable['good'] = fuzzy.trapmf(
            distance_between_elevator_and_person_goal_variable.universe,
            [self.f1_array[5], self.f1_array[6], num_of_floor, num_of_floor])

        number_of_free_places_variable = ctrl.Antecedent([1, 4, 7, capacity + 1], 'number_of_free_places_variable')
        # number_of_free_places_variable.automf(3)
        number_of_free_places_variable['good'] = fuzzy.trapmf(number_of_free_places_variable.universe, [1, 1, 2, 4])
        number_of_free_places_variable['average'] = fuzzy.trimf(number_of_free_places_variable.universe, [3, 5, 7])
        number_of_free_places_variable['poor'] = fuzzy.trapmf(number_of_free_places_variable.universe, [6, 8, 9, 9])

        nearest_car_variable = ctrl.Antecedent([1, 2, 5, 15, num_of_floor + 2], 'nearest_car_variable')
        # nearest_car_variable.automf(3)
        nearest_car_variable['poor'] = fuzzy.trapmf(nearest_car_variable.universe,
                                                    [1, 1, self.f3_array[0], self.f3_array[1]])
        nearest_car_variable['average'] = fuzzy.trimf(nearest_car_variable.universe,
                                                      [self.f3_array[2], self.f3_array[3], self.f3_array[4]])
        nearest_car_variable['good'] = fuzzy.trapmf(nearest_car_variable.universe,
                                                    [self.f3_array[5], self.f3_array[6], num_of_floor + 1,
                                                     num_of_floor + 1])

        distance_between_person_and_elevator_variable = ctrl.Antecedent([0, 1, 2, 5, 15, num_of_floor + 1],
                                                                        'distance_between_person_and_elevator_variable')
        # distance_between_person_and_elevator_variable.automf(3)
        distance_between_person_and_elevator_variable['good'] = fuzzy.trapmf(
            distance_between_person_and_elevator_variable.universe, [0, 0, self.f4_array[0], self.f3_array[1]])
        distance_between_person_and_elevator_variable['average'] = fuzzy.trimf(
            distance_between_person_and_elevator_variable.universe,
            [self.f4_array[2], self.f4_array[3], self.f4_array[4]])
        distance_between_person_and_elevator_variable['poor'] = fuzzy.trapmf(
            distance_between_person_and_elevator_variable.universe,
            [self.f4_array[5], self.f4_array[6], num_of_floor, num_of_floor])

        solution = ctrl.Consequent([1, 3, 5, 7, 10], 'solution')
        solution.automf(3)

        # distance_between_elevator_and_person_goal_variable.view()
        # number_of_free_places_variable.view()
        # nearest_car_variable.view()
        # distance_between_person_and_elevator_variable.view()
        # solution.view()
        # plt.show()

        self.ruleG = ctrl.Rule(
            (distance_between_elevator_and_person_goal_variable['good'] & nearest_car_variable['good']) |
            (distance_between_elevator_and_person_goal_variable['good'] &
             distance_between_person_and_elevator_variable['good']) |
            (nearest_car_variable['good'] & distance_between_person_and_elevator_variable['good']) |
            (distance_between_elevator_and_person_goal_variable['good'] & number_of_free_places_variable[
                'good'] & nearest_car_variable['average'] & distance_between_person_and_elevator_variable[
                 'poor']) |
            (distance_between_elevator_and_person_goal_variable['good'] & number_of_free_places_variable[
                'good'] & nearest_car_variable['poor'] & distance_between_person_and_elevator_variable[
                 'average']) |
            (distance_between_elevator_and_person_goal_variable['average'] &
             number_of_free_places_variable['good'] & nearest_car_variable['poor'] &
             distance_between_person_and_elevator_variable['good']) |
            (distance_between_elevator_and_person_goal_variable['poor'] & number_of_free_places_variable[
                'good'] & nearest_car_variable['good'] & distance_between_person_and_elevator_variable[
                 'average']) |
            (distance_between_elevator_and_person_goal_variable['poor'] & number_of_free_places_variable[
                'good'] & nearest_car_variable['average'] & distance_between_person_and_elevator_variable[
                 'good']), solution['good'])

        self.ruleM = ctrl.Rule(
            (distance_between_elevator_and_person_goal_variable['good'] & number_of_free_places_variable['average'] & nearest_car_variable['average'] & distance_between_person_and_elevator_variable['poor']) |
            (distance_between_elevator_and_person_goal_variable['good'] & number_of_free_places_variable['average'] & nearest_car_variable['poor'] & distance_between_person_and_elevator_variable['average']) |
            (distance_between_elevator_and_person_goal_variable['average'] & number_of_free_places_variable['average'] & nearest_car_variable['good'] & distance_between_person_and_elevator_variable['poor']) |
            (distance_between_elevator_and_person_goal_variable['average'] & number_of_free_places_variable['average'] & nearest_car_variable['poor'] & distance_between_person_and_elevator_variable['good']) |
            (distance_between_elevator_and_person_goal_variable['poor'] & number_of_free_places_variable['average'] & nearest_car_variable['good'] & distance_between_person_and_elevator_variable['average']) |
            (distance_between_elevator_and_person_goal_variable['poor'] & number_of_free_places_variable['average'] & nearest_car_variable['average'] & distance_between_person_and_elevator_variable['good']) |
            (distance_between_elevator_and_person_goal_variable['average'] & nearest_car_variable['average']) |
            (distance_between_elevator_and_person_goal_variable['average'] & distance_between_person_and_elevator_variable['average']) |
            (nearest_car_variable['average'] & distance_between_person_and_elevator_variable['average']),
            solution['average'])

        self.ruleB = ctrl.Rule(
            (distance_between_elevator_and_person_goal_variable['poor'] & nearest_car_variable['poor']) |
            (distance_between_elevator_and_person_goal_variable['poor'] &
             distance_between_person_and_elevator_variable['poor']) |
            (nearest_car_variable['poor'] & distance_between_person_and_elevator_variable['poor']) |
            (distance_between_elevator_and_person_goal_variable['good'] & number_of_free_places_variable[
                'poor'] & nearest_car_variable['average'] & distance_between_person_and_elevator_variable[
                 'poor']) |
            (distance_between_elevator_and_person_goal_variable['good'] & number_of_free_places_variable[
                'poor'] & nearest_car_variable['poor'] & distance_between_person_and_elevator_variable[
                 'average']) |
            (distance_between_elevator_and_person_goal_variable['average'] &
             number_of_free_places_variable['poor'] & nearest_car_variable['good'] &
             distance_between_person_and_elevator_variable['poor']) |
            (distance_between_elevator_and_person_goal_variable['average'] &
             number_of_free_places_variable['poor'] & nearest_car_variable['poor'] &
             distance_between_person_and_elevator_variable['good']) |
            (distance_between_elevator_and_person_goal_variable['poor'] & number_of_free_places_variable[
                'poor'] & nearest_car_variable['good'] & distance_between_person_and_elevator_variable[
                 'average']) |
            (distance_between_elevator_and_person_goal_variable['poor'] & number_of_free_places_variable[
                'poor'] & nearest_car_variable['average'] & distance_between_person_and_elevator_variable[
                 'good']), solution['poor'])

    def algorithm_fuzzy_logic(self, person, elevators):
        total_points = list()
        counter = 0
        while counter < len(elevators):
            elevator = elevators.__getitem__(counter)
            if elevator.is_not_full():
                total_points.append(self.logic_for_fuzzy_logic(distance_between_person_and_elevator(person, elevator),
                                                               number_of_free_places(elevator),
                                                               nearest_car(person, elevator, self.num_of_floor),
                                                               distance_between_elevator_and_person_goal(person,
                                                                                                         elevator,
                                                                                                         self.num_of_floor), ))
            else:
                total_points.append(-1)
            counter += 1
        if len(total_points) > 0:
            return total_points.index(max(total_points))

    def logic_for_fuzzy_logic(self, f1, f2, f3, f4):
        tipping = ctrl.ControlSystem([self.ruleG, self.ruleM, self.ruleB])
        Tip = ctrl.ControlSystemSimulation(tipping)
        Tip.input['distance_between_elevator_and_person_goal_variable'] = f4
        Tip.input['number_of_free_places_variable'] = f2
        Tip.input['nearest_car_variable'] = f3
        Tip.input['distance_between_person_and_elevator_variable'] = f1
        try:
            Tip.compute()
            return Tip.output['solution']
        except ValueError:
            print(f4, f2, f3, f1)
            return 7.5


def algorithm_nearest_elevator(person, elevators, num_of_floor):
    counter = 0
    list_of_elevators_distance = list()
    while counter < len(elevators):
        elevator = elevators.__getitem__(counter)
        if elevator.is_not_full():
            list_of_elevators_distance.append(
                nearest_car(person, elevator, num_of_floor))
        else:
            list_of_elevators_distance.append(-1)
        counter += 1
    if len(list_of_elevators_distance) > 0:
        return list_of_elevators_distance.index(max(list_of_elevators_distance))


def distance_between_elevator_and_person_goal(person, elevator, num_of_floor):
    if person.get_Goal() >= elevator.get_current_position():
        distance = person.get_Goal() - elevator.get_current_position()
    else:
        distance = elevator.get_current_position() - person.get_Goal()
    if elevator.get_direction() == 'waiting':
        return num_of_floor - distance
    if (
            elevator.get_direction() == 'up' and person.get_actual_floor() >= elevator.get_current_position()) or (
            elevator.get_direction() == 'down' and person.get_actual_floor() <= elevator.get_current_position()):
        return num_of_floor - distance
    if (
            elevator.get_direction() == 'down' and person.get_actual_floor() > elevator.get_current_position()) or (
            elevator.get_direction() == 'up' and person.get_actual_floor() < elevator.get_current_position()):
        return 1


def number_of_free_places(elevator):
    return int(elevator.get_capacity() - elevator.get_count_person())


def nearest_car(person, elevator, num_of_floor):
    if person.get_actual_floor() >= elevator.get_current_position():
        d = person.get_actual_floor() - elevator.get_current_position()
    else:
        d = elevator.get_current_position() - person.get_actual_floor()
    if person.get_direction() == elevator.get_direction() or elevator.get_direction() == 'waiting':
        return (num_of_floor + 1) - d
    if (
            person.get_direction() == 'up' and elevator.get_direction() == 'down' and person.get_actual_floor() <= elevator.get_current_position()) or (
            person.get_direction() == 'down' and elevator.get_direction() == 'up' and person.get_actual_floor() >= elevator.get_current_position()):
        return num_of_floor - d
    if (
            person.get_direction() == 'up' and elevator.get_direction() == 'down' and person.get_actual_floor() > elevator.get_current_position()) or (
            person.get_direction() == 'down' and elevator.get_direction() == 'up' and person.get_actual_floor() < elevator.get_current_position()):
        return 1


def distance_between_person_and_elevator(person, elevator):
    if person.get_actual_floor() >= elevator.get_current_position():
        distance = person.get_actual_floor() - elevator.get_current_position()
    else:
        distance = elevator.get_current_position() - person.get_actual_floor()
    return distance
