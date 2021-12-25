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
from random import randint

array = [1, 3, 1, 3, 4, 5, 1]

#array = [randint(1, 10) for i in range(100)]

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
    b = array[:]
    b.sort(key=lambda val: array.count(val), reverse=True)
    return f'Чаще всего встречается число {b[0]}, ' \
           f'оно появилось в массиве {b.count(b[0])} раз(а)'


def func_4():
    result = max([[array.count(i), i] for i in set(array)])
    return f'Чаще всего встречается число {result[1]}, ' \
           f'оно появилось в массиве {result[0]} раз(а)'


def func_5():
    result = max(array, key=array.count)
    return f'Чаще всего встречается число {result}, ' \
           f'оно появилось в массиве {array.count(result)} раз(а)'


print(func_1())
print(func_2())
print(func_3())
print(func_4())
print(func_5())


print(timeit('func_1()', 'from __main__ import func_1, array', number=10000))
print(timeit('func_2()', 'from __main__ import func_2, array', number=10000))
print(timeit('func_3()', 'from __main__ import func_3, array', number=10000))
print(timeit('func_4()', 'from __main__ import func_4, array', number=10000))
print(timeit('func_5()', 'from __main__ import func_5, array', number=10000))

# В исходном списке выигрывают по времени func_1 и func_5, причем func_1 немного быстрее, таким образом ускорить задачу
# не получись, но если создать случайный список из 100 элементов, по времени значительно выигрывает вариант func_4,
# т.к. длинный список преобразуется в множество, содержащее только уникальные элементы



