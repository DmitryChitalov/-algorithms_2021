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
from timeit import timeit
from random import randint


array = [randint(1, 100) for i in range(20)]


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


def func_3():
    num = max(array, key=array.count)
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {array.count(num)} раз(а)'


print(func_1())
print(func_2())
print(func_3())
print(f'Время выполнения функции func_1: {timeit(stmt="func_1()", globals=globals())}')
print(f'Время выполнения функции func_2: {timeit(stmt="func_2()", globals=globals())}')
print(f'Время выполнения функции func_3: {timeit(stmt="func_3()", globals=globals())}')

# func_3 работает быстрее используется меньше операций
