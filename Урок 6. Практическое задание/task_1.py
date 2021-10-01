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

from timeit import default_timer
import memory_profiler
import numpy as np
from pympler import asizeof


def decor(func):
    def wrapper(*args, **kwargs):
        m1 = memory_profiler.memory_usage()
        t1 = default_timer()
        func(*args, **kwargs)
        time_diff = default_timer() - t1
        m2 = memory_profiler.memory_usage()
        mem_diff = m2[0] - m1[0]
        return f'Выполнение заняло: {mem_diff} MiB\nЗаняло времени: {time_diff}\n'

    return wrapper


######################################################################################################################
"""Урок 4. задание 2. Число наоборот """


@decor
def get_reverse_recurs(enter_num):
    return reverse_recurs(enter_num)


def reverse_recurs(enter_num, revers_num=''):
    if enter_num == 0:
        return print(f'Перевернутое число: {revers_num}')
    else:
        return reverse_recurs(enter_num // 10, revers_num + str(enter_num % 10))


@decor
def revers_while(enter_num, revers_num=''):
    while enter_num != 0:
        revers_num = revers_num + str(enter_num % 10)
        enter_num //= 10
    return print(f'Перевернутое число: {revers_num}')


num = 12345678905982370455820384028460284645294689234465330
print(f'Число наоборот:')
print(f'Рекурсия:\n{get_reverse_recurs(num)}')
print(f'Цикл:\n{revers_while(num)}')

"""
Число наоборот:
Перевернутое число: 03356443298649254648206482048302855407328950987654321
Рекурсия:
Выполнение заняло: 0.0625 MiB
Заняло времени: 0.000216227999999985

Перевернутое число: 03356443298649254648206482048302855407328950987654321
Цикл:
Выполнение заняло: 0.0 MiB
Заняло времени: 0.0001352130000000784

Повторные вызовы функции в рекурсивном методе существенно влияют на память т. к. результаты
каждого вызова функции сохраняются в памяти. цикл и быстрее рекурсии и занимеет меньше памяти"""

######################################################################################################################
"""Урок 4. задание 5. "Решето Эратосфена" """


@decor
def sieve_of_eratosthenes_list(i, n):
    prime_list = []
    sieve = set(range(2, n + 1))
    while sieve:
        prime = min(sieve)
        prime_list.append(prime)
        sieve -= set(range(prime, n + 1, prime))
    print(f'Размер списка: {asizeof.asizeof(prime_list)} байт')
    return print(f'{i}-е простое число: {prime_list[i - 1]}')


@decor
def sieve_of_eratosthenes_numpy(i, n):
    prime_list = np.array([])
    sieve = set(range(2, n + 1))
    while sieve:
        prime = min(sieve)
        prime_list = np.append(prime_list, prime)
        sieve -= set(range(prime, n + 1, prime))
    del sieve
    print(f'Размер numpy: {asizeof.asizeof(prime_list)} байт')
    return print(f'{i}-е простое число: {int(prime_list[i - 1])}')


num = 1200
length = 10000
print(f'\nРешето Эратосфена:')
print(f'Список: {sieve_of_eratosthenes_list(num, length)}')
print(f'Numpy: {sieve_of_eratosthenes_numpy(num, length)}')

'''
Решето Эратосфена:
Размер списка: 49336 байт
1200-е простое число: 9733
Список: Выполнение заняло: 0.59765625 MiB
Заняло времени: 0.06717837100000001

Размер numpy: 9952 байт
1200-е простое число: 9733
Numpy: Выполнение заняло: 0.3515625 MiB
Заняло времени: 0.07689301300000007

Уменьшение использования памяти достигаестя истользованием Numpy массива вместо обычного списка т. к. 
Numpy массив занимает существенно меньше места в памяти чем обычный списсок.
'''

######################################################################################################################
"""Урок 4. задание 5. Сложение и умножение двух шестнадцатиричных чисел """


class HexOp:
    def __init__(self, first_num, second_num):
        self.first_num = first_num
        self.second_num = second_num

    def __add__(self, other):
        return list(hex(int(''.join(self.first_num), 16) + int(''.join(other.second_num), 16)))[2:]

    def __mul__(self, other):
        return list(hex(int(''.join(self.first_num), 16) * int(''.join(other.second_num), 16)))[2:]


class HexOpSlots:
    __slots__ = ['first_num', 'second_num']

    def __init__(self, first_num, second_num):
        self.first_num = first_num
        self.second_num = second_num

    def __add__(self, other):
        return list(hex(int(''.join(self.first_num), 16) + int(''.join(other.second_num), 16)))[2:]

    def __mul__(self, other):
        return list(hex(int(''.join(self.first_num), 16) * int(''.join(other.second_num), 16)))[2:]


first_num_hex = 'afe34'
second_num_hex = 'eef1'

print(f'\nСложение и умножение двух шестнадцатиричных чисел:')

hex_obj = HexOp(first_num_hex, second_num_hex)
print(f'Обычный класс: {asizeof.asizeof(hex_obj)}')
hex_obj_slots = HexOpSlots(first_num_hex, second_num_hex)
print(f'Класс со слотами: {asizeof.asizeof(hex_obj_slots)}')
print(f'Сумма чисел:{HexOp(first_num_hex, second_num_hex) + HexOp(first_num_hex, second_num_hex)}')
print(
    f'Произведение чисел:{HexOp(first_num_hex, second_num_hex) * HexOp(first_num_hex, second_num_hex)}')

print(f'Сумма чисел:{HexOpSlots(first_num_hex, second_num_hex) + HexOpSlots(first_num_hex, second_num_hex)}')
print(
    f'Произведение чисел:{HexOpSlots(first_num_hex, second_num_hex) * HexOpSlots(first_num_hex, second_num_hex)}')

"""
Сложение и умножение двух шестнадцатиричных чисел:
Обычный класс: 392
Класс со слотами: 160
Сумма чисел:['b', 'e', 'd', '2', '5']
Произведение чисел:['a', '4', '2', 'a', 'd', 'a', '6', 'f', '4']

По умолчания для хранения данных используется словарь, __slots__ изменяет тип данных для хранения, в данном случае
на список, который потребляет меньше памяти чем словарь. Правда при этом теряется возможность добавлять 
новые атрибуты вне описания класса.
"""
