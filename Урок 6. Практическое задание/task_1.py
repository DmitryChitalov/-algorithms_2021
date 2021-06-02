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

from memory_profiler import memory_usage, profile
from timeit import default_timer
from random import randint


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


@memory_time_profiler
def parity(number, count_par, count_not_par):
    if number == 0:
        return print(f'Количество четных и нечетных цифр в числе равно: ({count_par}, {count_not_par})')
    if (number % 2) == 1:
        count_not_par += 1
    else:
        count_par += 1
    parity(number // 10, count_par, count_not_par)


# @memory_time_profiler
# def even_and_uneven(num):
#     even = 0
#     uneven = 0
#     for i in str(num):
#         if int(i) % 2 == 0:
#             even += 1
#         else:
#             uneven += 1
#     return f'   even_and_uneven\n' \
#            f'Even: {even}\n' \
#            f'Uneven: {uneven}\n'
#
#
# usr_num = randint(900000, 1000000)
# usr_lst = [randint(0, 100) for el in range(1000)]
# print(usr_num)
