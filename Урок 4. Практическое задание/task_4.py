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
from collections import Counter

array = [1, 3, 1, 3, 4, 5, 1, 1, 3, 1, 3, 4, 5, 1, 1, 3, 1, 3, 4, 5, 1, 1, 3, 1, 3, 4, 5, 1, 1, 3, 1, 3, 4, 5, 1, 1, 3, 1, 3, 4, 5, 1, ]


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
    most_common_tuple = Counter(array).most_common(1)[0]
    most_common_number = most_common_tuple[0]
    most_common_count = most_common_tuple[1]
    return f'Чаще всего встречается число {most_common_number}, ' \
           f'оно появилось в массиве {most_common_count} раз(а)'


print(func_1())
print(func_2())
print(func_3())

for i in range(3):
    func_name = f'func_{i + 1}'
    print(func_name)
    print(
        timeit(
            f"{func_name}()",
            setup=f'from __main__ import {func_name}, array',
            number=10000
        )
    )

"""
второй вариант работает медленнее первого, потому что идет формирование нового массива
третий вариант самый быстрый, потому что используется встроенная библиотека Counter из collections 
"""
