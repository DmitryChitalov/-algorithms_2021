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

# Вторая функция выполняется медленнее, чем первая, так как она пробегает по всему массиву
# и потом на основании его данных формирует новый массив.
# Затем функция уже анализирует новый массив, пытаясь найти максимальное значение,
# из-за чего получается, что она пробегает по массивам дважды.
# В отличие от неё первая функция пробегает по массиву единожды,
# из-за чего и получает преимущество во времени.


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


# Я попыталась, создать что-то своё, но лучше первой функции сделать не получилось.
# Смогла уделать только вторую, и то не намного; надеялась, что обращение к словарю поможет выйграть немного времени,
# но не особо получилось. Опять же прошлась по массивам два раза, да и методы словарей наверняка тоже заняли время .

def func_3():
    my_dict = {array.count(i): i for i in array}
    max_value = max(my_dict.keys())
    return f'Чаще всего встречается число {my_dict[max_value]}, оно появилось в массиве {max_value} раз(а)'


print(f'Время выполнения функции func_1: {timeit("func_1()", globals=globals(), number=1000)}')
print(func_1())
print(f'Время выполнения функции func_2: {timeit("func_2()", globals=globals(), number=1000)}')
print(func_2())
print(f'Время выполнения функции func_3: {timeit("func_3()", globals=globals(), number=1000)}')
print(func_3())