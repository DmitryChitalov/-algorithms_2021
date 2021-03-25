"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.

Без аналитики задание считается не принятым
"""
from collections import Counter
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
    result = Counter(array).most_common()[0]
    return f'Чаще всего встречается число {result[0]}, ' \
           f'оно появилось в массиве {result[1]} раз(а)'


def func_4():
    result = max(array, key=array.count)
    return f'Чаще всего встречается число {result}, ' \
           f'оно появилось в массиве {array.count(result)} раз(а)'


print(func_1())
print(func_2())
print(func_3())
print(func_4())
print(timeit('func_1', globals=globals()))
print(timeit('func_2', globals=globals()))
print(timeit('func_3', globals=globals()))
print(timeit('func_4', globals=globals()))


"""
Я попробовал два варианта, но, к сожалению, превзойти результат второй функции не смог.
Вторая функция самая быстрая.

P.S возможно с моей тачкой что-то не так т.к 4-я функция иногда бывает эффективнее остальных, а иногда третья или первая. Кажется, что на моей машине расчеты происходят некорректно.
"""