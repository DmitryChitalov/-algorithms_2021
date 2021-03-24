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
from collections import Counter


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
    res = Counter(array).most_common(1)
    return f'Чаще всего встречается число {res[0][0]}, ' \
           f'оно появилось в массиве {res[0][1]} раз(а)'


def func_4():
    res = max([[array.count(i), i] for i in set(array)])
    return f'Чаще всего встречается число {res[1]}, ' \
           f'оно появилось в массиве {res[0]} раз(а)'


print(func_1())
print(func_2())
print(func_3())
print(func_4())

print('Выполнение первой функции составило', timeit("func_1()", globals=globals()))
print('Выполнение второй функции составило', timeit("func_2()", globals=globals()))
print('Выполнение третьей функции составило', timeit("func_3()", globals=globals()))
print('Выполнение четвертой функции составило', timeit("func_4()", globals=globals()))

# т.к. сдаю это д/з с задержкой, использую тут материалы 5 урока =)
# замеры показывают, что с коллекцией существенно медленнее, чем без нее! 5.2 сек против 2.3 и 1.6
# я попробовала еще один вариант, func_4, использующий LC и встроеннй метод,
# но и он оказался медленне первого, 2 сек против 1.6
# ускорить не удалось
