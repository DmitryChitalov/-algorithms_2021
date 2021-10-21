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
from memory_profiler import profile, memory_usage
from random import randint
from numpy import array


def dec(func):
    def wrapper(*args):
        start = memory_usage()
        res = func(*args)
        stop = memory_usage()
        print(f'{func.__name__}:        {res}', stop[0] - start[0])
    return wrapper


#################################################################################################
def call_func(number):
    @dec
    def check_digit_1(number, even=0, odd=0):
        if not number:
            return even, odd
        get_num = number % 10
        if get_num % 2 == 0:
            even += 1
        else:
            odd += 1
        return check_digit_1(number // 10, even, odd)
    return check_digit_1(number)


@dec
def check_digit_2(number, even=0, odd=0):
    for el in str(number):
        if int(el) % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd


@dec
def check_digit_3(number, even=0, odd=0):
    while number:
        if not number % 2:
            even += 1
        else:
            odd += 1
        number = number // 10
    return even, odd


# number_obj = randint(10**10, 50**10)
# call_func(number_obj)
# check_digit_2(number_obj)
# check_digit_3(number_obj)

"""
check_digit_1:        (8, 9) 0.0
check_digit_1:        None 0.00390625
check_digit_1:        None 0.00390625
check_digit_1:        None 0.00390625
check_digit_1:        None 0.00390625
check_digit_1:        None 0.00390625
check_digit_1:        None 0.00390625
check_digit_1:        None 0.00390625
check_digit_1:        None 0.00390625
check_digit_1:        None 0.00390625
check_digit_1:        None 0.00390625
check_digit_1:        None 0.00390625
check_digit_1:        None 0.00390625
check_digit_1:        None 0.00390625
check_digit_1:        None 0.00390625
check_digit_1:        None 0.00390625
check_digit_1:        None 0.00390625
check_digit_1:        None 0.00390625
check_digit_2:        (8, 9) 0.0
check_digit_3:        (8, 9) 0.0

Как видно, при вызове рекурсивной функции занимается больше памяти, чем в цикле, т.к. происходит накопление запросов, 
как в стеке.
"""
# ##################################################################################################


@dec
def func_1(nums):
    new_arr = {i for i in range(len(nums)) if not nums[i] % 2}
    return new_arr


@dec
def func_2(nums):
    new_arr = [i for i in range(len(nums)) if not nums[i] % 2]
    return new_arr


@dec
def func_3(nums):
    new_arr = array([i for i in range(len(nums)) if not nums[i] % 2])
    return new_arr


numbers = [i for i in range(1, 10**7)]
# func_1(numbers)
# func_2(numbers)
# func_3(numbers)
"""
func_1:         282.42578125
func_2:         194.39453125
func_3:         17.63671875
Как видно, множество занимает очень много памяти,заменив его на список или используя array, в данном примере,
 можно значительно сэкономить память.
"""

# ###################################################################################################


# @dec
def multiple7():
    numbers = []
    for i in range(1, 1001):
        if i % 2 == 1:
            numbers.append(i ** 3)
    sum_numbers = 0
    for number in numbers:
        summ = 0
        number_round = number
        while number_round:
            summ += number_round % 10
            number_round = number_round // 10
        if summ % 7 == 0:
            sum_numbers += number
    return sum_numbers


# @dec
def multiple7_two():
    def create_gen():
        for i in range(1, 1001):
            if i % 2 == 1:
                yield i**3
    numbers = create_gen()
    sum_numbers = 0
    for number in numbers:
        summ = 0
        num = number
        number_round = num
        while number_round:
            summ += number_round % 10
            number_round = number_round // 10
        if summ % 7 == 0:
            sum_numbers += num
    return sum_numbers


# @dec
def multiple7_thee():
    numbers = (i ** 3 for i in range(1, 1001) if i % 2 == 1)
    sum_numbers = 0
    for number in numbers:
        summ = 0
        number_round = number
        while number_round:
            summ += number_round % 10
            number_round = number_round // 10
        if summ % 7 == 0:
            sum_numbers += number
    return sum_numbers


# multiple7()
# multiple7_two()
# multiple7_thee()
"""
multiple7:        17485588610 0.00390625
multiple7_two:        17485588610 0.0
multiple7_thee:        17485588610 0.0
Оптимизация памяти произошла из-за замены списка генератором, который занимает меньше места
"""
