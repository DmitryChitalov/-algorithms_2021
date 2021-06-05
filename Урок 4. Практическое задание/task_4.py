"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.

Без аналитики задание считается не принятым!
"""
import numpy as np
from collections import Counter
from timeit import timeit


array = [1, 3, 1, 3, 4, 5, 1]


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


def builtin_comm():
    return f'Чаще всего встречается число {max(array, key=array.count)}, '\
           f'оно появилось в массиве {array.count(1)} раз(а)'


def np_comm():
    counts = np.bincount(array)
    return f'Чаще всего встречается число {np.argmax(counts)}, ' \
           f'оно появилось в массиве {max(counts)} раз(а)'


def col_comm():
    cnt = Counter(array)
    return f'Чаще всего встречается число {cnt.most_common()[0][0]}, ' \
           f'оно появилось в массиве {cnt.most_common()[0][1]} раз(а)'


print(func_1())
print(f'Время выполнения func_1: {timeit("func_1", globals=globals(), number=100000000)}')

print(func_2())
print(f'Время выполнения func_2: {timeit("func_2", globals=globals(), number=100000000)}')

print(builtin_comm())
print(f'Время выполнения builtin_comm: {timeit("builtin_comm", globals=globals(), number=100000000)}')

print(np_comm())
print(f'Время выполнения np_comm: {timeit("np_comm", globals=globals(), number=100000000)}')

print(col_comm())
print(f'Время выполнения col_comm: {timeit("col_comm", globals=globals(), number=100000000)}')

"""
Чаще всего встречается число 1, оно появилось в массиве 3 раз(а)
Время выполнения func_1: 1.784944
Чаще всего встречается число 1, оно появилось в массиве 3 раз(а)
Время выполнения func_2: 1.9597167
Чаще всего встречается число 1, оно появилось в массиве 3 раз(а)
Время выполнения builtin_comm: 1.7104962999999995
Чаще всего встречается число 1, оно появилось в массиве 3 раз(а)
Время выполнения np_comm: 1.5559127999999998
Чаще всего встречается число 1, оно появилось в массиве 3 раз(а)
Время выполнения col_comm: 1.5346071000000006

C помощью модуля collections получилось ускорить задачу, т.к у collections под капотом словарь с более расширенным 
функционалом.
"""