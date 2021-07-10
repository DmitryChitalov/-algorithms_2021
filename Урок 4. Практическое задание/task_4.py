"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой и по возможности самой лаконичной.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.

Без аналитики задание считается не принятым!
"""

"""
Первый алгоритм - самый быстрый - вероятно потому что список очень короткий и его линейная
сложность нормально и быстро проходит

Второй использует счетчики и спец методы наверное задержка в этом примере где-то здесь

Третия (мой) - решил сумничать и проявить оригинальность, результат примерно такой же как и во твором 
случае, конкретная реализация поиска моды не мне не понятна, но наверное похожа на второй вариант 
"""


import statistics
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
    mode = statistics.mode(array)
    return f"Чаще всего встречается число {mode}, " \
           f"оно появилось в массиве {array.count(mode)} раз(а)"


print(func_1())
print(func_2())
print(func_3())

print(
    timeit(
        'func_1()',
        setup='from __main__ import func_1, array',
        number=1000000))

print(
    timeit(
        'func_3()',
        setup='from __main__ import func_3, array',
        number=1000000))

print(
    timeit(
        'func_3()',
        setup='from __main__ import func_3, array',
        number=1000000))
