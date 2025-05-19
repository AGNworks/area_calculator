"""
Module with different shape classes.
"""

import math
from area_calculator.base_shape_object import Shape


class Circle(Shape):
    """
    Class for representing a circle.
    """

    def __init__(self, radius: float):
        if radius <= 0 or not isinstance(radius, (float, int)) or isinstance(radius, bool):
            raise ValueError("The radius of a circle should be positive number")
        self.radius = radius
        print(self.radius)

    def area(self) -> float:
        try:
            return math.pi * self.radius ** 2
        except:
            print("You should define a Circle object with valid radius!")
            raise ValueError('Invalid radius value')


class Triangle(Shape):
    """
    Class for representing a triangle object.
    """

    def __init__(self, a: float, b: float, c: float):
        if any(side <= 0 for side in [a, b, c]):
            raise ValueError("All the sides should be positive numeber")
        if not self._is_valid_triangle(a, b, c):
            raise ValueError("Треугольник с такими сторонами не существует")
        self.a = a
        self.b = b
        self.c = c

    def area(self) -> float:
        """
        Get the area of the triangle - Heron’s Formula.
        """

        try:
            s = (self.a + self.b + self.c) / 2
            return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        except:
            print('There is not valid data for the triangle! Check the sides!')
            raise ValueError('Not valid triangle')

    def is_right(self) -> bool:
        """
        Check if it is a right triangle.
        """

        pass

    @staticmethod
    def _is_valid_triangle(a: float, b: float, c: float) -> bool:
        """
        Check if there is a valid triangle with these side lengths.
        Args:
            - a, b, c: the three sides of a triangle
        Returns:
            - bool: true if these for a valid triangle, flase if not
        """

        return (a + b > c) and (a + c > b) and (b + c > a)
