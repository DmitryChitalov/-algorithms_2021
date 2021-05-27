"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.

Без аналитики задание считается не принятым!
"""

# Третья версия func_3 является быстрой по сравнению с другими. Однако не сильно, по сравнению со второй.
# Это связано с тем, что список преобразуется во множество.

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
    array_set = set(array)
    most_common = None
    qty_most_common = 0

    for item in array_set:
        qty = array.count(item)
        if qty > qty_most_common:
            qty_most_common = qty
            most_common = item

    return f'Чаще всего встречается число {most_common}, ' \
           f'оно появилось в массиве {qty_most_common} раз(а)'


print(timeit("func_1", globals=globals()))
print(timeit("func_2", globals=globals()))
print(timeit("func_3", globals=globals()))