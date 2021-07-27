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
from memory_profiler import profile
from pympler import asizeof
from timeit import timeit
from collections import defaultdict
from recordclass import recordclass
from numpy import number
import sys

# 1 Рекурсия vs Цикл                                                MiB

@profile
def decor(func):                                                    # 0
    def wrapper(*argv):                                             # 0
        return func(*argv)                                          # 0
    return wrapper                                                  # 0

@ decor
def get_rev_number(number, rev_number = ''):                        # 0
    # базовый случай!!!
    if number == 0:                                                 # 0
        return rev_number                                           # 0
    else:
        # шаг рекурсии
        last_number = number % 10                                   # 0
        rev_number += str(last_number)                              # 0
        return get_rev_number(number // 10, rev_number)             # 0.2

@profile
def get_rev_number_2(number, rev_number = ''):                      # 0
    while number != 0:                                              # 0
        last_number = number % 10                                   # 0
        rev_number += str(last_number)                              # 0
        number = number // 10                                       # 0
    return rev_number                                               # 0

number_s = 1230
print(get_rev_number(number_s))
print(get_rev_number_2(number_s))
# print(
#     timeit(
#         "get_rev_number(number_s)",
#         setup="from __main__ import get_rev_number, number_s", number=1000000))
# print(
#     timeit(
#         "get_rev_number_2(number_s)",
#         setup="from __main__ import get_rev_number_2, number_s", number=1000000))

'''
1 000 000 повторений:
get_rev_number = 1.291
get_rev_number_2 = 1.012

Аналитика:

Замена Рекурсии на Цикл привела к снижению сложности и увеличению скорости 
обработки операций с факториальной O(n!) на линейную O(n).

@profile - показывает, что цикл не нагружает доп. элементы в Increment - что говорит о том,
 что дополнительной Опертивной памяти для хранения Итерации не требуется. 
'''

# 2 Изменение типа __slots__ в class

class HexNumber:
    def __init__(self, num_1,num_2):
        self.num_1 = num_1
        self.num_2 = num_2


simple_int_1 = '1a3'
simple_int_2 = '3de'
a = HexNumber(simple_int_1, simple_int_2)
print(asizeof.asizeof((a)))                                     # asizeof.asizeof = 376

class HexNumber:
    __slots__ = ('num_1', 'num_2')
    def __init__(self, num_1,num_2):
        self.num_1 = num_1
        self.num_2 = num_2


simple_int_1 = '1a3'
simple_int_2 = '3de'
a = HexNumber(simple_int_1, simple_int_2)
print(asizeof.asizeof((a)))                                     # asizeof.asizeof = 160

"""
Аналитика:

Использование __slots__ приводит к изменению типа данных для хранения.
По умолчанию используется dict, и так как его идентификаторы/ключи ХЕШируются,
данные занимают вдвое больше памяти, например, по сравнению с tuple!

asizeof.asizeof = 376 без использования __slots__
asizeof.asizeof = 160 с использования __slots__
"""

# 3 recordclass vs defaultdict

a = input('Введите первое число: ')
b = input('Введите второе число: ')

ddict = defaultdict(list)
ddict[1] = list(a)
ddict[2] = list(b)
print(ddict)

# c = hex(int(''.join(str(i) for i in ddict[1]), 16) * int(''.join(str(i) for i in ddict[2]), 16))
# d = hex(int(''.join(str(i) for i in ddict[1]), 16) + int(''.join(str(i) for i in ddict[2]), 16))
# print(f'Сумма: {list(d[2:].upper())}')
# print(f'Произведение: {list(c[2:].upper())}')

rec_val = recordclass('rec_val', ('x', 'y'))

rec_val = rec_val(x=list(a), y=list(b))
print(rec_val)

print(f'Объём занимаемой объектом recordclass памяти: {sys.getsizeof(rec_val)} байт(а)')
print(f'Объём занимаемой объектом ddict памяти: {sys.getsizeof(ddict)} байт(а)')

'''
Объём занимаемой объектом recordclass памяти: 40 байт(а)
Объём занимаемой объектом ddict памяти: 240 байт(а)

Аналитика:

Объем занимаемой памяти recordclass в 5 раз меньше, чем ddict.
В связи с чем, выполнение объемных алгоритмов будет испольняться в разы быстрее.

'''