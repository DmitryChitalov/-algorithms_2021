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
    max_2 = max(array, key=array.count)
    return f'Чаще всего встречается число {max_2}, ' \
           f'оно появилось в массиве {array.count(max_2)} раз(а)'


# print(func_1())
# print(func_2())
# print(func_3())


print(timeit("func_1()", globals=globals()))
print(timeit("func_2()", globals=globals()))
print(timeit("func_3()", globals=globals()))
"""
2.4093405000000003
3.1432865000000003
2.0743805999999996

Первые две реализации похожи, но вторая медленнее из-за дпополнительного использования функции max, усложняет решение
Функция 3 написана без ипользования циклов, только с примененеием встроенной (уже оптимизированной) функции,
поэтому она самая быстрая!
"""