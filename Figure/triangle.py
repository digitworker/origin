from figure import Figure
import math

class Triangle(Figure):
    def __init__(self, side1, side2, side3):
        if side1<=0:
            raise Exception("Exception: The value is not positive.")
        else: self.side1 = side1
        if side2<=0:
            raise Exception("Exception: The value is not positive.")
        else: self.side2 = side2 
        if side3<=0:
            raise Exception("Exception: The value is not positive.")
        else: self.side3 = side3
    def setSides(self, side1, side2, side3):
        if side1<=0:
            raise Exception("Exception: The value is not positive.")
        else: self.side1 = side1
        if side2<=0:
            raise Exception("Exception: The value is not positive.")
        else: self.side2 = side2 
        if side3<=0:
            raise Exception("Exception: The value is not positive.")
        else: self.side3 = side3
    def area(self):
        # Используем формулу Герона для вычисления площади треугольника
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def is_right_triangle(self):
        # Правильный треугольник = квадрат гипотенузы равен сумме квадратов катетов.
        sides = [self.side1, self.side2, self.side3]
        sides.sort()
        return sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2
    