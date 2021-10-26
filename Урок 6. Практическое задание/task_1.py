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
from random import randint
from numpy import array


def dec(func):
    def wrapper(*args):
        start = memory_usage()
        res = func(*args)
        stop = memory_usage()
        print(f'{func.__name__}:        {res}', stop[0] - start[0])

    return wrapper


# Скрипт №1
def call_func(number):
    @dec
    def counter(number, result_1=0, result_2=0):
        if number == 0:
            return print(f'Even numbers: {result_1}. Odd numbers: {result_2}')
        if (number % 10) % 2 == 0:
            result_1 = result_1 + 1
        else:
            result_2 = result_2 + 1
        return counter(number // 10, result_1, result_2)

    return counter(number)


@dec
def counter_2(number):
    result_1 = 0
    result_2 = 0
    for i in str(number):
        i = int(i)
        if i % 2 == 0:
            result_1 = result_1 + 1
        else:
            result_2 = result_2 + 1

    return print(f'Even numbers: {result_1}. Odd numbers: {result_2}')


@dec
def counter_3(number):
    result_1, result_2 = 0, 0
    while number != 0:
        if (number % 10) % 2 == 0:
            result_1 = result_1 + 1
        else:
            result_2 = result_2 + 1
        number = number // 10
    return print(f'Even numbers: {result_1}. Odd numbers: {result_2}')


# number = randint(10 ** 10, 50 ** 10)
# call_func(number)
# counter_2(number)
# counter_3(number)
"""
Even numbers: 11. Odd numbers: 6
counter:        None 0.0
counter:        None 0.0
counter:        None 0.0
counter:        None 0.0
counter:        None 0.0
counter:        None 0.0
counter:        None 0.0
counter:        None 0.0
counter:        None 0.0
counter:        None 0.0
counter:        None 0.0
counter:        None 0.0
counter:        None 0.0
counter:        None 0.0625
counter:        None 0.0625
counter:        None 0.0625
counter:        None 0.0625
counter:        None 0.0625
Even numbers: 11. Odd numbers: 6
counter_2:        None 0.0
Even numbers: 11. Odd numbers: 6
counter_3:        None 0.0
При вызове рекурсивной функции занимается больше памяти, чем в цикле, так как происходит накопление запросов, 
как в стеке, поэтому я заменил рекурсии на цикл for и while.
"""


# Скрипт №2
# number = 123456789


def call_mirror(number):
    @dec
    def mirror_function(number, result=''):
        if number == 0:
            return print(result)
        x = str(number % 10)
        result = result + x
        return mirror_function(number // 10, result)

    return mirror_function(number)


@dec
def mirror_function_2(number):
    # number = str(number)
    result = ''
    while number != 0:
        x = str(number % 10)
        result = result + x
        number //= 10
    return print(result)


@dec
def mirror_function_3(number):
    number = str(number)
    return print(''.join(list(reversed(number))))


# call_mirror(number)
# mirror_function_2(number)
# mirror_function_3(number)
"""
987654321
mirror_function:        None 0.0
mirror_function:        None 0.0
mirror_function:        None 0.0
mirror_function:        None 0.0
mirror_function:        None 0.0
mirror_function:        None 0.0
mirror_function:        None 0.0
mirror_function:        None 0.0625
mirror_function:        None 0.0625
mirror_function:        None 0.0625
987654321
mirror_function_2:        None 0.0
987654321
mirror_function_3:        None 0.0
При вызове рекурсивной функции занимается больше памяти, чем в цикле, так как происходит накопление запросов, 
как в стеке, поэтаму я заменил рекурсии на цикл while а во второй я решил с помощью встоенной функцией.
"""


# Скрипт №3
@dec
def even_numbers(my_list):
    new_arr = {i for i in range(len(my_list)) if not my_list[i] % 2}
    return new_arr


@dec
def even_numbers_2(my_list):
    new_arr = [i for i in range(len(my_list)) if not my_list[i] % 2]
    return new_arr


@dec
def even_numbers_3(my_list):
    new_arr = array([i for i in range(len(my_list)) if not my_list[i] % 2])
    return new_arr


numbers = [i for i in range(1, 10 ** 5)]
# even_numbers(numbers)
# even_numbers_2(numbers)
# even_numbers_3(numbers)
"""
even_numbers 3.75
even_numbers_2 1.1484375
even_numbers_3 0.13671875
множество занимает очень много памяти,если заменить его на список или используя array от numpy, в данном примере,
можно значительно сэкономить память.
"""


# Скрипт №4
def call_t4():
    @dec
    def task_4(summ=0.0, x=1.0, n=0):
        if n == 0.0:
            n = int(input("Insert n please: "))
        summ = summ + x
        x = x / -2
        n = n - 1
        if n == 0:
            return print(summ)
        return task_4(summ, x, n)

    return task_4()


@dec
def task_4_1(n):
    summ = 0
    x = 1
    for i in range(n):
        summ = summ + x
        x = x / -2

    return print(summ)


@dec
def task_4_3(n):
    summ = 0
    x = 1
    while n:
        summ = summ + x
        x = x / -2
        n -= 1
    return print(summ)


# call_t4()
# task_4_1(3)
# task_4_3(3)
"""
0.75
task_4:        None 0.0
task_4:        None 0.00390625
task_4:        None 0.01953125
0.75
task_4_1:        None 0.0
0.75
task_4_3:        None 0.0
Как сказал выше, при вызове рекурсивной функции занимается больше памяти, чем в цикле, так как происходит накопление запросов, 
как в стеке, поэтаму я заменил рекурсии на цикл while и for.
"""
