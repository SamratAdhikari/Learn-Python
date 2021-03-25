# Abstract baseclass
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0

class Recangle(Shape):
    type = "Rectangle"
    sides = 4

    def __init__(self):
        self.length = 10
        self.breadth = 4

    def printarea(self):
        return self.length * self.breadth

rect1 = Recangle()
print(rect1.printarea())