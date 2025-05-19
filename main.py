"""
Example of using the area calculator.
"""

# Import the library
from area_calculator import calculator


# Test the calculator
if __name__ == '__main__':
    triangle = calculator.shapes.Triangle(2,2,3)

    print(calculator.get_shape_area(triangle))

    circle = calculator.shapes.Circle(0.001)

    print(calculator.get_shape_area(circle))

    circle = calculator.shapes.Circle(True)

    print(calculator.get_shape_area(circle))