"""
Задание 1.

Выполните профилирование памяти в скриптах.
Проанализируйте результат и определите программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.

Можно взять только домашние задания с курса Основ
или с текущего курса Алгоритмов

Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""

from pympler import asizeof
from sys import getsizeof
import numpy as np
from random import randint
import memory_profiler
from timeit import default_timer
import json

"""
Что-то ничего достойного из старых решений не нашлось
поэтому взял кое что из домашних наработок

Первая часть - это класс трехиерной точки, без всяких затей, 
просто реализованы несколько статических способов создания
простая оптимизация через слоты дала тройную экономию памяти
"""


class Point:
    counter = 0

    def __init__(self, name: int, x: float, y: float, z: float):
        Point.counter += 1
        self.id = Point.counter
        self.name = name
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    @staticmethod
    def create_point_from_list(data: list):
        if len(data) == 4:
            return Point(data[0], data[1], data[2], data[3])
        if len(data) == 3:
            return Point(Point.counter + 1, data[0], data[1], data[2])

    @staticmethod
    def create_point_from_input():
        data = input("Введите \"№ x y z\":").split()
        return Point.create_point_from_list(data)

    def __str__(self):
        return f"Точка № \"{self.name}\":\n" \
               f"\tx = {self.x}\n" \
               f"\ty = {self.y}\n" \
               f"\tz = {self.z}\n"


class Point2:
    __slots__ = ("name", "id", "x", "y", "z")
    counter = 0

    def __init__(self, name: int, x: float, y: float, z: float):
        Point2.counter += 1
        self.id = Point2.counter
        self.name = name
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    @staticmethod
    def create_point_from_list(data: list):
        if len(data) == 4:
            return Point2(data[0], data[1], data[2], data[3])
        if len(data) == 3:
            return Point2(Point2.counter + 1, data[0], data[1], data[2])

    @staticmethod
    def create_point_from_input():
        data = input("Введите \"№ x y z\":").split()
        return Point2.create_point_from_list(data)

    def __str__(self):
        return f"Точка № \"{self.name}\":\n" \
               f"\tx = {self.x}\n" \
               f"\ty = {self.y}\n" \
               f"\tz = {self.z}\n"


point1 = Point.create_point_from_list([1, 2, 3])
point2 = Point2.create_point_from_list([2, 3, 4])
print(f"Размер объета точка до использования слотов {asizeof.asizeof(point1)}")
print(f"Размер объета точка после использования слотов {asizeof.asizeof(point2)}")

"""
Размер объета точка до использования слотов 536
Размер объета точка после использования слотов 176

Точка по своей сути неизменяемый объект со статичной структурой
Использование слотов уменьшило размер объекта в три раза
"""


class Scan:
    def __init__(self, point_list):
        self.point_list = point_list


class Scan2:
    __slots__ = ("point_list")

    def __init__(self, point_list):
        self.point_list = np.array(point_list)


point_lst = [Point2.create_point_from_list([randint(0, 100), randint(0, 100), randint(0, 100)])
             for _ in range(100000)]

scan1 = Scan(point_lst)
scan2 = Scan2(point_lst)
print("=" * 66)
print(f"Размер объета скан до использования оптимизации {asizeof.asizeof(scan1)}")
print(f"Размер объета скан после оптимизации {asizeof.asizeof(scan2)}")

"""
Для оптимизации класса скан исплоьзовал слоты и запаковку в массив NumPy

Размер объета скан до использования оптимизации 21593040
Размер объета скан после оптимизации 40

Разница какя-то космическая....

Скорее всего потому что сами координаты точек все лежат в пределе от 0 до 100 и повторяются
"""


def decor(func):
    def wrapper(*args, **kwargs):
        m1 = memory_profiler.memory_usage()
        t1 = default_timer()
        res = func(args[0])
        m2 = memory_profiler.memory_usage()
        t2 = default_timer()
        mem_diff = m2[0] - m1[0]
        time_diff = t2 - t1
        return res, mem_diff, time_diff

    return wrapper


class Scan3:
    def __init__(self, point_list):
        self.point_list = point_list
        self.point_counter = 0

    @decor
    def get_next_point(self):
        if self.point_counter <= len(self.point_list):
            self.point_counter += 1
            return self.point_list[self.point_counter]
        else:
            self.point_counter = 0
            return -1


class Scan4:
    def __init__(self, point_list):
        for idx, point in enumerate(point_list):
            point_list[idx] = (point.name, point.x, point.y, point.z)
        self.point_list = json.dumps(point_list)
        self.point_counter = 0

    @decor
    def get_next_point(self):
        p_lst = json.loads(self.point_list)
        if self.point_counter <= len(p_lst):
            self.point_counter += 1
            return Point2.create_point_from_list(list(p_lst[self.point_counter]))
        else:
            self.point_counter = 0
            return -1


scan3 = Scan3(point_lst)
scan4 = Scan4(point_lst)

print("=" * 66)
print(f"Размер объета скан до использования сериализации {asizeof.asizeof(scan3)}")
print(f"Размер объета скан после сериализации {asizeof.asizeof(scan4)}")
print(scan3.get_next_point())
print(scan4.get_next_point())

"""
(<__main__.Point2 object at 0x0000023060557E00>, 0.00390625, 0.10909689999999994)
(<__main__.Point2 object at 0x0000023060557E00>, 0.0, 0.10907510000000009)

Оптимизировал память скана через сериализацию в JSON
Мне мое решение не нравится тем, что оно требует обратного чтения
из jsona при каждом вызове

общий размер объекта уменьшился почти в 10 раз, но время отдельной операции сильно возрасло из-за
распаковки, ну и время удвоилось(

"""
