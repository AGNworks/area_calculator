"""
Calculator to get area of different shapes.
"""

# TODO add all imports
from area_calculator.base_shape_object import Shape
# Import all classes to be able to use with main function
import area_calculator.shapes as shapes


def get_shape_area(shape: Shape) -> float:
    """
    Function to get the area of a Shape object.

    Args:
        - shape (Shape): a shape object of which we want to know the area

    Return:
        - float : the area of the input shape
    """

    return shape.area()