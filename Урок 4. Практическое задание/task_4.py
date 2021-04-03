"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.

Без аналитики задание считается не принятым
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
    numb = max(array, key=array.count)
    return f"Чаще всего встречается число {numb}, оно появилось в массиве {array.count(numb)} раз(а)"


def func_4():
    arr_set = set(array)
    m = 0
    num = 0
    for i in arr_set:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


print(func_1())
print(func_2())
print(func_3())
print(func_4())

func_list = ['func_1', 'func_2', 'func_3', 'func_4']
for func in func_list:
    print(f'Функция {func}:', timeit(func + '()', number=1000000, globals=globals()))

'''
Функция func_1: 2.544683
Функция func_2: 3.1567616
Функция func_3: 2.2534705000000006
Функция func_4: 1.5756817000000005

Самый долгий результат дает второй вариант, в рамках функции func_2 формируется новый массив чисел
из количества включений числа изначального массива.
Третий вариант быстрый, в нем сразу определяется максимум из количества включений числа в массив.
Функция func_1 хороший алгоритм но, к елементу который встречается несколько раз будет
каждый раз применятся count. В функции func_4 убрана данная проблема, добавлением set.
'''