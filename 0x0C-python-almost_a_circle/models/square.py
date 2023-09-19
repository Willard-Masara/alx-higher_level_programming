#!/usr/bin/python3
""" documentation of the rectangle problem """

from models.rectangle import Rectangle

class Square(Rectangle):
    """Class that defines properties of a Square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Creates a new instance of Square.

        Args:
            size (int): Size of the square.
            x (int, optional): x-coordinate. Defaults to 0.
            y (int, optional): y-coordinate. Defaults to 0.
            id (int, optional): Identity number of the square. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return a string representation of the square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Getter for the size attribute."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for the size attribute.

        Args:
            value (int): New size value.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update attributes of the square using *args and **kwargs.

        Args:
            *args: List of arguments (id, size, x, y).
            **kwargs: Dictionary of keyword arguments (id, size, x, y).
        """
        if args and len(args) > 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

