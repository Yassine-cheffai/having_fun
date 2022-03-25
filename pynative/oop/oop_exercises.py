from dataclasses import dataclass


@dataclass
class Vehicle:
    name: str
    max_speed: int
    mileage: int
    capacity: int = 5
    color: str = "white"

    def __eq__(self, instance) -> bool:
        return self.max_speed == instance.max_speed and self.mileage == instance.mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"


class Bus(Vehicle):
    def __init__(self, name: str, max_speed: int, mileage: int, capacity: int = 50):
        super().__init__(name, max_speed, mileage, capacity)


def exercise_1():
    vehicle = Vehicle("generic", 180, 3000, 4)
    return vehicle


def exercise_4():
    bus = Bus(name="bus", max_speed=120, mileage=140000)
    return bus
