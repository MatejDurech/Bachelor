class Passenger(object):

    def __init__(self, actual_floor, goal):
        self.actual_floor = actual_floor
        self.goal = goal
        self.tag = -1
        self.step = 0

    def get_Goal(self):
        return self.goal

    def get_actual_floor(self):
        return self.actual_floor

    def set_Tag(self, tag):
        self.tag = tag

    def get_tag(self):
        return self.tag

    def get_direction(self):
        if self.get_Goal() > self.get_actual_floor():
            return 'up'
        if self.get_Goal() < self.get_actual_floor():
            return 'down'

    def one_step(self):
        self.step += 1

    def get_stepper(self):
        return self.step
