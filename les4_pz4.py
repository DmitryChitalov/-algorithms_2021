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
    obj = Counter(array)
    return f'Чаще всего встречается число {obj.most_common()[0][0]}, ' \
           f'оно появилось в массиве {obj.most_common()[0][1]} раз(а)'


def func_4():
    x = max(array, key=array.count)
    return f'Чаще всего встречается число {x}, ' \
           f'оно появилось в массиве {array.count(x)} раз(а)'


print(timeit('func_1()', globals=globals()))    # 1.0708195999999999
print(timeit('func_2()', globals=globals()))    # 1.4214178000000002
print(timeit('func_3()', globals=globals()))    # 2.5634520999999997
print(timeit('func_4()', globals=globals()))    # 1.1268389999999995

# Самым быстрым решением оказалось перебор со встроенной функцией count,
# самым медленным - с Counter, который много времени тратит на создание словаря
# Ускорить задачу у меня не получилось: лаконичные решения через Counter и функцию max
# не дали ускорения работы.
