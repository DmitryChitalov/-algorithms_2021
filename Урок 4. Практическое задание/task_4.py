"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.

Без аналитики задание считается не принятым
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
    m = 0
    num = 0
    i = len(array)-1
    while i > 0:
        count = array.count(i)
        if count > m:
            m = count
            num = i
        i -= 1
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_4():
    f = list(filter(lambda x: (x, array.count(x)), array))
    return f'Чаще всего встречается число {f[0]}, ' \
        f'оно появилось в массиве {f[1]} раз(а)'


def func_5():
    m = max((array.count(i) for i in array))
    for i in array:
        if array.count(i) == m:
            return f'Чаще всего встречается число {i}, ' \
                f'оно появилось в массиве {m} раз(а)'


def func_6():
    for i in array:
        if array.count(i) == max((array.count(i) for i in array)):
            return f'Чаще всего встречается число {i}, ' \
                   f'оно появилось в массиве {array.count(i)} раз(а)'


# Вариант 3 разница небольшая и иногда обратная но в большинстве случаев t1< t3,но иногда самая быстрая t1
# т.к используется цикл и значения сохраняются в переменные.


print(func_1())
print(func_2())
print(func_3())
print(func_4())
print(func_5())
print(func_6())


print(timeit.timeit("func_1()", 'from __main__ import func_1', number=100000), ">>>1")
print(timeit.timeit("func_2()", 'from __main__ import func_2', number=100000), ">>>2")
print(timeit.timeit("func_3()", 'from __main__ import func_3', number=100000), ">>>3")
print(timeit.timeit("func_4()", 'from __main__ import func_4', number=100000), ">>>4")
print(timeit.timeit("func_5()", 'from __main__ import func_5', number=100000), ">>>5")
print(timeit.timeit("func_6()", 'from __main__ import func_6', number=100000), ">>>6")
