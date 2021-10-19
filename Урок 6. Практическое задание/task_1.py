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

from timeit import timeit
from memory_profiler import profile


@profile
def decor(func):
    def wrapper(*argv):
        return func(*argv)
    return wrapper

@ decor
def get_rev_number(number, rev_number = ''):

    if number == 0:
        return rev_number
    else:

        last_number = number % 10
        rev_number += str(last_number)
        return get_rev_number(number // 10, rev_number)

@profile
def get_rev_number_2(number, rev_number = ''):
    while number != 0:
        last_number = number % 10
        rev_number += str(last_number)
        number = number // 10
    return rev_number

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

@profile
def get_revers_number(number, rev_number=''):
    if number == 0:
        return rev_number
    else:
        last_number = number % 10
        rev_number = rev_number + str(last_number)
        return get_revers_number(number // 10, rev_number)


print(get_revers_number(123123890737460787))

@profile
def get_revers_number_2(number, rev_number_2=''):
    while number != 0:
        last_number = number % 10
        rev_number = rev_number_2 + str(last_number)
        number = number // 10
    return rev_number_2

print(get_revers_number_2(123123890737460787))