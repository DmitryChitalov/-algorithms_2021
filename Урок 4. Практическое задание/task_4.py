"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой и по возможности самой лаконичной.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.

Без аналитики задание считается не принятым!
"""
import timeit

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
    a_set = set(array)
    elem = 0
    max_qty = 0
    for item in a_set:
        qty = array.count(item)
        if qty >  max_qty:
            max_qty = qty
            elem = item
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_qty} раз(а)'


print(func_1())
print(func_2())
print(func_3())

print(
    timeit.timeit(
         "func_1()",
         globals=globals(),
         number=10000))

print(
    timeit.timeit(
         "func_2()",
         globals=globals(),
         number=10000))

print(
    timeit.timeit(
         "func_3()",
         globals=globals(),
         number=10000))

""" У меня получилось ускорить, так как в моем случае проверяются только уникальные элементы массива
при этом, чем болше будет повторяющихся элементов в массиве, тем больше будет разница
Чаще всего встречается число 1, оно появилось в массиве 3 раз(а)
Чаще всего встречается число 1, оно появилось в массиве 3 раз(а)
Чаще всего встречается число 1, оно появилось в массиве 3 раз(а)
0.020122300000000003
0.024823400000000002
0.014098"""