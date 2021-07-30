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

    m = 0
    num = 0
    array_str = ', ' + str(array)[1:-1] + ', '
    copy_array_str = array_str
    num_comma = array_str.count(', ')

    for i in range(num_comma - 1):

        first_index = copy_array_str.find(', ')
        second_index = copy_array_str.find(', ', first_index + 1)
        need_find = copy_array_str[first_index:second_index]
        copy_array_str = copy_array_str[second_index:]
        counter = array_str.count(need_find)

        if counter > m:
            m = counter
            num = need_find[2:]

    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_4():
    num = max(array, key=array.count)
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {array.count(num)} раз(а)'


def func_5(array_in, m=0, num=0):

    for i in array_in:
        count = array_in.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


print(func_1())
print(func_2())
print(func_3())
print(func_4())
number = 100000

print('func_1')  # 0.18603302500000002
print(
    timeit(
        "func_1()",
        setup='from __main__ import func_1',
        number=number))
print('func_2')  # 0.27401201
print(
    timeit(
        "func_2()",
        setup='from __main__ import func_2',
        number=number))
print('func_3')  # 0.962197978
print(
    timeit(
        "func_3()",
        setup='from __main__ import func_3',
        number=number))
print('func_4')  # 0.20417611199999985
print(
    timeit(
        "func_4()",
        setup='from __main__ import func_4',
        number=number))
print('func_5')  # 0.17129198099999998
print(
    timeit(
        "func_5(array)",
        setup='from __main__ import func_5, array',
        number=number))

'''Согласно временным замерам самым быстрым является пятый способ, являющийся упрощением первого, второго по скорости
выполнения в списке замеров. Использования ключа при использовании функции max даёт почти такие же быстрые результаты, 
как 1 и 5-й способы, но, видимо, в силу сложности проводимых операйций уступает в работе for in и if со списком чисел.
Добавление для обработки данных ещё одного списка замедляет работу 2-го способа. А работа с поиском внтури строк из-за 
зависимости от длины строки при неоднократном использовнаии в коде и вовсе в разы проигрывает поиску с помощью 
встроенного count внутри for in. Полноценного отличного от изначально предложенных способа, который бы ускорял работу,
мне придумать не удалось.'''
