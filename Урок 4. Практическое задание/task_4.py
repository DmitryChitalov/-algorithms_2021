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
from itertools import count

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
    elem = max(array, key=array.count)
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {array.count(elem)} раз(а)'


print(func_1())
print(func_2())
print(func_3())


print(timeit("func_1()", globals=globals(), number=1000))
print(timeit("func_2()", globals=globals(), number=1000))
print(timeit("func_3()", globals=globals(), number=1000))
"""
func_1: 0.0037176000000000015
func_2: 0.004517199999999999
func_3: 0.0034602999999999995
Второе решение самое медленное, так как используется цикл, в цикле производится подсчет количества 
элементов, а потом еще медленная функция append. Первый вариант быстрее, так как не используется дополнительный массив
и функция append для его заполнения.
Третий вариант такой же быстрый как первый, но выглядит более лаконично,так как использованы только 
стандартные функции языка.
"""