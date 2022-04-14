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
    res = max(Counter(array).items(), key=lambda i: i[1])
    return f'Чаще всего встречается число {res[0]}, ' \
           f'оно появилось в массиве {res[1]} раз(а)'


def func_4():
    res = max(array, key=array.count)
    return f'Чаще всего встречается число {res}, ' \
           f'оно появилось в массиве {array.count(res)} раз(а)'


print(func_1())
print(func_2())
print(func_3())
print(func_4())

n = 1000000
print(timeit('func_1()', number=n, globals=globals()))
print(timeit('func_2()', number=n, globals=globals()))
print(timeit('func_3()', number=n, globals=globals()))
print(timeit('func_4()', number=n, globals=globals()))

'''
Функции 1 и 4 сопостовимы по скорости (разница незначительна), но функция 4 более лаконична. Функция 3 лаконична, 
но время выполнения самое долгое, за счет выполнения кеширования, так как результат храниться в словаре.
'''
