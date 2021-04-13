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
    m = max(array, key=array.count)
    elem = array.count(m)
    return f'Чаще всего встречается число {m}, ' \
           f'оно появилось в массиве {elem} раз(а)'

#print(func_1())
#print(func_2())
print(f'func_1 {timeit("func_1()", number=1000000, globals=globals())}')
print(f'func_2 {timeit("func_2()", number=1000000, globals=globals())}')
print(f'func_3 {timeit("func_3()", number=1000000, globals=globals())}')

#func_1 4.7764919
#func_2 5.8926339
#func_3 5.0106278

#Самый медленный вариант это func_2, так как используется добаврение в массив
# Самый быстрый и простой варинт получился с использованием цикла func_1 4.7764919