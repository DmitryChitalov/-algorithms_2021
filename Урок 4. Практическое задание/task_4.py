"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.

Без аналитики задание считается не принятым!
"""

from timeit import Timer
from random import randint as randint

# array = [1, 3, 1, 3, 4, 5, 1] # Не репрезентативно, скучно!
array = [randint(1, 20) for i in range(1000)]


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
    arr_value = []
    arr_count = []
    for el in array:
        if el not in arr_value:
            count2 = array.count(el)
            arr_value.append(el)
            arr_count.append(count2)

    max_2 = max(arr_count)
    elem = arr_value[arr_count.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


print(func_1())
print(func_2())
print(func_3())

t1 = Timer("func_1()", "from __main__ import func_1")
print('t1', t1.timeit(number=1000))

t2 = Timer("func_2()", "from __main__ import func_2")
print('t2', t2.timeit(number=1000))

t3 = Timer("func_3()", "from __main__ import func_3")
print('t3', t3.timeit(number=1000))

# В этом задании работа опять производится на каждой итерации над одним и тем же массивом (понятно,
# что это делается для определения наиболее эффективного алгоритма). В порядке
# эксперимента я в каждой функции генерил свой массив с произвольными данными, результаты работы функций
# не сильно отличались от варианта с одинаковым массивом для всех функций.
# Более того увеличил длинну массива до 1000 элементов
# Третья функция - это немного модифицированная вторая. Но результат получился очень хороший:
#
# Чаще всего встречается число 11, оно появилось в массиве 63 раз(а)
# Чаще всего встречается число 11, оно появилось в массиве 63 раз(а)
# Чаще всего встречается число 11, оно появилось в массиве 63 раз(а)
# t1 13.601908887
# t2 13.531736463000001
# t3 0.4026966269999974
