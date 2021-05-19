from memory_profiler import memory_usage
from timeit import timeit
from random import randint

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


def memory_time(func):  # Пришлось подшаманить так, как default_timer везде показывал 0.
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        result = func(args[0])
        m2 = memory_usage()
        time_exec = timeit("func(args[0])", globals=locals(), number=100000)
        mem_diff = m2[0] - m1[0]  # Память во многих местах 0-вая. Не знаю как исправить

        print(f'    {func}\n'
              f'Memory: {mem_diff} MiB\n'
              f'Time: {round(time_exec, 5)} sec\n')
        return result

    return wrapper


def memoize(f):
    cache = {}

    def decorate(*args):

        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]

    return decorate


usr_num = randint(900000, 1000000)
usr_lst = [randint(0, 100) for el in range(1000)]
print(usr_num)


# Script 1


@memory_time
def even_and_uneven_shell(n):
    def even_and_uneven_rec(num, even=0, uneven=0):
        if num == 0:
            return f'   even_and_uneven_shell\n' \
                   f'Even: {even}\n' \
                   f'Uneven: {uneven}\n'
        elif num % 2 == 0:
            even += 1
        else:
            uneven += 1
        return even_and_uneven_rec(num // 10, even, uneven)

    return even_and_uneven_rec(n)


@memory_time
def even_and_uneven(num):
    even = 0
    uneven = 0
    for i in str(num):
        if int(i) % 2 == 0:
            even += 1
        else:
            uneven += 1
    return f'   even_and_uneven\n' \
           f'Even: {even}\n' \
           f'Uneven: {uneven}\n'


print(f'{even_and_uneven_shell(usr_num)}\n'
      f'{even_and_uneven(usr_num)}\n')

"""
Две эти функции вычисляют сколько чётных и нечётных чисел в введённой строке. Первая выполнена в виде рекурсии.
А вторая функция перебирает введённое число с помощью for.
Вторая функция выполняется быстрее и занимает меньше места в памяти.

        <function even_and_uneven_shell at 0x00000219BAF33C10>
    Memory: 0.0078125 MiB
    Time: 0.22568 sec

        <function even_and_uneven at 0x00000219BAF33D30>
    Memory: 0.0 MiB
    Time: 0.18538 sec

"""


# Script 2


@memory_time
def reverse_nums_shell(n):
    def reverse_nums(num):
        if len(str(num)) == 1:
            return num
        else:
            return str(num % 10) + str(reverse_nums(num // 10))

    return reverse_nums(n)


@memory_time
def reverse_nums(num):
    return str(num)[::-1]


print(f'    reverse_nums_shell\n'
      f'{reverse_nums_shell(usr_num)}\n'
      f'    reverse_nums\n'
      f'{reverse_nums(usr_num)}\n')

"""
Две эти функции переворачивают введённое число. Первая выполнена в виде рекурсии.
А вторая функция перебирает введённое число с помощью среза(если [::-1] к ним относится).
Вторая функция выполняется быстрее и занимает меньше места в памяти.

        <function reverse_nums_shell at 0x00000219BAF36F70>
    Memory: 0.0 MiB
    Time: 0.38751 sec

        <function reverse_nums at 0x00000219BAF36E50>
    Memory: 0.0 MiB
    Time: 0.05538 sec

"""


# Script 3

@memory_time
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return True  # new_arr  (чтобы не забивать консоль боьшим списком)


@memory_time
def func_2(nums):
    result = list(filter(lambda x: x % 2 == 0, nums))
    return True  # result   (чтобы не забивать консоль боьшим списком)


print(f'    func_1\n'
      f'{func_1(usr_lst)}\n'
      f'    func_2\n'
      f'{func_2(usr_lst)}\n')

"""
Две эти функции сохраняют в массиве индексы четных элементов другого массива.
Первая функция перебирает введённое число с помощью for.
А вторая функция с помощью filter и lambda.
Первая функция выполняется быстрее, но занимает больше места в памяти.

        <function func_1 at 0x000002E5FB771CA0>
    Memory: 0.0078125 MiB
    Time: 8.54742 sec

        <function func_2 at 0x000002E5FB771DC0>
    Memory: 0.0 MiB
    Time: 10.23487 sec

"""


# Script 4

@memory_time
def recursive_reverse_shell(n):
    def recursive_reverse(number):
        if number == 0:
            return ''
        return f'{str(number % 10)}{recursive_reverse(number // 10)}'

    return recursive_reverse(n)


@memory_time
def recursive_reverse_mem_shell(n):
    @memoize
    def recursive_reverse(number):
        if number == 0:
            return ''
        return f'{str(number % 10)}{recursive_reverse(number // 10)}'

    return recursive_reverse(n)


print(f'    recursive_reverse\n'
      f'{recursive_reverse_shell(usr_num)}\n'
      f'    recursive_reverse_mem\n'
      f'{recursive_reverse_mem_shell(usr_num)}\n')

"""
Две эти функции реверсируют число. Обе выполнены рекурсией(в оболочках), но вторая с декоратором @memoize
Первая(без @memoize) функция выполняется быстрее(что для меня удевительно), но занимает больше места в памяти.

        <function recursive_reverse_shell at 0x0000024F52632D30>
    Memory: 0.0078125 MiB
    Time: 0.27764 sec
    
        <function recursive_reverse_mem_shell at 0x0000024F52632E50>
    Memory: 0.0 MiB
    Time: 0.56427 sec

"""
