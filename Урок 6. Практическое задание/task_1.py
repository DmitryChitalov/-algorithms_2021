"""
Задание 1.

Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
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
from random import randint


''' Создаем декоратор для профилирования времени и памяти'''


def memory_time_profiler(func):
    def wraper(*args):
        memory = memory_usage()
        timer = default_timer()
        result = func(*args)
        memory = memory_usage()[0] - memory[0]
        timer = default_timer() - timer
        print(f'Время выполнения: {timer}\nИспользуемая память: {memory}')
        return result
    return wraper


'''Скрипт №1. Поиск четных и не четных чисел в строке'''


def parity_1(number, count_par, count_not_par):
    if number == 0:
        return f'Количество четных и нечетных цифр в числе равно: ({count_par}, {count_not_par})'
    if (number % 2) == 1:
        count_not_par += 1
    else:
        count_par += 1
    parity_1(number // 10, count_par, count_not_par)


def parity_2(number, count_par, count_not_par):
    for el in str(number):
        if (int(el) % 2) == 1:
            count_not_par += 1
        else:
            count_par += 1
        return f'Количество четных и нечетных цифр в числе равно: ({count_par}, {count_not_par})'


@memory_time_profiler
def recurs_parity(function, n, count_par, count_not_par):
    return function(n, count_par, count_not_par)


number = 1556674849880084098094983242342342342342342342342444234234234234234234234243234
count_par = 0
count_not_par = 0
recurs_parity(parity_1, number, count_par, count_not_par)
recurs_parity(parity_2, number, count_par, count_not_par)


''' За счет того что мы избавились от рекурсии и перешли на цикл, мспользование памяти уменьшилось, а время
выполнения осталось прежним
Время выполнения: 0.109463162
Используемая память: 0.03515625
Время выполнения: 0.10931710900000002
Используемая память: 0.0
'''

'''Скрипт №2. Нахождение факториала числа'''


def fact_1(n):
    if n == 0:
        return 1
    return fact_1(n-1) * n


def fact_2(n):
    factorial = 1
    for el in range(1, n + 1):
        factorial *= el
        yield factorial


@memory_time_profiler
def recurs_fact(function, n):
    return function(n)


n = 600
recurs_fact(fact_1, n)
recurs_fact(fact_2, n)

''' За счет того что мы используем генератор, вместо рекурсии использование памяти уменьшилось, а время
выполнения осталось прежним, особенно заметно при больших значениях n
Время выполнения: 0.109459215
Используемая память: 0.4921875
Время выполнения: 0.10937197799999998
Используемая память: 0.0
'''

'''Скрипт №3 Сложение и умножение комплексных чисел'''


class Complex_Number:
    @memory_time_profiler
    def __init__(self, com_num_1, com_num_2):
        self.number = complex(com_num_1, com_num_2)

    def __str__(self):
        return str(self.number)

    def __add__(self, other):
        return self.number + other.number

    def __mul__(self, other):
        return self.number * other.number


class Complex_Number_2:
    __slots__ = ('number')
    @memory_time_profiler
    def __init__(self, com_num_1, com_num_2):
        self.number = complex(com_num_1, com_num_2)

    def __str__(self):
        return str(self.number)

    def __add__(self, other):
        return self.number + other.number

    def __mul__(self, other):
        return self.number * other.number


com_num_1 = Complex_Number(2, 8)
com_num_2 = Complex_Number_2(2, 8)

'''
За счет того что мы создали слоты для класса, использование памяти уменьшилось.
Время выполнения: 0.10948408399999998
Используемая память: 0.00390625
Время выполнения: 0.10944184700000004
Используемая память: 0.0
'''