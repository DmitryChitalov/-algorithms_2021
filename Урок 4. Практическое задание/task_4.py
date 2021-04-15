"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.

Без аналитики задание считается не принятым
"""

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


print(func_1())
print(func_2())

from timeit import timeit


array = [1, 3, 1, 3, 4, 5, 1]

@@ -39,5 +41,21 @@ def func_2():
           f'оно появилось в массиве {max_2} раз(а)'


def func_3():
    elem = max(array, key=array.count)
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {array.count(elem)} раз(а)'

print(func_1())
print(func_2())
print(func_3())

print(f'{timeit("func_1()",globals=globals(), number = 1000)} func_1' )
print(f'{timeit("func_2()",globals=globals(), number = 1000)} func_2' )
print(f'{timeit("func_3()",globals=globals(), number = 1000)} func_3' )

#0.003340799999999998 func_1
#0.007536400000000006 func_2
#0.0032724999999999976 func_3
# func_2 самая медленная из-за создания нового массива и применения append, a func_1 и func_3 примерно одинаковы
