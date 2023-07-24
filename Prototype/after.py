from abc import ABC, abstractmethod
import copy
from typing import List


class Shape(ABC):
    """
    Shape interface.
    """
    @abstractmethod
    def address(self):
        pass

    @abstractmethod
    def clone(self):
        pass


class Rectangle(Shape):
    """
    A Rectangle.
    """
    def __init__(self, coordinates: List) -> None:
        self._coordinates = coordinates

    @property
    def coordinates(self):
        return self._coordinates
    
    @coordinates.setter
    def coordinates(self, coordinates):
        self._coordinates = coordinates

    def address(self):
        address = hex(id(self._coordinates))
        print("Rectangular coordinates address: {}".format(address))

    def clone(self) -> Shape:
        coordinates = copy.deepcopy(self._coordinates)
        return Rectangle(coordinates)


class Square(Shape):
    """
    A Circle.
    """
    def __init__(self, side) -> None:
        self._side = side

    @property
    def side(self):
        return self._side
    
    @side.setter
    def side(self, side):
        print("Setting side")
        self._side = side

    def address(self):
        address = hex(id(self._side))
        print("Square side address: {}".format(address))

    def clone(self) -> Shape:
        side = copy.deepcopy(self._side)
        return Square(side)


def main():
    """
    Copy rectangles and squares using clone method
    Deep copy - Deep copy method constructs new object for every nested compound object.
    """
    coordinates_one = [1, 2, 3, 4]
    coordinates_two = [5, 6, 7, 8]
    print("Creating a rectangle with coordinates {}".format(coordinates_one))
    rectangle = Rectangle(coordinates_one)
    rectangle.address()
    print("Creating a clone of the rectangle")
    rectangle_clone = rectangle.clone()
    rectangle_clone.address()
    print("Setting the coordinates of the clone to {}".format(coordinates_two))
    rectangle_clone.coordinates = coordinates_two
    print("The coordinates of the original rectangle are {}".format(coordinates_one))
    print("The coordinates of the clone are {}".format(coordinates_two))

    side_one = 1
    side_two = 2
    print("Creating a square with side {}".format(side_one))
    square = Square(side_one)
    square.address()
    print("Creating a clone of the square")
    square_clone = square.clone()
    square_clone.address()
    print("Setting the side of the clone to {}".format(side_two))
    square_clone.side = side_two
    print("The side of the original square is {}".format(side_one))
    print("The side of the clone is {}".format(side_two))

if __name__ == "__main__":
    main()
