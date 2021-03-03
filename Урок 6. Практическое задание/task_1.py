"""
Задание 1.

Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.

Можно взять задачи с курса Основ
или с текущего курса Алгоритмов

Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""


"""
1) Реализуем сложение двух матриц стандартными средствами и средствами numpy
В качестве матриц используем список списков
"""

import numpy as np


class Matrix:
    def __init__(self, data):
        self.m = data

    def __add__(self, other):
        if len(self.m) < len(other.m):
            max_count = len(self.m)
            smaller_matrix = self
        else:
            max_count = len(other.m)
            smaller_matrix = other

        m = []
        for line_index in range(max_count):
            line = []
            for elem_index in range(len(smaller_matrix.m[line_index])):
                line.append(self.m[line_index][elem_index] + other.m[line_index][elem_index])
            m.append(line)
        return Matrix(m)


list1 = [[1, 1, 1], [2, 2, 2], [2, 2, 2]]
list2 = [[4, 4, 4], [5, 5, 50], [5, 5, 50]]

m1 = Matrix(list1)
m2 = Matrix(list2)

m3 = m1 + m2
print(m3.m)

m_np1 = np.array(list1)
m_np2 = np.array(list2)
print(m_np1 + m_np2)