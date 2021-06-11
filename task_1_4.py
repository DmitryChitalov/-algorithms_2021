from random import randint
from pympler import asizeof


class Matrix:
    """
    Класс Matrix (матрица).
    Принимает на вход данные (список списков) и формирует из них матрицу.
    """

    def __init__(self, arg):
        """ arg: список списков """
        self.matrix = arg

    def __str__(self):
        """ печатает матрицу в привычном виде """
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.matrix]))
        # return '\n'.join(map(str, self.matrix))

    def __add__(self, other):
        """ реализует операцию сложения двух матриц и возвращает новую матрицу """
        return Matrix([[el_1 + el_2 for el_1, el_2 in zip(self.matrix[i], other.matrix[i])]
                       for i in range(len(self.matrix))])


class MatrixOptimized:
    """
    Класс Matrix (матрица).
    Принимает на вход данные (список списков) и формирует из них матрицу.
    """
    __slots__ = ['matrix']

    def __init__(self, arg):
        """ arg: список списков """
        self.matrix = arg

    def __str__(self):
        """ печатает матрицу в привычном виде """
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.matrix]))
        # return '\n'.join(map(str, self.matrix))

    def __add__(self, other):
        """ реализует операцию сложения двух матриц и возвращает новую матрицу """
        return MatrixOptimized([[el_1 + el_2 for el_1, el_2 in zip(self.matrix[i], other.matrix[i])]
                                for i in range(len(self.matrix))])


row = int(input('Укажите кол-во строк в матрице: '))
column = int(input('Укажите кол-во столбцов в матрице: '))
mat_1 = MatrixOptimized([[randint(100, 1000) for j in range(column)] for i in range(row)])
mat_2 = Matrix([[randint(100, 1000) for k in range(column)] for n in range(row)])
print('Матрица №1:\n{}\nМатрица №2:\n{}\n'.format(mat_1, mat_2))

mat_3 = mat_1 + mat_2
print('Сумма исходных матриц:\n{}'.format(mat_3))


print(mat_1.__slots__)
print(mat_2.__dict__)

print('Размер экземпляра класса со слотом:', asizeof.asizeof(mat_1))
print('Размер экземпляра класса со словарем:', asizeof.asizeof(mat_2))


class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus
        self._income = {
            "wage": self.wage,
            "bonus": self.bonus
        }


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        Worker.__init__(self, name, surname, position, wage, bonus)

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')


class PositionWithSlots(Worker):
    __slots__ = ['name', 'surname', 'position', 'wage', 'bonus']

    def __init__(self, name, surname, position, wage, bonus):
        Worker.__init__(self, name, surname, position, wage, bonus)

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')
# with open('home_6_3.txt', encoding='utf-8', errors='ignore') as file:
#     worker_list = list(line.split() for line in file)
#
# for elem in worker_list:
#     for j in range(len(elem)):
#         if elem[j].isdigit():
#             elem[j] = int(elem[j])
#     worker = Position(*elem)
#     print(f'Имя, Фамилия сотрудника: {worker.get_full_name()}')
#     print(f'Должность: {worker.position}')
#     print(f'Доход с учётом премии: {worker.get_total_income()} у.е.')
#     print('-' * 10)


worker_1 = PositionWithSlots('Ivan', 'Ivanov', 'director', 21000, 12000)
worker_2 = Position('Sergey', 'Petrov', 'engineer', 17000, 10000)

print('Размер экземпляра класса со словарем:', asizeof.asizeof(worker_1))
print('Размер экземпляра класса со словарем:', asizeof.asizeof(worker_2))


"""
Для одного параметра применение слотов не даёт существенной экономии:
    Размер экземпляра класса со слотом: 17536
    Размер экземпляра класса со словарем: 17768

А вот для нескольких парметор слоты позволяют экономить память:
    Размер экземпляра класса со словарем: 832
    Размер экземпляра класса со словарем: 1008
"""