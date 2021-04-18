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
from timeit import default_timer


#  Реализаия декоратора для подсчета статистики по ресурсам
def profile_ext(func):
    def wrapped(*args):
        v_begin_time = default_timer()
        v_begin_memory = memory_usage()
        ret = func(*args)
        v_end_time = default_timer()
        v_end_memory = memory_usage()
        print(f'Затрачено на вызов функции {func.__name__}: {v_end_time - v_begin_time} секунд, '
              f'иcпользовано: {v_end_memory[0] - v_begin_memory[0]} Mib')
        return ret

    return wrapped


@profile_ext
def factorial_as_generator(n):
    a = 1
    for i in range(1, n + 1):
        a *= i
        yield a


@profile_ext
def factorial_as_while(n):
    factorial = 1
    ret = [1]
    while n > 1:
        factorial *= n
        ret.append(factorial)
        n -= 1
    return ret


# Расчет списка чисел факториала c использованием yield
factorial_as_generator(10000)
# Расчет списка чисел факториала c использованием while
factorial_as_while(10000)
"""
Затрачено на вызов функции factorial_as_generator: 0.1003116 секунд, иcпользовано: 0.0078125 Mib
Затрачено на вызов функции factorial_as_while: 0.18381719999999996 секунд, иcпользовано: 80.59765625 Mib
ВЫВОД:
Использовние памяти при выборе генератора гораздо более эффективно за счет ее выыделения только тогда, когда ребуется 
ноое значчение итератора.
"""

import random
import collections

v_list = [{random.randint(1, 10000), random.randint(1, 10000)} for _ in range(1, 100000)]
v_deque = collections.deque(v_list)


@profile_ext
def appendleft_list(v_cnt):
    for _ in range(v_cnt):
        v_list.insert(0, {random.randint(1, 10000), random.randint(1, 10000)})


@profile_ext
def appendleft_deque(v_cnt):
    for _ in range(v_cnt):
        v_deque.appendleft({random.randint(1, 10000), random.randint(1, 10000)})


appendleft_list(100000)
appendleft_deque(100000)

"""
Затрачено на вызов функции appendleft_list: 8.9783721 секунд, иcпользовано: 30.2578125 Mib
Затрачено на вызов функции appendleft_deque: 0.36521130000000035 секунд, иcпользовано: 28.66015625 Mib
ВЫВОД:
Существенное ускорение операции добавления слева при использовании deque по сравнению со списком не
зависит от использование памяти. Более того, несколько замеров показало, что использование deque 
стабильно потребляет меньше пямяти. Можно сделать вывод, ччто ускорение функиональности расширения списка слева
осуществлено не за счет избыточного использования памяти.
"""


def pow2(x):
    return x * x


#  Генерация списка с помощью цикла
@profile_ext
def list_for(n):
    l = []
    for x in range(n):
        l.append(x * x)
    return l


@profile_ext
def list_for_func(n):
    l = []
    for x in range(n):
        l.append(pow2(x))
    return l


#  Генерация списка с помощью списковых включений
@profile_ext
def list_compr(n):
    return [x * x for x in range(n)]


@profile_ext
def list_compr_func(n):
    return [pow2(x) for x in range(n)]


#  Генерация списка с помощью map и лямбды
@profile_ext
def list_map_lambda(n):
    return list(map(lambda x: x * x, range(n)))


@profile_ext
def list_map_func(n):
    return list(map(pow2, range(n)))


list_for(10000000)
list_for_func(10000000)
list_compr(10000000)
list_compr_func(10000000)
list_map_lambda(10000000)
list_map_func(10000000)

"""
Затрачено на вызов функции list_for: 1.1015826000000004 секунд, иcпользовано: 384.109375 Mib
Затрачено на вызов функции list_for_func: 1.6511969999999998 секунд, иcпользовано: 385.94921875 Mib
Затрачено на вызов функции list_compr: 0.8289897999999987 секунд, иcпользовано: 386.01953125 Mib
Затрачено на вызов функции list_compr_func: 1.2807722000000012 секунд, иcпользовано: 386.015625 Mib
Затрачено на вызов функции list_map_lambda: 1.2425701999999994 секунд, иcпользовано: 386.19921875 Mib
Затрачено на вызов функции list_map_func: 1.1471911000000006 секунд, иcпользовано: 386.12109375 Mib
ВЫВОД:
Сравнили шесть варинтов формирования списка с простейшей арфиметической операцией.
Использование памяти примерно везде одинаково, но самый простой вариант с использованием цикла стабильно 
потребляет меньше памяти, в то время как скорость ожидаемо выше при использовании списковых включений. 
Вероятно, уменьшение потребления памяти при использовании циклов вызвано тем, что память выделяется только 
по требованию при каждой итерации. 
"""
