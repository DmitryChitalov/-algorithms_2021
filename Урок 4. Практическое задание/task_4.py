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


print(func_1())
print(func_2())


def func_3():
    max_count_num = max(array, key=lambda i: array.count(i))
    return f'Чаще всего встречается число {max_count_num}, оно появилось в массиве \
{array.count(max_count_num)} раз(а)'

print(func_3())


print(timeit('func_1()', globals=globals(), number=100000))         # 0.46906378400000004
print(timeit('func_2()', globals=globals(), number=100000))         # 0.6670984759999999
print(timeit('func_3()', globals=globals(), number=100000))         # 0.8214000460000002


# Первая функция работает на базе цикла, поэтому является самой быстрой.
# Вторая создает новый список и заполняет его, из-за этого выполняется чуть медленнее.
# Третья, написанная на основе функции max(), наиболее лаконичная, но занимает наибольшее время для выполнения.
