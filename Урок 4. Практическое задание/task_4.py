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
# array = [1, 3, 1, 3, 4, 5, 1]
array = [1, 3, 1, 3, 4, 5, 1, 4, 3, 2, 3, 2, 5, 6, 7, 3, 4, 12, 3, 45, 24, 2, 45, 23, 53, 23, 5, 23]


def func_1():
    m = 0
    num = 0
    for i in set(array):
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
    res = max([(i, array.count(i)) for i in set(array)], key=lambda j: j[1])
    return f'Чаще всего встречается число {res[0]}, ' \
           f'оно появилось в массиве {res[1]} раз(а)'


print(func_1())
print(func_2())
print(func_3())
print(timeit('func_1()', globals=globals()))  # 1.4128933  |  11.8639366
print(timeit('func_2()', globals=globals()))  # 1.9684872  |  13.0384062
print(timeit('func_3()', globals=globals()))  # 2.1512649  |  7.648020200000001
"""
При небольшом колличестве элементов первые две функции отрабатывают быстрее,
однако стоит увеличить список, время работы третьей функции стало значительно меньше первых двух.
Это благодоря применению функции set к списку однако при всех уникальных значениях в списке прироста
производительности третьей функции при увеличении размера списка мы не увидим.
Если применить множество во время цикла в первой функции это также поможет уменьшить её время работы:
первый замер 1.250228
второй замер 5.8892701
"""
