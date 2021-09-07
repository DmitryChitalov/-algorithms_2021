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

import memory_profiler
from timeit import default_timer
import sys
from pympler import asizeof
from numpy import array


def decor(func):
    def wrapper(*args, **kwargs):
        m1 = memory_profiler.memory_usage()
        start_time = default_timer()
        res = func(args[0])
        m2 = memory_profiler.memory_usage()
        print(f'memory: {m2[0] - m1[0]}, time: {default_timer() - start_time}')
        return res

    return wrapper


#############################################################################################
# Вариант1. Задание с курса "Основы языка Python"
# Создать список, состоящий из кубов нечётных чисел от 0 до 1000:
# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7
@decor
def old_version(n):
    my_list = []
    full_summ = 0
    for i in range(1, n + 1, 2):
        my_list.append(i ** 3)
    for i in my_list:
        num = i
        sum_num = 0
        while num > 0:
            sum_num += num % 10
            num //= 10
        if sum_num % 7 == 0:
            full_summ += i
    print(full_summ)


def nums_generator(max_num):
    for i in range(1, max_num + 1, 2):
        num = i ** 3
        sum_num = 0
        while num > 0:
            sum_num += num % 10
            num //= 10
        yield i ** 3 if sum_num % 7 == 0 else 0


@decor
def new_version(n):
    nums_gen = nums_generator(n)
    full_summ = 0

    for _ in range(1, n + 1, 2):
        num = next(nums_gen)
        full_summ += num
    print(full_summ)


old_version(1000)  # memory: 0.07421875, time: 0.10349790000000003
new_version(1000)  # memory: 0.0, time: 0.10015699999999994


# Оптимизация алгоритма с помощью генератора. Для данной ситуации, где нет необходимости хранить значения массива,
# подходит хорошо, памяти опрактически не занимает, а вот по времени выиграть не удалось
#############################################################################################

# Задание из курса алгоритмов 2 урок, рекурсия
def count_even_odd_numbs(number, even=0, odd=0):
    if number == 0:
        return even, odd
    else:
        if number % 10 % 2 == 0:
            even += 1
        else:
            odd += 1
        return count_even_odd_numbs(number // 10, even, odd)


@decor
def main_f(num):
    print(f'Четных и нечетных чисел: {count_even_odd_numbs(num)}')


@decor
def count_even_odd_numbs2(number, even=0, odd=0):
    while number > 0:
        if number % 10 % 2 == 0:
            even += 1
        else:
            odd += 1
        number //= 10
    return even, odd


main_f(66555230)  # memory: 0.00390625, time: 0.1002071000000001
print(f'Четных и нечетных чисел: {count_even_odd_numbs2(6655523002)}')  # memory: 0.0, time: 0.10012310000000002


# Вывод: Отказ от рекурсии позволил сэкономить память

#############################################################################################
# Вариант 3. Задание из Основ, применяем слоты
class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f"{self.day:02}.{self.month:02}.{self.year:04}"


date_1 = Date(28, 2, 2021)

print(asizeof.asizeof(date_1))  # 416


class Date:
    __slots__ = ('day', 'month', 'year')

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f"{self.day:02}.{self.month:02}.{self.year:04}"


date_1 = Date(28, 2, 2021)

print(asizeof.asizeof(date_1))  # 152


# Использование слотов в ООП существенно экономит память

#############################################################################################
# Вариант 4 (Задание из 4-го урока)
@decor
def func_3(nums):
    return [i for i in range(0, len(nums), 2)]


@decor
def func_4(nums):
    return array([i for i in range(0, len(nums), 2)])


nums = [num ** 2 for num in range(1000000)]

func_3(nums)  # memory: 19.3828125, time: 0.12074570000000007
func_4(nums)  # memory: 1.96875, time: 0.17786880000000016

# Использование модуля numpy - переход к array вместо list - наглядная экономия памяти, но работает это только на
# больших объемах данных, при этом в ущерб времени, правда небольшой
