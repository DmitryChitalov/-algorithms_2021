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


def own_func():
    elem = max(set(array), key=array.count)
    count = array.count(elem)
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {count} раз(а)'


# быстрее выполняется вариант 1, т.к. в func_2 производится генерация вспомогательного массива и поиск в нем наибольшего
# значения, что медленнее, чем (см. func_1) запоминание каждый раз новых значений num и count при выполнения условия
# if count > m
print(timeit('func_1()', number=100000, globals=globals()))  # результат 0.0144 с
print(timeit('func_2()', number=100000, globals=globals()))  # результат 0.194 с

# выполнение задачи стало быстрее на 0.001 с быстрее, чем вариант выполнения в func_1 =>
# можно считать, что ускорить выполнение задачи не получилось
print(timeit('own_func()', number=100000, globals=globals()))  # результат 0.143 с
