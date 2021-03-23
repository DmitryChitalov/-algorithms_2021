from timeit import timeit
import cProfile
"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.

Без аналитики задание считается не принятым
"""

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


print(func_1())
print(timeit('func_1()', globals=globals(), number=10000))
print(func_2())
print(timeit('func_2()', globals=globals(), number=10000))

cProfile.run('func_1()')
cProfile.run('func_2()')


def my_function():
    maximum = 0
    elem = 0
    my_set = set(array)
    for elems in my_set:
        if array.count(elems) > maximum:
            maximum = array.count(elems)
            elem = elems
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {maximum} раз(а)'


print(timeit('my_function', globals=globals(), number=10000))
print(my_function())

"""
В моей функции мы используем множество, чтобы убрать проверку повтора в массиве из-за этого повышаем скорость.
"""