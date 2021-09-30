#!/usr/bin/env python3

from collections import defaultdict, Counter
from timeit import timeit

"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой и по возможности самой лаконичной.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.

Без аналитики задание считается не принятым!
"""

array = [1, 3, 1, 3, 4, 5, 1]

'''
O(n)
'''
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

'''
O(n^2)
В цикле вызывается метод count, медленнее первого
'''
def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'

'''
O(n)
Используем встроенные функции
'''
def func_3():
    elem = max(array, key=array.count)
    count = array.count(elem)
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {count} раз(а)'


print(f"func_1: {timeit('func_1()', number=100000, globals=globals())}")
print(f"func_2: {timeit('func_2()', number=100000, globals=globals())}")
print(f"func_3: {timeit('func_3()', number=100000, globals=globals())}")



print(func_1())
print(func_2())
print(func_3())

'''
Написать вункцю с самым быстрым исполнением не получилось

'''
