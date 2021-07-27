"""
Описать класс Shape - фигура, у которого должно быть 2 абстрактных метода:
- get_perimeter для расчета периметра
- get_square для расчета площади

Описать класс Circle для круга, отнаследоваться от фигуры
добавить недостающие атрибуты
перегрузить методы get_perimeter и get_square
Длина окружности = 2 * pi * r
Площадь = pi * r ** 2

Описать класс Rectangle для прямоугольника, отнаследоваться от фигуры
добавить недостающие атрибуты
перегрузить методы get_perimeter и get_square
Периметр = 2 * a + 2 * b
Площадь = a * b


Описать класс Square для квадрата, отнаследоваться от прямоугольника
перегрузить методы get_perimeter и get_square
Периметр = 4 * a
Площадь = a ** 2
"""

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):

    @abstractmethod
    def get_perimeter(self):
        pass

    @abstractmethod
    def get_square(self):
        pass


class Circle(Shape):

    rad: float

    def __init__(self, rad: float):
        self.rad = rad

    def get_perimeter(self):
        return(f'Периметр круга = {2 * pi * self.rad}')

    def get_square(self):
        return(f'Площадь круга = {pi * self.rad ** 2}')


class Rectangle(Shape):

    side_one: float
    side_two: float

    def __init__(self, side_one: float, side_two: float):

        self.side_one = side_one
        self.side_two = side_two

    def get_perimeter(self):
        return(f'Периметр прямоугольника = {2 * self.side_one + 2 * self.side_two}')

    def get_square(self):
        return(f'Площадь прямоугольника = {self.side_one * self.side_two}')


class Square(Rectangle):

    side_one: float

    def __init__(self, side_one: float):
        super().__init__(side_one, side_one)

    def get_perimeter(self):
        return(f'Периметр квадрата = {self.side_one * 4}')

    def get_square(self):
        return(f'Площадь квадрата = {self.side_one ** 2}')
