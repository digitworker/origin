import pytest
from triangle import Triangle
import math

class TestTriangle:
    triangle = Triangle(3,4,5)
    side1 = None
    side2 = None
    side3 = None
       
    def testTriangleArea(self):
        self.side1 = 3
        self.side2 = 4
        self.side3 = 5
        self.triangle.setSides(self.side1, self.side2, self.side3)
        pp = (self.side1 + self.side2 + self.side3) / 2
        assert self.triangle.area() == math.sqrt(pp * (pp - self.side1) * (pp - self.side2) * (pp - self.side3))
        self.side1 = 3.6
        self.side2 = 4
        self.side3 = 5
        self.triangle.setSides(self.side1, self.side2, self.side3)
        pp = (self.side1 + self.side2 + self.side3) / 2
        assert self.triangle.area() == math.sqrt(pp * (pp - self.side1) * (pp - self.side2) * (pp - self.side3))
        
    def testIsRightTriangleFunction(self):
        self.side1 = 3
        self.side2 = 4
        self.side3 = 5
        self.triangle.setSides(self.side1, self.side2, self.side3)
        sides = [self.side1, self.side2, self.side3]
        sides.sort()
        assert self.triangle.is_right_triangle() == (sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2)
        self.side1 = 3
        self.side2 = 4
        self.side3 = 5.5
        self.triangle.setSides(self.side1, self.side2, self.side3)
        sides = [self.side1, self.side2, self.side3]
        sides.sort()
        assert self.triangle.is_right_triangle() == (sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2)
    
    def testTriangleConstructorPositiveSides(self):
        self.side1 = -3
        self.side2 = 4
        self.side3 = 5
        with pytest.raises(Exception):
            self.triangle = Triangle(self.side1, self.side2, self.side3)
        self.side1 = 3
        self.side2 = -4
        self.side3 = 5
        with pytest.raises(Exception):
            self.triangle = Triangle(self.side1, self.side2, self.side3)
        self.side1 = 3
        self.side2 = 4
        self.side3 = -5
        with pytest.raises(Exception):
            self.triangle = Triangle(self.side1, self.side2, self.side3)
    
    def testTriangleSetterPositiveSides(self):
        self.side1 = -3
        self.side2 = 4
        self.side3 = 5
        with pytest.raises(Exception):
            self.triangle.setSides(self.side1, self.side2, self.side3)
        self.side1 = 3
        self.side2 = -4
        self.side3 = 5
        with pytest.raises(Exception):
            self.triangle.setSides(self.side1, self.side2, self.side3)
        self.side1 = 3
        self.side2 = 4
        self.side3 = -5
        with pytest.raises(Exception):
            self.triangle.setSides(self.side1, self.side2, self.side3)