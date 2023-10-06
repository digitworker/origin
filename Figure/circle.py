from figure import Figure
import math

class Circle(Figure):
    def __init__(self, radius):
        if radius<=0:
            raise Exception("Exception: The value is not positive.")
        else: self.radius = radius
    def setRadius(self, radius):
        if radius<=0:
            raise Exception("Exception: The value is not positive.")
        else: self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2