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

array = [1, 3, 1, 3, 4, 5, 1]


def func_1():
    """
    Сложность - O(n^2)
    """
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
    """
    Сложность - O(n^2)
    """
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def memoize(f):
    cache = {}

    def decorate(*args):

        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]
    return decorate


@memoize
def func_1_mem():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


print(func_1())
print(func_2())
print(timeit("func_1()", globals=globals(), number=10000))
print(timeit("func_2()", globals=globals(), number=10000))
print(timeit("func_1_mem()", globals=globals(), number=10000))

"""
Сделав профилировку, видим, что первая функция срабатывает быстрее.
Проанализиров задачу, видим, что мы много кратно выполняем одну и ту же процедуру: поиск количества того, сколько раз 
элемент входит в массив. Думаю, тут лучше использовать мемоизацию.

Результаты:
0.042884900000000004
0.06206789999999998
0.004093199999999991

Получилось оптимизировать функцию
"""