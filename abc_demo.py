from abc import ABC, abstractmethod

# With ABC Shape cannot be instantiated AND classes that inherit from Shape have to implement all of the abstract methods
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return (self.length * self.length)

    def perimeter(self):
        return (4 * self.length)

square = Square(4)
print(square.area())
