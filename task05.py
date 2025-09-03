from abc import ABC, abstractmethod

# Abstrakt class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Circle class
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        pi = 3.14  
        return pi * (self.radius ** 2)

# Rectangle class
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


# Test qilish
c = Circle(5)
r = Rectangle(4, 6)

print(c.area())  # 78.5
print(r.area())  # 24
