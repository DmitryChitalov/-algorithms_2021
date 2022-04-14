"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.

Без аналитики задание считается не принятым
"""
from timeit import timeit

array = [1, 3, 1, 3, 4, 5, 1, 2, 3, 5, 1, 4, 6]


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


# Вот так должно быть лучше


def func_3():
    elems = {array.count(v): v for v in set(array)}

    max_3 = max(elems.keys())
    return f'Чаще всего встречается число {elems[max_3]}, ' \
           f'оно появилось в массиве {max_3} раз(а)'


def memoize(f):
    cache = {}

    def decorate(*args):

        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]
    return decorate


@memoize
def func_1_mem():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


@memoize
def func_2_mem():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


@memoize
def func_3_mem():
    elems = {array.count(v): v for v in set(array)}

    max_3 = max(elems.keys())
    return f'Чаще всего встречается число {elems[max_3]}, ' \
           f'оно появилось в массиве {max_3} раз(а)'


print(
    timeit(
        'func_1()',
        setup='from __main__ import func_1',
        number=10000))
print(
    timeit(
        'func_2()',
        setup='from __main__ import func_2',
        number=10000))
print(
    timeit(
        'func_3()',
        setup='from __main__ import func_3',
        number=10000))
print('Ускорим работу этих функций ! ')
print('--------------------МЕМОИЗАЦИЯ--------------------')
print(
    timeit(
        'func_1_mem()',
        setup='from __main__ import func_1_mem',
        number=10000))
print(
    timeit(
        'func_2_mem()',
        setup='from __main__ import func_2_mem',
        number=10000))
print(
    timeit(
        'func_3_mem()',
        setup='from __main__ import func_3_mem',
        number=10000))
