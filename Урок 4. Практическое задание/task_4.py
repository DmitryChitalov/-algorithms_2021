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


# print(func_1())
# print(func_2())


def func_3():
    """ list comprehension """
    new_array = [array.count(i) for i in array]
    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def func_4():
    """ Встроенная функция max() и аргумент key """
    max_2 = max(array, key=array.count)
    elem = array.count(max_2)
    return f'Чаще всего встречается число {max_2}, ' \
           f'оно появилось в массиве {elem} раз(а)'


def func_5():
    m = 0
    num = 0
    for i in set(array):
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


if __name__ == '__main__':
    print(f'func_1 {timeit("func_1()", number=1000000, globals=globals())}')
    print(f'func_2 {timeit("func_2()", number=1000000, globals=globals())}')
    print(f'func_3 {timeit("func_3()", number=1000000, globals=globals())}')
    print(f'func_4 {timeit("func_4()", number=1000000, globals=globals())}')
    print(f'func_5 {timeit("func_5()", number=1000000, globals=globals())}')

# Замеры
"""
func_1 1.034237611
func_2 1.4021699449999998
func_3 1.2803982509999998
func_4 1.099538726
func_5 0.8992509269999998
"""

"""
- "func_3" почти идентична "func_2" чтобы увеличить эффективность заменил цикл на списковое включение.
- "func_4" быстрее за счет встроенной функции max() и аргумента "key".
- func_5 ещё быстрее за счет set() для исходного списка, там самым сокращая кол-во итераций в цикле 
по исходному списку.
"""
