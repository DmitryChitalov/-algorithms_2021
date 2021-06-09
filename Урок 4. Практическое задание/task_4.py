"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
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
    array.sort(key=lambda x: array.count(x), reverse=True)
    return f'Чаще всего встречается число {array[0]}, ' \
           f'оно появилось в массиве {array.count(array[0])} раз(а)'


print(func_1())
print(func_2())
print(func_3())

print("\nФункция func_1():")
print(timeit("func_1()", globals=globals()))

print("\nФункция func_2():")
print(timeit("func_2()", globals=globals()))

print("\nФункция func_3():")
print(timeit("func_3()", globals=globals()))

"""
Время выполнения фукций:

Функция func_1():
2.2649852569999998

Функция func_2():
3.0836836269999996

Функция func_3():
1.9502563129999997

Третья версия оказалась самой быстрой благодаря использованию встроенного метода .sort и lambda-функции
в качестве ключа сортировки.

В первых двух вариантах мы последовательно проходим все элементы массива, поэтому алгоритмы работают дольше.
"""