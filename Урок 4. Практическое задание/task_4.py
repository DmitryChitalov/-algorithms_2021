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

array = [1, 2, 3, 4, 5, 1]


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'The most common number: {num}, ' \
           f'it has appeared in the array {m} times'


def func_2():
    new_array = []
    for elem in array:
        count = array.count(elem)
        new_array.append(count)
    m = max(new_array)
    num = array[new_array.index(m)]
    return f'The most common number: {num}, ' \
           f'it has appeared in the array {m} times'

def func_3():
    num = max(array, key=array.count)
    m = array.count(num)
    return f'The most common number: {num}, ' \
           f'it has appeared in the array {m} times'


print(func_1())
print(timeit("func_1()", globals=globals(), number=1000))

print(func_2())
print(timeit("func_2()", globals=globals(), number=1000))

print(func_3())
print(timeit("func_3()", globals=globals(), number=1000))
