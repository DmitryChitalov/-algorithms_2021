"""
Задание 4.
Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.
Сделайте профилировку каждого алгоритма через timeit
Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
Без аналитики задание считается не принятым!
"""
import timeit
import numpy as np
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


def func_3():
    elem = list(Counter(array).most_common(1)[0])[0]
    max_3 = list(Counter(array).most_common(1)[0])[1]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_3} раз(а)'


def func_4():
    counts = np.bincount(array)
    elem = np.argmax(counts)
    max_4 = max(counts)
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_4} раз(а)'

def func_5():
    elem = max(array, key=array.count)
    max_5 = array.count(elem)
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_5} раз(а)'


print(func_1())
print(func_2())
print(func_3())
print(func_4())
print(func_5())

print(f'func_1 - {timeit.timeit("func_1", globals=globals(), number=1000)} сек.')
print(f'func_2 - {timeit.timeit("func_2", globals=globals(), number=1000)} сек.')
print(f'func_3 - {timeit.timeit("func_3", globals=globals(), number=1000)} сек.')
print(f'func_4 - {timeit.timeit("func_4", globals=globals(), number=1000)} сек.')
print(f'func_5 - {timeit.timeit("func_5", globals=globals(), number=1000)} сек.')

'''
func_1 - 2.2100000000024878e-05 сек.
func_2 - 1.8099999999965366e-05 сек.
func_3 - 1.669999999998062e-05 сек.
func_4 - 1.940000000000275e-05 сек.
func_5 - 1.799999999996249e-05 сек.

Наиболее медленной оказалась func_1 с циклом for, потом func_4 с использованием numpy, функции func_2 (использует цикл for) 
и func_5 (с использованием метода max) отработали почти одинаково. Самой быстрой оказалась func_3 с использованием 
коллекции Counter
'''