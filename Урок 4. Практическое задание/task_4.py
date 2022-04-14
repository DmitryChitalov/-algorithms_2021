"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой и по возможности самой лаконичной.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.

Без аналитики задание считается не принятым!
"""

"""
func_1  время 0.0009258000000000009
func_2  время 0.001255000000000001
func_3  время 0.0006925000000000021   самая быстрое время выполнение + краткость кода
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
    return max(array, key=array.count)


print(timeit.timeit('func_1()', globals=globals(), number=1000))
print(timeit.timeit('func_2()', globals=globals(), number=1000))
print(timeit.timeit('func_3()', globals=globals(), number=1000))

# print(func_1())
# print(func_2())
# print(func_3())
