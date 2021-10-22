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
    num = max(array, key=array.count)
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {array.count(num)} раз(а)'


def func_4():
    number, frequency = Counter(array).most_common(1)[0]
    return f'Чаще всего встречается число {number}, ' \
           f'оно появилось в массиве {frequency} раз(а)'


# print(func_1())
# print(func_2())
# print(func_3())
# print(func_4())

print(f'func_1: {timeit("func_1()", globals=globals(), number=1000000)}')
print(f'func_2: {timeit("func_2()", globals=globals(), number=1000000)}')
print(f'func_3: {timeit("func_3()", globals=globals(), number=1000000)}')
print(f'func_4: {timeit("func_3()", globals=globals(), number=1000000)}')

"""
Функции 1 и 2 менее быстрые со сложностью (n^2) т.к. это цикл в цикле
(цикл for и перебор элементов в цикле count) 
Функции 3 более быстрая, со сложностью (n) (через max).
сложность 4 функции (n log n) из-за сортировки в most_common.
Так что самая лаконичная и быстрая (из пердставленных сдесь)
это func_3.

func_1: 1.6201495000000001
func_2: 1.9460965
func_3: 1.3710503999999997
func_4: 1.5083662999999996
"""
