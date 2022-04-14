"""
Задание 2.*
Предложить еще какие-либо варианты (механизмы, подходы, библиотеки, идеи)
для оптимизации памяти и
доказать!!! (наглядно, кодом) их эффективность (на примере профилировщика).
С урока ничего не дублир-ть. только новые способы
"""


from pympler import asizeof
from recordclass import recordclass
from recordclass import make_dataclass


class Point:
    def __init__(self, x, y, z):

        self.x = x
        self.y = y
        self.z = z


Coordinates = Point(100, 500, 1000)
print(asizeof.asizeof(Coordinates))  # 416

Point = recordclass('Point', ('x', 'y', 'z'))
Coordinates = Point(100, 500, 1000)
print(asizeof.asizeof(Coordinates))  # 40

Position = make_dataclass('Position', ('x', 'y', 'z'))
Coordinates = Position(100, 500, 1000)
print(asizeof.asizeof(Coordinates))  # 40


class PointSlot:
    __slots__ = ['x', 'y', 'z']

    def __init__(self, x, y, z):

        self.x = x
        self.y = y
        self.z = z


Coordinates = PointSlot(100, 500, 1000)
print(asizeof.asizeof(Coordinates))  # 152
"""
Изучая способы оптимизации памяти в Python я встретил много интересных способов
таких как мнногопрцессорная обработка, использование PyPy, Cython. Но на разбор
и выполнение примеров с вышеперечисленными способами нужно гораздо больше времени
(во всяком случае для меня) чем отведено на выполнение ДЗ. Я решил привести пример
оптимизации памяти с помощью модуля "recordclass" т.к он более понятен мне.
И как можно видеть из замеров при помощи "recordclass" действительно получается достигнуть 
уменьшение объема памяти, занимаемой объектами.
Так же сделал сравнение с методом __slots__ где "recordclass" так же имеет приимущество.
"""
