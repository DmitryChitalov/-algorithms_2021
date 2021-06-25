
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
    return f'Используя ф-ю func_1, чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Используя ф-ю func_2, чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'



# Статистика (statistics.mode(data))
# Функция mode() модуля statistics возвращает единственный наиболее распр-ный эле-т данных data
def func_3(array):
    return (mode(array))




# 1-ЫЙ замер:
print(f'Вариант 1 :', timeit("func_1", globals=globals(), number=1000))
# print(timeit("func_1", setup="from __main__ import func_1", number=1000)) # Аналог предыдущего

# 2-ОЙ замер:
print(f'Вариант 2 :', timeit("func_2", globals=globals(), number=1000))

# 3-ИЙ замер:
print(f'Вариант 3 :', timeit("func_3", globals=globals(), number=1000))

"""
Используя ф-ю func_1, чаще всего встречается число 1, оно появилось в массиве 3 раз(а)
Используя ф-ю func_2, чаще всего встречается число 1, оно появилось в массиве 3 раз(а)
Используя ф-ю func_3, чаще всего встречается число  1
Вариант 1 : 1.9299999999999873e-05
Вариант 2 : 2.5299999999998934e-05
Вариант 3 : 1.910000000000106e-05
"""

# Вариант из вебинара - хороший
def func(): # Через ф-ю max. Параметр key - указывает на поиск эл-та с максимальной частотой
    numb = max(array, key=array.count)
    return f'Чаще встречается число :  {numb}, всего {array.count(numb)} раза'

print(func_1())
print(func_2())
print(f'Используя ф-ю func_3, чаще всего встречается число ', func_3(array))
print(func())
