"""
Задание 2.*
Предложить еще какие-либо варианты (механизмы, подходы, библиотеки, идеи)
для оптимизации памяти и
доказать!!! (наглядно, кодом) их эффективность (на примере профилировщика).
"""

import sys


ob = {'x': 1, 'y': 2, 'z': 3}


class Point:
    #
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


ob_class = Point(1, 2, 3)

print(sys.getsizeof(ob))
print(sys.getsizeof(ob_class.__dict__))


# Словарь экземпляра класса занимает меньше места в оперативной памяти, чем обычный словарь
# 232
# 104
