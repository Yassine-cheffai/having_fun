from typing import Union  # because the or operator | need python 3.10
from dataclasses import dataclass


@dataclass
class Vector:
    x: Union[int, float] = 0
    y: Union[int, float] = 0
    z: Union[int, float] = 0

    def __repr__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"

    def __str__(self):
        return f"{self.x}i + {self.y}j + {self.z}k"

    def __getitem__(self, item: int) -> Union[int, float]:
        items = {0: self.x, 1: self.y, 2: self.z}
        if item in items:
            return items[item]
        else:
            raise IndexError("There are only three elemnts in the vector")

    def __add__(self, other):
        return Vector(x=self.x + other.x, y=self.y + other.y, z=self.z + other.z)

    def __sub__(self, other):
        return Vector(x=self.x - other.x, y=self.y - other.y, z=self.z - other.z)

    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y + self.z * other.z
        elif isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other, self.z * other)
        else:
            raise TypeError("operand must be Vector, int or float")


test = Vector(3, 5, 9) * Vector(1, -3, 2)
print(test)

test = Vector(3, 5, 9) * 3
print(test)
