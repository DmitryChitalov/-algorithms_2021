"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.

Без аналитики задание считается не принятым
"""
import timeit

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
print('func_1', timeit.timeit('func_1', globals=globals()))
print(func_2())
print('func_2', timeit.timeit('func_2', globals=globals()))


def func_3():
    max_num = 0
    result = dict((i, array.count(i)) for i in array)
    for item in result.keys():
        if result[item] > max_num:
            max_num = result[item]
        return f'Чаще всего встречается число {item}, ' \
               f'оно появилось в массиве {max_num} раз(а)'


print(func_3())
print('func_3', timeit.timeit('func_3', globals=globals()))

# Два первых варианта медленные т.к. в них используются списк и массив, а в моём(третьем варианте) используется словарь
# скорость которого на чтение выше, чем у первых двух.


def func_4():
    max_dict = dict((array.count(i), i) for i in array)
    return f'Чаще всего встречается число {(max_dict[max(max_dict)])}, ' \
           f'оно появилось в массиве {max(max_dict)} раз(а)'


print(func_4())
print('func_4', timeit.timeit('func_4', globals=globals()))

# Исправленная функция три, в одну строку. Функция отрабатывает быстрее т.к. в ней нет цикла, который ищет максимальное
# число, эту задачу выполняет функция max.
