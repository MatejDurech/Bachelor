from build import Build
import random


def f1_function(floors):
    f1_list = list()
    x3 = random.randint(3, (floors / 3) - 1)
    x2 = random.randint(x3 + 1, (floors / 2) - 1)
    x1 = random.randint(2, x3 - 1)
    x5 = random.randint((2 * (floors / 3)) + 1, floors - 3)
    x6 = random.randint((floors / 2) + 1, x5 - 1)
    x7 = random.randint(x5 + 1, floors - 1)
    x4 = random.randint(x2 + 1, x6 - 1)
    f1_list.append(x1)
    f1_list.append(x2)
    f1_list.append(x3)
    f1_list.append(x4)
    f1_list.append(x5)
    f1_list.append(x6)
    f1_list.append(x7)
    print(f1_list)
    return f1_list


def f3_function(floors):
    f3_list = list()
    x3 = random.randint(3, int(((floors + 1) / 3)) - 1)
    x2 = random.randint(x3 + 1, int(((floors + 1) / 2)) - 1)
    x1 = random.randint(2, x3 - 1)
    x5 = random.randint((2 * int(((floors + 1) / 3))) + 1, floors - 3)
    x6 = random.randint(int(((floors + 1) / 2)) + 1, x5 - 1)
    x7 = random.randint(x5 + 1, floors)
    x4 = random.randint(x2 + 1, x6 - 1)
    f3_list.append(x1)
    f3_list.append(x2)
    f3_list.append(x3)
    f3_list.append(x4)
    f3_list.append(x5)
    f3_list.append(x6)
    f3_list.append(x7)
    print(f3_list)
    return f3_list


def f4_function(floors):
    f4_list = list()
    x3 = random.randint(2, (floors / 3) - 1)
    x2 = random.randint(x3 + 1, (floors / 2) - 1)
    x1 = random.randint(1, x3 - 1)
    x5 = random.randint((2 * (floors / 3)) + 1, floors - 3)
    x6 = random.randint((floors / 2) + 1, x5 - 1)
    x7 = random.randint(x5 + 1, floors - 1)
    x4 = random.randint(x2 + 1, x6 - 1)
    f4_list.append(x1)
    f4_list.append(x2)
    f4_list.append(x3)
    f4_list.append(x4)
    f4_list.append(x5)
    f4_list.append(x6)
    f4_list.append(x7)
    print(f4_list)
    return f4_list


def random_search(floors):
    f1 = f1_function(floors)
    f3 = f3_function(floors)
    f4 = f4_function(floors)
    f = list()
    f.append(f1)
    f.append(f3)
    f.append(f4)
    return f
def f1():
    f = list()
    f.append(3)
    f.append(9)
    f.append(7)
    f.append(11)
    f.append(17)
    f.append(14)
    f.append(22)
    return f

def f3():
    f = list()
    f.append(7)
    f.append(10)
    f.append(9)
    f.append(13)
    f.append(20)
    f.append(18)
    f.append(23)
    return f

def f4():
    f = list()
    f.append(4)
    f.append(8)
    f.append(6)
    f.append(13)
    f.append(17)
    f.append(15)
    f.append(22)
    return f

def fuzzy():
    f = list()
    f.append(f1())
    f.append(f3())
    f.append(f4())
    return f


if __name__ == '__main__':
    counter = 0
    floors = 24
    elevators = 3
    capacity = 9
    metric = 0
    final_list_of_value_good = list()
    final_list_of_value_bad = list()
    algorithm = 'random'

    if algorithm == 'nearest car':
        list_of_values = random_search(floors)
        value = 0
        while counter < 40:
            build = Build(floors, elevators, list_of_values, algorithm)
            value = build.main_loop()
            if value > 0:
                metric += value
                counter += 1
        print('nearest car: ', metric / 40)
    if algorithm == 'fuzzy':
        counter = 0
        while counter < 40:
            list_of_value = fuzzy()
            build = Build(floors, elevators, list_of_value, algorithm)
            value = build.main_loop()
            if value > 0:
                metric += value
                counter += 1
        print('Fuzzy logic: ', metric / 40)
    if algorithm == 'random':
        final_metric_1 = 1000000
        helper = 0
        counter = 0
        while counter < 10:
            list_of_value = random_search(floors)
            build = Build(floors, elevators, list_of_value, algorithm)
            metric = build.main_loop()
            if metric > 0:
                if final_metric_1 > metric:
                    final_metric_1 = metric
                    final_list_of_value_good = list_of_value
                if helper < metric:
                    helper = metric
                    final_list_of_value_bad = list_of_value
                counter += 1

        final_metric_2 = 1000000
        counter = 0
        while counter < 10:
            list_of_value = random_search(floors)
            build = Build(floors, elevators, list_of_value, algorithm)
            metric = build.main_loop()
            if metric > 0:
                if final_metric_2 > metric:
                    final_metric_2 = metric
                counter += 1

        final_metric_3 = 1000000
        counter = 0
        while counter < 10:
            list_of_value = random_search(floors)
            build = Build(floors, elevators, list_of_value, algorithm)
            metric = build.main_loop()
            if metric > 0:
                if final_metric_3 > metric:
                    final_metric_3 = metric
                counter += 1

        final_metric_4 = 1000000
        counter = 0
        while counter < 10:
            list_of_value = random_search(floors)
            build = Build(floors, elevators, list_of_value, algorithm)
            metric = build.main_loop()
            if metric > 0:
                if final_metric_4 > metric:
                    final_metric_4 = metric
                counter += 1

        print('fuzzy logic random: ', (final_metric_1 + final_metric_2 + final_metric_3 + final_metric_4) / 4)
