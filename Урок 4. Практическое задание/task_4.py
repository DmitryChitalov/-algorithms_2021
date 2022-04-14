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
from cProfile import run

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
    total = max(array, key=array.count)
    total_n = array.count(total)
    return f'Чаще всего встречается число {total}, ' \
           f'оно появилось в массиве {total_n} раз(а)'


print(timeit("func_1()", number=3700000, globals=globals()))
run('func_1()')

print(timeit("func_2()", number=3700000, globals=globals()))
run('func_2()')

print(timeit("func_3()", number=3700000, globals=globals()))
run('func_3()')

print(func_1())
print(func_2())
print(func_3())

""" 
Выводы: В первых двух функциях переборы и сравнения, в третьем варианте используется встроенная функция, 
которая по идеи должна работать быстрее, но немного уступает первому примеру.
"""