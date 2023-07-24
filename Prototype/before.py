from abc import ABC, abstractmethod
from typing import List


class Shape(ABC):
    """
    Shape interface.
    """
    @abstractmethod
    def address(self):
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


def main():
    """
    Copy rectangles and squares after they have been created.
    """
    coordinates_one = [1, 2, 3, 4]
    coordinates_two = [5, 6, 7, 8]
    print("Creating a rectangle with coordinates {}".format(coordinates_one))
    rectangle_one = Rectangle(coordinates_one)
    print("Creating a clone of the rectangle")
    rectangle_two = rectangle_one
    rectangle_one.address()
    rectangle_two.address()
    print("Setting the coordinates of the clone to {}".format(coordinates_two))
    rectangle_two.coordinates = coordinates_two
    print("The coordinates of the original rectangle are {}".format(rectangle_one.coordinates))
    print("The coordinates of the clone are {}".format(rectangle_two.coordinates))
    
    side_one = 5
    side_two = 10
    print("Creating a square with side length {}".format(side_one))
    square_one = Square(5)
    print("Creating a clone of the square")
    square_two = square_one
    square_one.address()
    square_two.address()
    print("Setting the side length of the clone to {}".format(side_two))
    square_two.side = side_two
    print("The side length of the original square is {}".format(square_one.side))
    print("The side length of the clone is {}".format(square_two.side))


if __name__ == "__main__":
    main()
