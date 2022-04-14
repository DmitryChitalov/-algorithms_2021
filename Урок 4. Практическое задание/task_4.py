"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой и по возможности самой лаконичной.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.

Без аналитики задание считается не принятым!
"""
#Опираясь на время выполнения каждой из функции, можно сделать вывод о том, что функция func_1() - самая эффективная,
#хоть и по памяти, хуже чем func_3_1(), func_3_2() и func_4(), но она лучше оптимизирована, быстра и лаконична.


from timeit import timeit
from collections import Counter


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


def func_3_1():
    return f'Чаще всего встречается число {Counter(array).most_common(1).pop()[0]}, ' \
           f'оно появилось в массиве {Counter(array).most_common(1).pop()[1]} раз(а)'


def func_3_2():
    b = Counter(array)
    return f'Чаще всего встречается число {b.most_common(1)[0][0]}, ' \
           f'оно появилось в массиве {b.most_common(1)[0][1]} раз(а)'


def func_4():
    new_array = []
    for el in set(array):
        new_array.append([el, array.count(el)])
    value, value_site  = max(new_array, key=lambda i: i[1])
    return f'Чаще всего встречается число {value}, ' \
           f'оно появилось в массиве {value_site} раз(а)'


print(
    timeit(
        "func_1()",
        globals=globals()
        ), func_1())
print(
    timeit(
        "func_2()",
        globals=globals()
        ), func_2())
print(
    timeit(
        "func_3_1()",
        globals=globals()
        ), func_3_1())
print(
    timeit(
        "func_3_2()",
        globals=globals()
        ), func_3_2())
print(
    timeit(
        "func_4()",
        globals=globals()
        ), func_4())