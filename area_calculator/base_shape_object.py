"""
The base Shape class.
"""

from abc import ABC, abstractmethod


class Shape(ABC):
    """
    Base Shape class for geometric shapes, to easier add new shapes.
    """

    @abstractmethod
    def area(self) -> float:
        """
        Required method for all classes created from Shape class.
        """

        pass
