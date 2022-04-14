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
import collections

array = [1, 3, 1, 3, 4, 5, 1, 3, 3, 4, 5, 5, 4, 2, 2, 5, 5]


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
    c_count = collections.Counter()
    for num in array:
        c_count[num] += 1
    return f'Чаще всего встречается число {c_count.most_common(1)[0][0]}, ' \
           f'оно появилось в массиве {c_count.most_common(1)[0][1]} раз(а) '

print(func_1())
print(func_2())
print(func_3())

print(
    timeit(
        "func_1()",
        setup="from __main__ import func_1", number=10000))

print(
    timeit(
        "func_2()",
        setup="from __main__ import func_2", number=10000))

print(
    timeit(
        "func_3()",
        setup="from __main__ import func_3", number=10000))


'''

0.050361083
0.05549808299999999
0.067626625

Решениe через Counter на 35% дольше при исполнении func_1 и на 22% - func_2,
 но с точки зрения кода более лаконично и удобнее для восприятия!

'''