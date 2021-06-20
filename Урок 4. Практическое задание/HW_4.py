import random
from timeit import timeit

# сложность зависит от кол-ва элементов в range (n)
array = [random.randint(0, 10) for el in range(10)]


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
    n = max(array)
    cnt = array.count(n)
    return f'Чаще всего встречается число {n}, ' \
           f'оно появилось в массиве {cnt} раз(а)'


print(timeit('func_1()', globals=globals()))  # 1.7151537000000001
print(timeit('func_2()', globals=globals()))  # 2.2032047
print(timeit('func_3()', globals=globals()))  # 0.5816053999999999

"""
ИТОГ: первые два способа используют совершенно бесполезные итераторы
создают новые списки и т.д.
В 3-ем способе использовано ровно то, что требуется для выполнения задачи.
Соответсвенно такая ф-ция быстрее остальных.
"""
