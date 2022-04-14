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
    sorted_array = sorted(array, key=lambda x: array.count(x), reverse=True)
    return f'Чаще всего встречается число {sorted_array[0]}, ' \
           f'оно появилось в массиве {array.count(sorted_array[0])} раз(а)'


def func_4():
    elem = max(array, key=lambda x: array.count(x))
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {array.count(elem)} раз(а)'


print(func_1())
print(func_2())
print(func_3())
print(func_4())

print(timeit('func_1()', globals=globals()))
print(timeit('func_2()', globals=globals()))
print(timeit('func_3()', globals=globals()))
print(timeit('func_4()', globals=globals()))

""" В задании говорится найти более быстрый, но я увы не сумел, поэтому добавил 2 способа, чуть медлее
    Если я правильно понял, то у первой фунеции линейная сложность, а у встроеных сорт и макс - линейно-логарифмическая
    пробовал с большими массивами, протестировать время, посмотреть как изменится, но не ощутил разницы
"""
