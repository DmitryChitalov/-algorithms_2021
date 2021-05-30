"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.

Без аналитики задание считается не принятым!
"""

from timeit import timeit
from collections import Counter, OrderedDict

array = [1, 3, 1, 3, 4, 5, 1]


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'func_1 - Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'func_2 - Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'

# моя версия решения № 1
def func_3():
    dict_obj = {array.count(val):val for val in set(array)}
    some_list = list(dict_obj.items())
    num = some_list[0][1]
    max_freq = some_list[0][0]
    return f'func_3 - Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {max_freq} раз(а)'

# моя версия решения № 2
def func_4():
    num = max(set(array), key=array.count)
    return f'func_4 - Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {array.count(num)} раз(а)'

print(func_1())
print(func_2())
print(func_3())
print(func_4())

print(f'Время выполнения функции func_1 - {timeit("func_1()", globals=globals())} секунды.')
print(f'Время выполнения функции func_2 - {timeit("func_2()", globals=globals())} секунды.')
print(f'Время выполнения функции func_3 - {timeit("func_3()", globals=globals())} секунды.')
print(f'Время выполнения функции func_4 - {timeit("func_4()", globals=globals())} секунды.')

"""
Выводы:
В первом моем варианте решения (func_3), в сравнениие с заданным решение func_1,
ускорить задачу не получилось, во втором варианте (func_4) ускорение получилось,
но оно оказалось не существенным.
"""
