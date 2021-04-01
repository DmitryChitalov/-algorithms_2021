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
2) Сравним списковое включение и генератор списка
"""
########################################################################################################################
import memory_profiler
import numpy as np
import timeit
from pympler import asizeof

count = 2000


def memory_measurement(func):
    def wrapper(*args, **kwargs):
        start_memory = memory_profiler.memory_usage()
        start_time = timeit.default_timer()

        res = func(*args, **kwargs)

        end_memory = memory_profiler.memory_usage()
        end_time = timeit.default_timer()

        mem_diff = end_memory[0] - start_memory[0]
        time_diff = end_time - start_time

        return res, mem_diff, time_diff

    return wrapper


class Matrix:
    def __init__(self, data):
        self.m = data

    def __add__(self, other):
        m = []
        for line_index in range(len(self.m)):
            line = []
            for elem_index in range(len(self.m[line_index])):
                line.append(self.m[line_index][elem_index] + other.m[line_index][elem_index])
            m.append(line)
        return Matrix(m)


@memory_measurement
def matrix_sum(m1, m2):
    """
    функция считает сумму двух матриц, состоящих из списков
    """
    return m1 + m2


@memory_measurement
def m_sum_gen(m1, m2):
    """
    функция считает сумму двух матриц, состоящих из генераторов
    """
    for line1, line2 in zip(m1.m, m2.m):
        line = []
        for elem_index in range(len(line1)):
            line.append(line1[elem_index] + line2[elem_index])
        yield line


@memory_measurement
def matrix_lc():
    """
    генерация списка через  lc
    """
    return [[i for i in range(count)] for j in range(count)]


@memory_measurement
def matrix_generator():
    """
    создание объекта генератора
    """
    for i in range(count):
        yield [j for j in range(count)]


@memory_measurement
def gen_iter(gen):
    for elem in gen:
        c = elem


# замерим результаты создания списка и генератора
list1, mem_diff1, time_diff1 = matrix_lc()
list2, mem_diff2, time_diff2 = matrix_generator()

# получим все данные из генератора
c, mem_diff2, time_diff2 = gen_iter(list2)

print(f'Генерация через LC затратила = {mem_diff1} mib, time_diff = {time_diff1} msec')
print(f'Генерация через generator затратила = {mem_diff2} mib, time_diff = {time_diff2} msec')

"""
1)
Генерация через LC затратила = 139.734375 mib, time_diff = 0.2783290070001385 msec
Генерация через generator затратила = 0.0 mib, time_diff = 0.10070318699945346 msec
Вывод №1: наглядно видим, что генератор использует гораздо меньше и времени и памяти
"""


m1 = Matrix(list1)
m2 = Matrix(list1)

s, mem_diff3, time_diff3 = matrix_sum(m1, m2)

m_np1 = np.array(list1)
m_np2 = np.array(list1)
s, mem_diff4, time_diff4 = matrix_sum(m_np1, m_np2)

print(f'Вычисление суммы списка списков затратила = {mem_diff3} mib, time_diff = {time_diff3} msec')
print(f'Вычисление суммы массивов NumPy затратила = {mem_diff4} mib, time_diff = {time_diff4} msec')
"""
2)
Вычисление суммы списка списков затратила = 147.68359375 mib, time_diff = 0.86058907000006 msec
Вычисление суммы массивов NumPy затратила = 30.4765625 mib, time_diff = 0.1176289610002641 msec
Вывод №2 - очевидно, что использование массивов NumPy требует гораздо меньше ресурсов
"""


m1_gen = Matrix(list2)
m2_gen = Matrix(list2)

m3, mem_diff5, time_diff5 = m_sum_gen(m1_gen, m2_gen)
# получим все данные из генератора
c, mem_diff5, time_diff5 = m_sum_gen(m1_gen, m2_gen)
r, mem_diff5, time_diff5 = gen_iter(c)

print(f'Вычисление суммы генераторов затратило = {mem_diff5} mib, time_diff = {time_diff5} msec')

"""
3)
Вычисление суммы генераторов затратило = 0.53125 mib, time_diff = 0.4272058790011215 msec
т.е. используя генератор, мы выигрываем даже у нампаевского массива
"""

"""
Попробуем разместить атрибуты в slots
"""


class Matrix2(Matrix):
    __slots__ = ['m']

    def __init__(self, data):
        self.m = data


def create_matrix1():
    return Matrix(list1)


def create_matrix2():
    return Matrix2(list1)


m = create_matrix1()
print(f'Создание матрицы без slots заняло = {asizeof.asizeof(m)} mib')

m = create_matrix2()
print(f'Создание матрицы c slots заняло = {asizeof.asizeof(m)} mib')

"""
4)
Создание матрицы без slots заняло = 144713024 mib
Создание матрицы c slots заняло =   144712976 mib

Совсем чуть чуть меньше)
"""