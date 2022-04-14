"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой и по возможности самой лаконичной.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.

Без аналитики задание считается не принятым!
"""

from timeit import timeit
from collections import Counter

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


# def func_3():
#     num = max([(i, array.count(i)) for i in set(array)], key=lambda x: x[1])
#     return f'Чаще всего встречается число {num[0]}, ' \
#            f'оно появилось в массиве {num[1]} раз(а)'


def func_3():  # Конечно же подсмотрел во вчерашнем разборе дз
    num = max(array, key=array.count)
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {array.count(num)} раз(а)'


def func_4():
    dictionary = Counter(array)
    el = dictionary.most_common(1)
    return f'Чаще всего встречается число {el[0][0]}, ' \
           f'оно появилось в массиве {el[0][1]} раз(а)'


print(func_1(), timeit('func_1()', globals=globals()))
print(func_2(), timeit('func_2()', globals=globals()))
print(func_3(), timeit('func_3()', globals=globals()))
print(func_4(), timeit('func_4()', globals=globals()))

'''
3-яя и 4-ая версии: лаконичные - да, а вот быстрые совсем нет.
'''
