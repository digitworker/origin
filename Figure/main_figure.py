from circle import Circle
from triangle import Triangle

# Пример использования классов Circle и Triangle:
if __name__ == "__main__":
    circle = Circle(5)
    print(f"Площадь круга: {circle.area()}")
    
    triangle = Triangle(3, 4, 5)
    print(f"Площадь треугольника: {triangle.area()}")
    
    if triangle.is_right_triangle():
        print("A triangle is a right triangle.")
    else:
        print("A triangle is not a right triangle.")
    
    # Вычисление площади фигур, незная их типа. И вывод на экран.
    figures = [circle, triangle]
    for i in range(0,len(figures)):
        print("Area of "+figures[i].__class__.__name__+" is " + str(figures[i].area()))