import math

class Circle:
    def __init__(self, radius):
        self.radius = radius  
    
    def get_area(self):
        return math.pi * self.radius ** 2


my_circle = Circle(5) 
print("The area of the circle is:", my_circle.get_area())

my_circle2 = Circle(44) 
print("The area of the circle 2 is:", my_circle2.get_area())
