"""
Tests
"""

import json
import math
from typing import Dict, Any
import pytest

from area_calculator import calculator


# Load test data from JSON files
with open('test_data_circle.json', encoding='utf-8') as f:
    circle_tests = json.load(f)

with open('test_data_triangle.json',  encoding='utf-8') as f:
    triangle_tests = json.load(f)


def calculate_circle_area(radius: float) -> float:
    """
    Calculate area of a circle given its radius.
    """

    try:
        circle = calculator.shapes.Circle(radius)
        return circle.area()
    except:
        return None


def calculate_triangle_area(a: float, b: float, c: float) -> float:
    """
    Calculate area of a triangle given its sides using Heron's formula.
    """

    try:
        triangle = calculator.shapes.Triangle(a, b, c)
        return triangle.area()
    except:
        return None


def is_right_triangle(a: float, b: float, c: float) -> bool:
    """
    Check if triangle is right-angled using Pythagorean theorem.
    """

    if not all(isinstance(side, (int, float)) for side in [a, b, c]):
        return None
    sides = sorted([a, b, c])
    return math.isclose(sides[0]**2 + sides[1]**2, sides[2]**2, rel_tol=1e-3)


# Circle tests
@pytest.mark.parametrize("test_data", circle_tests)
def test_circle_area(test_data: Dict[str, Any]):
    """
    Test the circle area calculating.
    """

    radius = test_data["radius"]
    expected_area = test_data["area"]
    expected_correct = test_data["correct_input"]

    actual_area = calculate_circle_area(radius)

    if expected_correct:
        assert isinstance(actual_area, float)
        assert math.isclose(actual_area, expected_area, rel_tol=1e-3)
    else:
        assert actual_area is None


# Triangle tests
@pytest.mark.parametrize("test_data", triangle_tests)
def test_triangle_area(test_data: Dict[str, Any]):
    """
    Test the triangle area calculating.
    """

    a, b, c = test_data["a"], test_data["b"], test_data["c"]
    expected_area = test_data["area"]
    expected_correct = test_data["correct_input"]

    actual_area = calculate_triangle_area(a, b, c)

    if expected_correct:
        assert isinstance(actual_area, float)
        assert math.isclose(actual_area, expected_area, rel_tol=1e-3)
    else:
        assert actual_area is None


# # Additional test for right triangle check if the data includes this field
# @pytest.mark.parametrize("test_data", [t for t in triangle_tests if "is_right_triangle" in t])
# def test_right_triangle_check(test_data: Dict[str, Any]):
#     if "is_right_triangle" not in test_data:
#         pytest.skip("Test data doesn't contain is_right_triangle field")

#     a, b, c = test_data["a"], test_data["b"], test_data["c"]
#     expected_right = test_data["is_right_triangle"]

#     # Only check if the input is valid
#     if test_data["correct_input"] and all(isinstance(side, (int, float)) for side in [a, b, c]):
#         actual_right = is_right_triangle(a, b, c)
#         assert actual_right == expected_right
