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
    max_count = max(array, key=array.count)
    return f'Чаще всего встречается число {max_count}, ' \
           f'оно появилось в массиве {array.count(max_count)} раз(а)'


def func_4():
    new_dict = {array.count(el): el for el in set(array)}
    maximum = max([value for value in new_dict.keys()])
    return f'Чаще всего встречается число {new_dict.get(maximum)}, ' \
           f'оно появилось в массиве {maximum} раз(а)'


print(func_1())
print(func_2())
print(func_3())
print(func_4())


functions = ['func_1', 'func_2', 'func_3', 'func_4']
for func in functions:
    print(f'{func}:', timeit(f'{func}()', globals=globals(), number=100000))

# Наиболее эффективным и лаконичным алгоритмом оказался func_3, хотя все они имеют одинаковую временную сложность O(N^2)
# Вариант со словарем оказался не самым плохим, что несколько удивило даже
# При больших списках на поиск наибольшего количества вхождений имеет смысл использовать множества,
# как реализовано в алгоритме со словарем.
