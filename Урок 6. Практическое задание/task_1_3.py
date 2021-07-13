import numpy
from pympler import asizeof
import numpy as np


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):
        if len(self.matrix[0]) == len(other.matrix[0]):
            return Matrix([[self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))]
                           for i in range(len(self.matrix))])
        else:
            return f"\033[31m {'Math error. Need matrices of the same size'}"

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.matrix]))


class Matrix2:
    __slots__ = ['s_matrix']

    def __init__(self, s_matrix):
        self.s_matrix = s_matrix

    def __add__(self, other):
        if len(self.s_matrix) == len(other.s_matrix):
            return ([[self.s_matrix[i][j] + other.s_matrix[i][j] for j in range(len(self.s_matrix[0]))]
                    for i in range(len(self.s_matrix))])
        else:
            return f"\033[31m {'Math error. Need matrices of the same size'}"

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.s_matrix]))


matrix_1 = Matrix([[11, 15, 1], [34, 43, 23], [100, 54, 1]])
matrix_2 = Matrix([[1, 4, 4], [44, 51, 32], [76, 25, 67]])

matrix_3 = matrix_1 + matrix_2
print(f"{'*'*30} First Matrix {'*'*30}\n{matrix_1}")
print(f"{'*'*30} Second Matrix {'*'*30}\n{matrix_2}")
print(f"{'*'*30} Sum of matrix {'*'*30}\n{matrix_3}\n")

matrix_4 = Matrix2([[11, 15, 1], [34, 43, 23], [100, 54, 1]])
matrix_5 = Matrix2([[1, 4, 4], [44, 51, 32], [76, 25, 67]])
matrix_6 = matrix_4 + matrix_5
print(matrix_6)

matrix_7 = np.matrix([[11, 15, 1], [34, 43, 23], [100, 54, 1]])
matrix_8 = np.matrix([[1, 4, 4], [44, 51, 32], [76, 25, 67]])
matrix_9 = matrix_7 + matrix_8
print(matrix_6)

print(f'Dict: {asizeof.asizeof(matrix_1.__dict__)}\nSlots: {asizeof.asizeof(matrix_4.__slots__)}'
      f'\nNumpy.matrix: {asizeof.asizeof(matrix_7)}')


"""
Dict: 736
Slots: 128
Numpy.matrix: 328

Похоже, я закрыл и второе задание.

Основное задание было через класс релизовать перегрузку метода __add__ для сложения матриц. 
Вариант 1. __dict__
Матрица заняла 736 

Вариант 2. __slots__ 
Матрица заняла 128

Вариант 3. Использование matrix из бибилотеки numpy
Матрица заняла 328

Основное. Решение через перегрузку методов и определние __slots__ имеет место быть для существенной экономии памяти, 
но не является "питоническим". Наиболее оптимальным вариантом является использование бибилиотек, хоть они и расходуют 
немного больше памяти, но импортирование библиотеки + 3 строчки кода имеют отношение к  "Явное лучше, чем неявное". 

"""
