"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой и по возможности самой лаконичной.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.

Без аналитики задание считается не принятым!
"""

from memory_profiler import profile
import random


array = []
for j in range(10000):
    array.append(random.randint(1, 50))


@profile()
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


@profile()
def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


@profile()
def my_func():
    my_num = max(array, key=array.count)
    return f'Чаще всего встречается число {my_num}, ' \
           f'оно появилось в массиве {array.count(my_num)} раз(а)'


print(func_1())
print(func_2())
print(my_func())


"""
Вывод: При работе с большими данными функция map позволяет уменьшить расход памяти.
"""
