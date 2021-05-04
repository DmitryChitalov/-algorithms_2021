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
# from random import randint

array = [1, 3, 1, 3, 4, 5, 1]
# array = [randint(1, 100) for i in range(0, 10000)]


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
    result = max(array, key=array.count)
    return f'Чаще всего встречается число {result}, ' \
           f'оно появилось в массиве {array.count(result)} раз(а)'


print(timeit('func_1', globals=globals(), number=10000000))
print(func_1())
print(timeit('func_2', globals=globals(), number=10000000))
print(func_2())
print(timeit('func_3', globals=globals(), number=10000000))
print(func_3())

'''
----------------------------------------------------------------
0.2162528
Чаще всего встречается число 1, оно появилось в массиве 3 раз(а)
0.19873880000000002
Чаще всего встречается число 1, оно появилось в массиве 3 раз(а)
0.17529619999999996
Чаще всего встречается число 1, оно появилось в массиве 3 раз(а)
----------------------------------------------------------------
    Вариант 3 отрабатывавет быстрее остальных большее количество раз, но не всегда.
Встроенные функции оптимизированны и решают задачу за меньшее количество действий.
    Вариант 2 работает медленее всех, т.к. в нем создается новый массив, заполняется
и впоследствии выбирается наибольший элемент.
    Увеличение длины и разнообразности массива не изменило результатов.
'''