"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.

Без аналитики задание считается не принятым
"""

import random
from timeit import timeit

array = [1, 3, 1, 3, 4, 5, 1]
array1 = [random.randint(1, 10) for i in range(1000)]


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


print(func_1())
print(func_2())

print(timeit("func_1()", setup='from __main__ import func_1', number=100000))
print(timeit("func_2()", setup='from __main__ import func_2', number=100000))

"""
Чаще всего встречается число 1, оно появилось в массиве 3 раз(а)
Чаще всего встречается число 1, оно появилось в массиве 3 раз(а)
0.10597874701488763
0.1286234069848433


второй алгоритм работает дольше за счет того, что дополнительно вычсиляется максимум в массиве, на больших данных
будет значимтельно увеличиваться время

улучшим первый алгоритм за счет кеша:
"""


def func_3():
    m = 0
    num = 0
    cache = {}
    for i in array:
        if i not in cache:
            count = array.count(i)
            cache[i] = count

            if count > m:
                m = count
                num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


print(timeit("func_3()", setup='from __main__ import func_3', number=100000))
"""
время выполнения 0.008754862996283919, что значительно быстрее предыдущих вариантов
"""
