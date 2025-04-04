from random import uniform
from prac_09.car import Car

class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        if uniform(0.0, 100.0) < self.reliability:
            super().drive(distance)