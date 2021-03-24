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
    result = max([[array.count(i), i] for i in set(array)])
    return f'Чаще всего встречается число {result[1]}, ' \
           f'оно появилось в массиве {result[0]} раз(а)'



print(f'func_1: {func_1()} , {timeit("func_1", globals=globals())} сек.')
print(f'func_2: {func_2()} , {timeit("func_2", globals=globals())} сек.')
print(f'func_3: {func_3()} , {timeit("func_3", globals=globals())} сек.')

# func_1: 0.019881483000000002 сек.
# func_2: 0.021701869 сек.
# func_3: 0.021573418999999996 сек.
# не получилось написать более быстрый алгоритм :(