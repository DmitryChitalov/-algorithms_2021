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
    result = max(set(array), key=array.count)
    return f'Чаще всего встречается число {result} ' \
           f'оно встречается {array.count(result)} раз(а)'


print(func_1())
print(func_2())
print(func_3())

print(timeit('func_1()', globals=globals()))
print(timeit('func_2()', globals=globals()))
print(timeit('func_3()', globals=globals()))

"""
Вывод:
Функция func_3() отрабатывает быстрее, поскольку итерирует не по каждлму элементу,
а только по уникальным элементам списка.
Функция func_2() самая медленная, т.к. в ней используется второй список,
Работа с ним так добавляет времени выполнения функции. Предполагаю,
что временная сложность операции count O(n). Эта операция находится в цикле,
что повышает временную сложность функции до O(n^2)
"""
