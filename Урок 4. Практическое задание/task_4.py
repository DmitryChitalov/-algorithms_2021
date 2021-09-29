"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой и по возможности самой лаконичной.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.

Без аналитики задание считается не принятым!
"""

from timeit import timeit, default_timer, repeat
from pprint import pprint

array = [1, 3, 1, 3, 4, 5, 1]
RETRIES, COUNTS = 100, 100000


def tst(r):
    def time_it(func):
        def wrapper():
            t = 0
            for i in range(r):
                start = default_timer()
                res = func()
                delta = default_timer() - start
                t += delta
            return ' '.join([func.__name__, res, f'{t:10.5f}'])

        return wrapper

    return time_it


@tst(COUNTS)
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


@tst(COUNTS)
def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


@tst(COUNTS)
def func_3():
    cache = dict()
    for el in array:
        if el in cache:
            cache[el] = cache[el] + 1
        else:
            cache.setdefault(el, 1)
    res = tuple(((x, y) for x, y in filter(lambda x: cache[x[0]] == max(cache.values()), cache.items())))[0]
    return f'Чаще всего встречается число {res[0]}, ' \
           f'оно появилось в массиве {res[1]} раз(а)'


@tst(COUNTS)
def func_4():
    m, num = sorted([(array.count(x), x) for x in array], key=max)[0]
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


@tst(COUNTS)
def func_5():
    num = max(array, key=array.count)
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {array.count(num)} раз(а)'


print(func_1())
print(func_2())
print(func_3())
print(func_4())
print(func_5())

'''
func_1 Чаще всего встречается число 1, оно появилось в массиве 3 раз(а)    0.50406
func_2 Чаще всего встречается число 1, оно появилось в массиве 3 раз(а)    0.62538
func_3 Чаще всего встречается число 1, оно появилось в массиве 3 раз(а)    1.82277
func_4 Чаще всего встречается число 1, оно появилось в массиве 3 раз(а)    1.14420

Мной написанные алгоритмы 3 и 4 оказались хуже по производительности, однако
алгоритм 4 на мой вкус более лаконичен за счет применения LC
'''
