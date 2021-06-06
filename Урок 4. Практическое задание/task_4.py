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
from cProfile import run

array = [1, 3, 1, 3, 3, 3, 3, 3, 4, 5, 1, 3, 1, 2, 3, 1, 3, 1, 3, 3, 3, 3, 3, 4, 5, 1, 3, 1, 2, 3, ]


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
    elements = {}
    for el in array:
        elements[el] = elements.get(el, 0) + 1
    return f'Чаще всего встречается число {max(elements, key=elements.get)}, ' \
           f'оно появилось в массиве {max(elements.values())} раз(а)'


def func_4():
    max_elem = max(set(array), key=array.count)
    count = array.count(max_elem)
    return f'Чаще всего встречается число {max_elem}, ' \
           f'оно появилось в массиве {count} раз(а)'


print(timeit("func_1()", globals=globals(), number=1000000))
print(timeit("func_2()", globals=globals(), number=1000000))
print(timeit("func_3()", globals=globals(), number=1000000))
print(timeit("func_4()", globals=globals(), number=1000000))

'''
10.0346546 - func_1
11.533943299999999 - func_2
4.399538500000002 - func_3
3.019878000000002 - func_4

func_3 алгоритм с использованием словаря весьма быстрый, так как метод .get словаря имеет O(1) сложность.
func_4 алгоритм с использованием метода max справляется быстрее если использовать не весь список а множество.
func_1 и func_2 отрабатывают намного медленнее из-за наличия цикла for.
'''