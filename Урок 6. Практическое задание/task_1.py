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

from memory_profiler import memory_usage, profile
from timeit import default_timer
from pympler import asizeof
from collections import namedtuple
import re
from recordclass import recordclass


def decor(func):
    def wrapper(*args):
        m1 = memory_usage()
        t1 = default_timer()
        res = func(*args)
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        time_diff = default_timer() - t1
        print(f'{res}, {mem_diff}, {time_diff}')

    return wrapper


# Скрипт №1
# Неоптимизированное решение

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        print(self.name, self.surname)

    def get_total_income(self):
        print(self._income['wage'] + self._income['bonus'])


worker = Position('Ivan', 'Ivanov', 'Boss', 500, 50)
print(asizeof.asizeof(worker))  # 960


# Оптимизированное
class Worker:
    __slots__ = ['name', 'surname', 'position', 'wage', 'bonus']

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        income = namedtuple('income', 'wage bonus')
        self._income = income(
            wage=wage,
            bonus=bonus
        )


class Position(Worker):
    def get_full_name(self):
        print(self.name, self.surname)

    def get_total_income(self):
        print(self._income.wage + self._income.bonus)


worker = Position('Ivan', 'Ivanov', 'Boss', 500, 50)
print(asizeof.asizeof(worker))  # 536


# Благодаря использованию слотов, а также замене словаря на именованный кортеж размер
# экземпляра класса уменьшился правктически в 2 раза


# Скрипт №2
# Неопмизированное
@decor
def not_optimized():
    def sum_num_list(number):
        result = 0
        num_list = list(str(number))
        for numb in num_list:
            result += int(numb)
        return result

    my_list = []
    for num in range(0, 10000):
        if num % 2:
            my_list.append(num ** 3)

    summary = 0
    for num in my_list:
        if not sum_num_list(num) % 7:
            summary += num
    print(summary)

    for idx in range(0, len(my_list)):
        my_list[idx] += 17

    summary = 0
    for num in my_list:
        if not sum_num_list(num) % 7:
            summary += num
    print(summary)


not_optimized()  # mem_diff = 0.265625, time_diff = 0.149514798


# Оптимизированное

@decor
def optimized():
    def sum_num_list(number):
        summary = 0
        num_list = list(str(number))
        for numb in num_list:
            summary += int(numb)
        return summary

    my_list = [num ** 3 for num in range(10000) if num % 2]

    gen_obj = (num for num in my_list if not sum_num_list(num) % 7)
    print(sum(gen_obj))

    for idx in range(0, len(my_list)):
        my_list[idx] += 17
    gen_obj = (num for num in my_list if not sum_num_list(num) % 7)
    print(sum(gen_obj))


optimized()  # mem_diff = 0.02734375, time_diff = 0.13852836200000007


# Оптимизированная функция имеет значительный выигрыш по памяти
# за счет использования генераторов и lc


# Скрипт №3
# Неоптимизированный
@decor
def reform(lst):
    for price in lst:
        rub = int(price)
        penny = int((price - int(price)) * 100)
        print(f'{rub:02d} руб {penny:02d} коп', end=', ')
    print('')


prices = [46.7, 97.2, 34.84, 54, 779.52, 21.09, 13.3, 9.8, 55.06, 88.8]
reform(prices)  # mem_diff = 0.00390625, time_diff = 0.10465618500000007


# Оптимизированный
@decor
def reform(lst):
    res = (f'{int(price):02d} руб {int((price - int(price)) * 100):02d} коп '
           for price in lst)
    print(*res)


prices = [46.7, 97.2, 34.84, 54, 779.52, 21.09, 13.3, 9.8, 55.06, 88.8]
reform(prices) # mem_diff = 0,0 time_diff = 0.10492150099999997
# Оптимизированная функция имеет выигрыш по памяти за счет использования генератора
