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

from memory_profiler import memory_usage
from timeit import default_timer
from numpy import array
from pympler import asizeof
from collections import namedtuple
from recordclass import recordclass


def decor_time_mem(func):
    def my_func(*args, **kwargs):
        start = default_timer()
        memory = memory_usage()
        result = func(*args, **kwargs)
        print(f'Память {memory_usage()[0] - memory[0]}')
        print(f'Время: {default_timer() - start}')
        print(f'Размер в байтах: {asizeof.asizeof(result)}')
        return result

    return my_func

print("==Matrix==")

@decor_time_mem
class Matrix_original:
    def __init__(self, matrix):
        self.matrix = matrix
    def __add__(self, other):
        for num in range(len(self.matrix)):
            for num2 in range(len(other.matrix[num])):
                self.matrix[num][num2] += other.matrix[num][num2]
        return self

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.matrix]))


matrix_1 = Matrix_original([[11, 12, 13], [14, 15, 16], [17, 18, 19]])
matrix_2 = Matrix_original([[19, 18, 17], [16, 15, 14], [13, 12, 11]])
print(matrix_1 + matrix_2)

@decor_time_mem
class Matrix_optimal:
    slots = ['matrix']
    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):
        for num in range(len(self.matrix)):
            for num2 in range(len(other.matrix[num])):
                self.matrix[num][num2] += other.matrix[num][num2]
        return self

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.matrix]))

matrix_3 = Matrix_optimal([[11, 21, 31], [41, 51, 61], [71, 81, 91]])
matrix_4 = Matrix_optimal([[91, 81, 71], [61, 51, 41], [31, 21, 11]])
print(matrix_3 + matrix_4)

"""
Магический атрибут Slot действительно ускоряет выполнение класса.
"""
print("==Numpy==")

@decor_time_mem
def numpy_arr():
    elem = array([el for el in range(1000000)])
    return elem


@decor_time_mem
def arr():
    elem = list(el for el in range(1000000))
    return elem


numpy_arr()
arr()

"""
Библиотека NumPy хорошо оптимизирована для работы с большими массивами, поэтому обычный список
проигрывает array в замерах памяти. 
"""
print("==Recordclass and collection==")

@decor_time_mem
def pers_info_original():
    namedtuple_ = namedtuple('test_1', 'name surname numbers address')
    info = namedtuple_(name='Ivan', surname='Ivanov', numbers=[el for el in range(10000)], address='New 55')
    return info


@decor_time_mem
def pers_info_optimal():
    recordclass_ = recordclass('test_2', ('name', 'surname', 'numbers', 'address'))
    info = recordclass_(name='Petr', surname='Petrov', numbers=[el for el in range(10000)], address='Old 11')
    return info


pers_info_original()
pers_info_optimal()
"""
Переменные recordclass действительно используют меньше места по сравнению с namedtuple, 
особенно при работе с большими объемами данных
"""