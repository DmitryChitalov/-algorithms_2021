"""
Задание 4.
Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.
Сделайте профилировку каждого алгоритма через timeit
Попытайтесь написать третью версию, которая будет самой быстрой и по возможности самой лаконичной.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
Без аналитики задание считается не принятым!
"""

import timeit
from collections import Counter
import statistics
from statistics import mode

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
    c = Counter(array)
    result = c.most_common(1)
    for el, count in result:
        return f'Чаще всего встречается число {el}, ' \
               f'оно появилось в массиве {count} раз(а)'

def func_4():
    frequent = mode(array)
    max_3 = max(array) # в этом модуле так и не нашёл счётчик, max_3 неверен
    return f'Чаще всего встречается число {frequent}, ' \
           f'оно появилось в массиве {max_3} раз(а)'

print(func_1())
print(func_2())
print(func_3())
print(func_4())

# Профилировка

print('func_1:')
print(timeit.timeit("""def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'""", number=20000))

print('func_2:')
print(timeit.timeit("""def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'""", number=20000))

print('func_3:')
print(timeit.timeit("""def func_3():
    c = Counter(array)
    result = c.most_common(1)
    for el, count in result:
        return f'Чаще всего встречается число {el}, ' \
               f'оно появилось в массиве {count} раз(а)'""", number=20000))

print('func_4:')
print(timeit.timeit("""def func_4():
    frequent = mode(array)
    max_3 = max(array)
    return f'Чаще всего встречается число {frequent}, ' \
           f'оно появилось в массиве {max_3} раз(а)'""", number=20000))

"""
Ускорить задачу получилось через Counter.most_common
"""