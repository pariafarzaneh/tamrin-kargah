from abc import ABC, abstractmethod
# Base class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# Rectangle class
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# Circle class
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14159 * self.radius

# Create a list of shapes
shapes = [
    Rectangle(4, 5),
    Circle(3)
]

# Loop through and print area and perimeter
for shape in shapes:
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
    print("------")