from abc import ABC, abstractmethod
import math


class Shape(ABC):
    
    @abstractmethod
    def calculate_perimeter(self):
        """Method to calculate the perimeter of the shape."""
        pass
    
    @abstractmethod
    def calculate_area(self):
        """Method to calculate the area of the shape."""
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_perimeter(self):
        """Calculate the perimeter (circumference) of the circle."""
        return 2 * math.pi * self.radius
    
    def calculate_area(self):
        """Calculate the area of the circle."""
        return math.pi * self.radius ** 2


class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length
    
    def calculate_perimeter(self):
        """Calculate the perimeter of the square."""
        return 4 * self.side_length
    
    def calculate_area(self):
        """Calculate the area of the square."""
        return self.side_length ** 2


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def calculate_perimeter(self):
        """Calculate the perimeter of the rectangle."""
        return 2 * (self.length + self.width)
    
    def calculate_area(self):
        """Calculate the area of the rectangle."""
        return self.length * self.width

#Example
circle = Circle(radius=5)
square = Square(side_length=4)
rectangle = Rectangle(length=6, width=3)


print(f"Circle: Perimeter = {circle.calculate_perimeter():.2f}, Area = {circle.calculate_area():.2f}")
print(f"Square: Perimeter = {square.calculate_perimeter()}, Area = {square.calculate_area()}")
print(f"Rectangle: Perimeter = {rectangle.calculate_perimeter()}, Area = {rectangle.calculate_area()}")
