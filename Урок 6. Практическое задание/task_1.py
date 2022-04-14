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

from random import randint
from pympler import asizeof
from numpy import array

"""
Оптимизация №1 - слоты в ООП, 
до добавления слотов в класс потреблало 240, 
после добавления слотов 72
"""

class Cell:
    __slots__ = ['count']
    def __init__(self, count):
        self.count = count

    def __int__(self):
        return int(self.count)

    def __add__(self, other):
        return self.count + int(other)

    def __sub__(self, other):
        if self.count - int(other) > 0:
            return self.count - int(other)
        else:
            print("Ошибка, Разность количества ячеек двух клеток меньше или равна нулю")

    def __mul__(self, other):
        return self.count * int(other)

    def __truediv__(self, other):
        return self.count // int(other)

    def make_order(self, cells_row):
        ch = '*'
        string = ""
        line = 0
        for i in range(self.count):
            line += 1
            string = string + ch
            if line == cells_row:
                line = 0
                string = string + '\n'
        return string

cell_1 = Cell(12)
cell_2 = Cell(5)

print(cell_1.make_order(5))
print(asizeof.asizeof(cell_1))

"""
Оптимизация №2 - array в numpy, 
был дан список, и надо было его обработать выведя только значения больше предыдущих...
при старом решении требовало 504 и 216 на изначальные и обработанный списки.
после применения функции array потребовало 160 и 136 соответственно.
"""

rand_list = [randint(0, 100) for i in range(10)]
print(f"Изначальный список {rand_list}")
print(asizeof.asizeof(rand_list))

new_list = [value for index, value in enumerate(rand_list) if value > rand_list[index - 1] and index != 0]
print(f"Обработанный список {new_list}")
print(asizeof.asizeof(new_list))


rand_list_numpy = array([randint(0, 100) for i in range(10)])
print(f"Изначальный список {rand_list}")
print(asizeof.asizeof(rand_list_numpy))

new_list_numpy = array([value for index, value in enumerate(rand_list) if value > rand_list[index - 1] and index != 0])
print(f"Обработанный список {new_list}")
print(asizeof.asizeof(new_list_numpy))

"""
Оптимизация №3 - генераторы
был дан список, надо вывести значения которые не повторяются
после обработки при помощи list comprehension - 216
после обработки при помощи генератора - 112
"""

num_list = [randint(0, 100) for i in range(500)]
print(f"Изначальный список {num_list}")
new_list = [i for i in num_list if num_list.count(i) == 1]
print(f"Обработанный список {new_list}")
new_generator = (i for i in num_list if num_list.count(i) == 1)
print(*new_generator)
print(asizeof.asizeof(new_list))
print(asizeof.asizeof(new_generator))