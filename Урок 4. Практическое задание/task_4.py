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


def func_41():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_42():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def func_43():
    elem_3 = max(set(array), key=array.count)
    max_3 = array.count(elem_3)
    return f'Чаще всего встречается число {elem_3}, ' \
           f'оно появилось в массиве {max_3} раз(а)'


print(func_41())
print(func_42())
print(func_43())

print(f'{timeit("func_41()", globals=globals(), number=100000)}')
print(f'{timeit("func_42()", globals=globals(), number=100000)}')
print(f'{timeit("func_43()", globals=globals(), number=100000)}')


"""
Аналитика:
первая функция проходится по всем элементам и сохраняет количество вхождений самого частого.
функция 2 хранит аналитику по всем значениям и с помощью max, вывоид самый частый, что медлнее
функция 3 самая быстрая, т.к. использует только встроенные функции без циклов
"""
