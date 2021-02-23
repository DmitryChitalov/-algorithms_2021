"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.

Без аналитики задание считается не принятым
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


# array = [1, 3, 1, 3, 4, 5, 1]
def func_3():
    keys = set(array)
    max_3 = 0
    elem = 0
    for key in keys:
        count = array.count(key)
        if count > max_3:
            max_3 = count
            elem = key
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_3} раз(а)'


print(func_1())
print(func_2())
print(func_3())
print(timeit('func_1()', globals=globals()))
print(timeit('func_2()', globals=globals()))
print(timeit('func_3()', globals=globals()))

# получилось ускорить за счет того, что колличество повторений рассчитывалось недля каждой цифры в списке, а для каждой
# цифры в множестве, что уменьшило количество операций
