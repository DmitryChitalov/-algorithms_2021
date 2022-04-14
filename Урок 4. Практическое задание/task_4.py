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
    number = max(set(array), key=array.count)
    return f'Чаще всего встречается число {number}, ' \
           f'оно появилось в массиве {array.count(number)} раз(а)'


print(func_1())
print(func_2())
print(func_3())

print('Функция func_1')
print(
    timeit(
        "func_1()",
        setup='from __main__ import func_1, array',
        number=10000))

print('Функция func_2')
print(
    timeit(
        "func_2()",
        setup='from __main__ import func_2, array',
        number=10000))

print('Функция func_3')
print(
    timeit(
        "func_3()",
        setup='from __main__ import func_3, array',
        number=10000))

"""
Функция func_1
0.013083299999999999
Функция func_2
0.0174758
Функция func_3
0.012890899999999997

Получен немного (почти незначительно и близко к погрешности) более быстрый вариант, за счет параметра key функции max. 
По сути ищет элемент, который имеет не максимальное значение, а максимальное число повторов. Чтобы каждое число не 
проверять несколько раз в качестве данных берем множество из этого списка.
"""
