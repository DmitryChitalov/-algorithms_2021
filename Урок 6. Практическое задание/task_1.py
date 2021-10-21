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
import random
from timeit import timeit
from memory_profiler import profile
from pympler import asizeof



#
# # рекурсия
# @profile
# def even_odd(number, even=0, odd=0):
#     if number == 0:
#         return even, odd
#     else:
#         if number % 2 == 0:
#             even = even + 1
#         else:
#             odd = odd + 1
#         return even_odd(number // 10, even, odd)
#
#
# # цикл
# @profile
# def even_odd_2(number, even=0, odd=0):
#     while number != 0:
#         if number % 2 == 0:
#             even += 1
#         else:
#             odd += 1
#         number = number // 10
#     return even, odd
#
# number = 123
# print(even_odd(number ))
# print(even_odd_2(number))

# print('Время выполениея для even_odd:',
#    timeit(
#        "even_odd(number)",
#        globals=globals(),
#        number=1000000))

# print('Время выполениея для even_odd_2:',
#     timeit(
#         "even_odd_2(number)",
#         globals=globals(),
#         number=1000000))
"""
Для 1 000 000 повторений:
even_odd = 0.6332627, Mem usage 19.3 MiB ,Increment 19.3 MiB 
even_odd_2 = 0.40217579999999986, Mem usage 19.3 MiB ,Increment 19.3 MiB 


В реализация через цикл время выполения снижается по сравнению с рекурсией и уменьшается сложность в О-натации.
Замеры памяти показали что цикл не увеличивает Increment, это значит циклу не требуется больше оперативной памяти для хранения!
"""


# @profile
# def get_revers_number(number, rev_number=''):
#    if number == 0:
#        return rev_number
#    else:
#         last_number = number % 10
#         rev_number = rev_number + str(last_number)
#         return get_revers_number(number // 10, rev_number)
#
# Enter_number = 123123890
# print(get_revers_number(123123890))

#################################################################################

# #@profile
# def get_revers_number_2(number, rev_number=''):
#    while number != 0:
#        last_number = number % 10
#        rev_number = rev_number + str(last_number)
#        number = number // 10
#    return rev_number
#
# Enter_number = 123123890
# print(get_revers_number_2(Enter_number))
#
#
# print(
#     timeit(
#         "get_revers_number_2(Enter_number)",
#         setup="from __main__ import get_revers_number_2, Enter_number", number=1000000))
#
# print(
#     timeit(
#         "get_revers_number(Enter_number)",
#         setup="from __main__ import get_revers_number, Enter_number", number=1000000))

"""
@profile - показывает, что цикл не нагружает доп. элементы в Increment - что говорит о том,
что дополнительной Опертивной памяти для хранения Итерации не требуется. 
"""


# class HexNumber:
#    def __init__(self, num_1, num_2):
#        self.num_1 = num_1
#        self.num_2 = num_2
#
#
# simple_int_1 = '1a3'
# simple_int_2 = '3de'
# a = HexNumber(simple_int_1, simple_int_2)
# print(asizeof.asizeof((a)))
#
#
# class HexNumber:
#    __slots__ = ('num_1', 'num_2')
#
#    def __init__(self, num_1, num_2):
#        self.num_1 = num_1
#       self.num_2 = num_2
#
#
# simple_int_1 = '1a3'
# simple_int_2 = '3de'
# a = HexNumber(simple_int_1, simple_int_2)
# print(asizeof.asizeof((a)))

"""
__slots__ изменяет тип данных для хранения, по умолчанию использщуется dict , а т.к. ключи хешируются ,
 данные занимаю  больше памяти.
class HexNumber asizeof.asizeof = 376
class HexNumber __slots__ asizeof.asizeof = 160
"""