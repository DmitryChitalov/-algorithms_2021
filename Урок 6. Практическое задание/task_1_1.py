"""
Задание 1. Скрипт № 1

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

# Скрипт "Сложение двумерных матриц" -------------------------------------------

import memory_profiler
from timeit import timeit
from random import randint
from pympler import asizeof


class Matrix:
    """Класс Матрица"""

    def __init__(self, matr):
        """
        Конструктор принимает двумерную матрицу

        :param matr(list): список списков
        """

        self.matr = matr

    def __str__(self):
        """Метод перегружает print() для вывода матрицы в привычном виде"""

        for i in range(len(self.matr)):
            print(f'{self.matr[i]}')
        return '---------'

    def __add__(self, other):
        """Метод перегружает '+' для сложения матриц

        :return sum_matr(list): список списков
        """

        sum_matr = []
        for i in range(len(self.matr)):
            matr_list = []
            for j in range(len(self.matr[i])):
                matr_list.append(self.matr[i][j] + other.matr[i][j])
            sum_matr.append(matr_list)
        return sum_matr


class MatrixSlots:
    """Класс Матрица"""

    __slots__ = ('matr')  # Добавлено использование __slots__

    def __init__(self, matr):
        """
        Конструктор принимает двумерную матрицу

        :param matr(list): список списков
        """

        self.matr = matr

    def __str__(self):
        """Метод перегружает print() для вывода матрицы в привычном виде"""

        for i in range(len(self.matr)):
            print(f'{self.matr[i]}')
        return '---------'

    def __add__(self, other):
        """Метод перегружает '+' для сложения матриц

        :return sum_matr(list): список списков
        """

        sum_matr = []
        for i in range(len(self.matr)):
            matr_list = []
            for j in range(len(self.matr[i])):
                matr_list.append(self.matr[i][j] + other.matr[i][j])
            matr_list = tuple(matr_list)  # Добавлено преобразование в кортеж
            sum_matr.append(matr_list)
        return sum_matr


def decorat(func):
    """Функция-декоратор"""

    def wrapper(arg1, arg2):
        mem1 = memory_profiler.memory_usage()
        res = func(arg1, arg2)
        mem2 = memory_profiler.memory_usage()
        mem_diff = mem2[0] - mem1[0]
        return res, mem_diff

    return wrapper


@decorat
def func_matrix(matr_1, matr_2):
    """Функция перегруженного сложения объектов класса Matrix для производства замеров"""
    matr_3 = matr_1 + matr_2
    return matr_3


def gen_matrix(x, y):
    """Функция генерации двумерной матрицы"""
    matr = []
    for i in range(y):
        row = []
        for j in range(x):
            num = randint(1, 10)
            row.append(num)
        row = tuple(row)  # Добавлено преобразование в кортеж
        matr.append(row)
    return matr


if __name__ == '__main__':
    x = 1000  # ширина матрицы (количество значений во вложенной коллекции)
    y = 1000  # высота матрицы (количество вложеных коллекций)

    print(f'{"=" * 15} Класс Matrix {x} x {y} {"=" * 15}')

    matr_1 = Matrix(gen_matrix(x, y))
    print(f'Память для {type(matr_1)}: {asizeof.asizeof(matr_1)}')
    # print(matr_1)
    matr_2 = Matrix(gen_matrix(x, y))
    print(f'Память для {type(matr_2)}: {asizeof.asizeof(matr_1)}')
    # print(matr_2)

    matr_res = func_matrix(matr_1, matr_2)
    matr_3 = Matrix(matr_res[0])
    print(f'Память для {type(matr_3)}: {asizeof.asizeof(matr_1)}')
    # print(matr_3)

    print(f"Выполнение заняло {matr_res[1]} Mib")
    # print(timeit("func_matrix(matr_1, matr_2)", globals=globals(), number=1))

    print(f'{"=" * 12} Класс MatrixSlots {x} x {y} {"=" * 13}')

    matr_1 = MatrixSlots(gen_matrix(x, y))
    print(f'Память для {type(matr_1)}: {asizeof.asizeof(matr_1)}')
    # print(matr_1)
    matr_2 = MatrixSlots(gen_matrix(x, y))
    print(f'Память для {type(matr_2)}: {asizeof.asizeof(matr_1)}')
    # print(matr_2)

    matr_res = func_matrix(matr_1, matr_2)
    matr_3 = MatrixSlots(matr_res[0])
    print(f'Память для {type(matr_3)}: {asizeof.asizeof(matr_1)}')
    # print(matr_3)

    print(f"Выполнение заняло {matr_res[1]} Mib")
    # print(timeit("func_matrix(matr_1, matr_2)", globals=globals(), number=1))

"""
При сложении двумерных матриц на основе списков профилирование памяти при помощи кортежей 
снизило использование памяти в среднем на 25 %. 

Результаты замеров:
    матрица 100 х 100: list - 0.0078 Mib  tuple - 0.0859 Mib
    матрица 1000 х 1000: list - 9.0351 Mib  tuple - 7.9143 Mib
    матрица 10000 х 10000: list - 805.3782 Mib  tuple - 765.3354 Mib
    
Использование __slots__ в разы снизило объем памяти занимаемый объектами класса!!!.
    
    =============== Класс Matrix 1000 x 1000 ===============
    Память для <class '__main__.Matrix'>: 8049544
    Память для <class '__main__.Matrix'>: 8049544
    Память для <class '__main__.Matrix'>: 8049544
    Выполнение заняло 9.28515625 Mib
    ============ Класс MatrixSlots 1000 x 1000 =============
    Память для <class '__main__.MatrixSlots'>: 40
    Память для <class '__main__.MatrixSlots'>: 40
    Память для <class '__main__.MatrixSlots'>: 40
    Выполнение заняло 7.1171875 Mib
    
Вывод: 
    1. Использование __slots__ жизненно необходимо.
    2. Обращение к кортежам при профилировании памяти в скриптах на основе списков
целесообразно при значительном объеме значений в коллекции.
"""
