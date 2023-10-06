import pytest
from circle import Circle
import math

class TestFigure:
    circle = Circle(5)
    side1 = None
    side2 = None
    side3 = None
    
    def testCircleArea(self):
        r = 10
        self.circle.setRadius(r)
        assert self.circle.area()==math.pi*r**2
        r = 10.6
        self.circle.setRadius(r)
        assert self.circle.area()==math.pi*r**2
        
    def testCircleConstructorPositiveRadius(self):
        r = -5
        with pytest.raises(Exception):
            self.circle = Circle(r)
            
    def testCircleSetterPositiveRadius(self):
        r = -5
        with pytest.raises(Exception):
            self.circle.setRadius(r)