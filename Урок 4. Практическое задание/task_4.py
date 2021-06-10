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
    counts = dict()
    for elem in array:
        if elem in counts:
            counts[elem] += 1
        else:
            counts[elem] = 1
    max_count = 0
    max_elem = None
    for elem in counts:
        if counts[elem] > max_count:
            max_elem = elem
            max_count = counts[elem]
    return f'Чаще всего встречается число {max_elem}, ' \
           f'оно появилось в массиве {max_count} раз(а)'

print(func_1())
print(func_2())
print(func_3())

print(timeit.timeit(lambda: func_1(), number=10000))
print(timeit.timeit(lambda: func_2(), number=10000))
print(timeit.timeit(lambda: func_3(), number=10000))

"""" в  связи  с  отсутствием   квадратичной   сложности   удалось  минимизировать   время"""