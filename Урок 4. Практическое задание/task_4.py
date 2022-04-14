"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой и по
возможности самой лаконичной.
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
    max_3 = max(array, key=array.count)
    count_3 = array.count(max_3)
    return f'Чаще всего встречается число {max_3}, оно появилось в массиве ' \
           f'{count_3} раз(а)'


print(func_1(), ' время работы: ', timeit('func_1()', globals=globals()))
print(func_2(), ' время работы: ', timeit('func_2()', globals=globals()))
print(func_3(), ' время работы: ', timeit('func_3()', globals=globals()))

"""
Отчет по работе функций с помощью профилировщика timeit показал следующее:
1)  1.4447789999999998
2)  2.0493388
3)  1.5353494999999997
исходя из данных можно сделать вывод что моя функция не стала самой быстрой 
"""
