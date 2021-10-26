"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой и по возможности самой лаконичной.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.

Без аналитики задание считается не принятым!
"""
import timeit

array = [1, 3, 1, 3, 3, 3, 4, 5, 1]


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
    set_array = set(array)
    num = 0
    max_3 = 0
    for el in set_array:
        cnt = array.count(el)
        if max_3 < cnt:
            max_3 = cnt
            num = el
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {max_3} раз(а)'


print(func_1())
print(func_2())
print(func_3())

print(timeit.repeat('func_1()', repeat=3, number=1000000, globals=globals()))
print(timeit.repeat('func_2()', repeat=3, number=1000000,  globals=globals()))
print(timeit.repeat('func_3()', repeat=3, number=1000000,  globals=globals()))

"""
Исходя из замеров, получилось сделать алгоритм быстрее. Было использовано множество, 
чтобы убрать из перебора список с повторяющимися позициями. Это ускорило процесс.
"""

