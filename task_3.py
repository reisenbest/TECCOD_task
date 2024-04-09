import math


class Point:
    def __init__(self, x: float, y: float):
        '''
        без явновго метода инициализации через встроенный - point = Point(x, y)
        :param x: число координа по x
        :param y: число координата по y
        '''

        self.x = x
        self.y = y
        self.__validate_coordinates()

    def __validate_coordinates(self):
        '''

        проверки, можно еще добавить

        '''
        if not isinstance(self.x, (int, float)) or not isinstance(self.y, (int, float)):
            raise TypeError("Координаты должны быть числами")

    def get_coordinates(self):
        '''

        :return: возвращает координаты точки в формате кортежа (x, y)
        '''
        return (self.x, self.y)

    def change_coordinates(self, new_x, new_y):
        '''
        поменять можно и напрямую обратившись к элементу point.x = ...
        :param new_x: новую координату принимает по x
        :param new_y: новая координата по y
        :return:
        '''
        self.x = new_x
        self.y = new_y
        self.__validate_coordinates()

    def distance_to(self, another_point):
        '''

        :param another_point: принимает экземпляр этого же класса Point(x, y)
        :return: возвращает расстояние между двумя точками
        '''
        distance = math.hypot(self.x - another_point.x, self.y - another_point.y)
        return distance
