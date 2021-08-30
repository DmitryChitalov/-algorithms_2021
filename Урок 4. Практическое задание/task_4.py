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
    num = max(set(array), key=lambda i: array.count(i))
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {array.count(num)} раз(а)'


def func_4():
    num = sorted(set(array), key=lambda i: array.count(i))[-1]
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {array.count(num)} раз(а)'


def func_5():
    m, num = 0, 0
    for i in set(array):
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


print(func_1( ) == func_2( ) == func_3( ) == func_4( ) == func_5( ))
print(timeit('func_1()', globals=globals( )))
print(timeit('func_2()', globals=globals( )))
print(timeit('func_3()', globals=globals( )))
print(timeit('func_4()', globals=globals( )))
print(timeit('func_5()', globals=globals( )))

"""
Из 3-ёх написанных мной алгоритмов func_3, func_4 и func_5, func_5 оказался самым быстрым так как является доработанной
версией func_1. Создавая множество от интересующего нас массива при проходе, мы избегаем повторных вызовов метода 
count() для уже посчитанных значений.
func_3 оказался медленней,но лаконичней, чем func_2.
func_4 показывает примерно такие же результаты как и func_2, так как мы сортируем множество, но берем срез, 
а не используем max().
"""