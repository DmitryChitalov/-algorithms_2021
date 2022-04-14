"""
Задание 4.
Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.
Сделайте профилировку каждого алгоритма через timeit
Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
Без аналитики задание считается не принятым!
"""
import collections
from timeit import timeit

array = [1, 3, 1, 3, 4, 5, 1]


def func_1():  # O(n)
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():  # O(n)
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def my_func():  # O(n)
    most_common = max(array, key=array.count)
    return f'Чаще всего встречается число {most_common}, ' \
           f'оно появилось в массиве {array.count(most_common)} раз(а)'


print(func_1())
print(func_2())
print(my_func())

print(f'Время работы первого алгоритма: {timeit("func_1()", globals=globals(), number=100)}.')
print(f'Время работы второго алгоритма: {timeit("func_2()", globals=globals(), number=100)}.')
print(f'Время работы третьего алгоритма: {timeit("my_func()", globals=globals(), number=100)}.')
'''
Время работы первого алгоритма: 0.0009432999999999941.
Время работы второго алгоритма: 0.0009664000000000061.
Время работы третьего алгоритма: 0.0007362999999999953.

Несмотря на одинаковую сложность, последний вариант работает быстрее, т.к. в нём не испозуется append/математические 
операции
'''
