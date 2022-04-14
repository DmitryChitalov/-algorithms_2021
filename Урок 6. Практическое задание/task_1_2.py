from random import randint
from functools import reduce
import memory_profiler
import timeit


def profiler(func):
    def wrapper(*args):
        start_time = timeit.default_timer()
        mem_start = memory_profiler.memory_usage()[0]
        func_result = func(*args)
        time_taken = timeit.default_timer() - start_time
        mem_used = memory_profiler.memory_usage()[0] - mem_start
        print("*" * 150)
        print(f"Функция {func.__name__} выполнялась {time_taken} сек и занимала в памяти {mem_used} MiB")
        print("*" * 150)
        return func_result

    return wrapper


class Matrix:
    """Класс реализует матрицы размерносити 3 на 3. Умеент складывать такие объекты"""

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        str_matrix = ''
        for row in self.matrix:
            for el in row:
                str_matrix += f'{el:10}'
            str_matrix += '\n'
        return str_matrix

    def __add__(self, other):
        if len(self.matrix) == len(other.matrix) & len(self.matrix[0]) == len(other.matrix[0]):
            new_matrix = [[el_self + el_other for el_self, el_other in zip(row_self, row_other)] for row_self, row_other
                          in
                          zip(self.matrix, other.matrix)]
        else:
            return str("Матрицы разноразмерные!!! Сложение невозможно!!!")
        return Matrix(new_matrix)


@profiler
def func_1():
    matrix_list = []
    for i in range(100000):
        matrix_list.append(Matrix([[randint(-100, 101) for _ in range(3)] for _ in range(3)]))
    print("Результат сложения списка матриц: ")
    print(reduce(lambda a, b: a + b, matrix_list))
    # print(f"Размер списка матриц: {asizeof(matrix_list)}")


@profiler
def func_2():
    matrix_list_2 = []
    for i in range(100000):
        matrix_list_2.append(Matrix([[randint(-100, 101) for _ in range(3)] for _ in range(3)]))
    print("Результат сложения списка матриц: ")
    print(reduce(lambda a, b: a + b, matrix_list_2))
    del matrix_list_2


func_1()
func_2()

"""
Вывод:
После выполнения func_2 инкримент памяти меньше по сравнению с первой функцией:
-Функция func_1 выполнялась 1.545329 сек и занимала в памяти 1.45703125 MiB
-Функция func_2 выполнялась 1.6267609 сек и занимала в памяти 0.2578125 MiB
тк после выполнения сложения всех элементов список объект список матриц был удален
"""
