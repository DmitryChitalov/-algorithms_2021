"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой и по возможности самой лаконичной.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.

Без аналитики задание считается не принятым!
"""
from collections import Counter
import timeit

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


def func_my():
    c = Counter()
    for i in array:
        c[i] += 1
    return f'The most common number {tuple(c.keys())[0]}, ' \
           f'it has appeared in the array {tuple(c.values())[0]}'



print(func_my())
print(func_1())
print(func_2())

print(min(timeit.repeat('func_1', globals=globals(), repeat=10, number=(10**6))))
print(min(timeit.repeat('func_2', globals=globals(), repeat=10, number=(10**6))))
print(min(timeit.repeat('func_my', globals=globals(), repeat=10, number=(10**6))))


""" В ходе профилирование было установленно, самый быстрый алгоритм func_my.
func_1 медленнее func_2 но разница не существена
"""