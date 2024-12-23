import doctest


class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def set_dimensions(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Ширина и высота должны быть положительными числами.")
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)


if __name__ == "__main__":
    doctest.testmod()
