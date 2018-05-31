import random
from car import Car


class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        super().__init__(fuel)
        self.reliability = reliability
        self.name = name

    def drive(self, distance):
        randint = random.randint(0, 100)
        if self.reliability >= randint:
            distance_driven = super().drive(distance)
            return distance_driven
        else:
            distance_driven = 0
            return distance_driven
