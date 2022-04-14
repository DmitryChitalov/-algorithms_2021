"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""
from timeit import timeit

array = [9, 1, 3, 1, 3, 4, 5, 1, 9, 9, 9, 9]


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
    max_elem = max(set(array), key=array.count)
    count = array.count(max_elem)
    return f'Чаще всего встречается число {max_elem}, ' \
           f'оно появилось в массиве {count} раз(а)'


print(func_1())
print(func_2())
print(func_3())

print(f'func_1() - {timeit("func_1()", globals=globals())}')
print(f'func_2() - {timeit("func_2()", globals=globals())}')
print(f'func_3() - {timeit("func_3()", globals=globals())}')

"""
Вывод:
Функция func_3() отрабатывает быстрее, если в аргументы max() передать не просто маасив чисел, а множество.
Тогда итерация пойдет только по уникальным элементам списка. Без этого скорость func_1 и 3 практически
одинаковая.
Функция func_2() самая медленная, т.к. в ней используется второй список,
"""
