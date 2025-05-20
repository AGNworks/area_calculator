"""
Example of using the area calculator.
"""

# Import the library
from area_calculator import calculator


# Test the calculator
if __name__ == '__main__':
    # Create triangle object
    triangle = calculator.shapes.Triangle(2,2,3)

    # Get the area and if it is a right triangle
    print(calculator.get_shape_area(triangle))
    print(triangle.is_right())

    # Create a circle object
    circle = calculator.shapes.Circle(0.001)
    # Get its area
    print(calculator.get_shape_area(circle))
