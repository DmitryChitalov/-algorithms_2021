"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.

Без аналитики задание считается не принятым
"""
import operator
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

print(
    timeit(
        'func_1()',
        globals=globals(),
        number=1000000))
print(
    timeit(
        'func_2()',
        globals=globals(),
        number=1000000))


"""
timeit показал, что func_2 медленнее первой функции.
В func_2 происходит создание второго массива и заполнение его значениями. 

2.1871473999999997
3.2600144
"""


def func_3():
    temp_dict = {}
    for el in array:
        if el in temp_dict:
            temp_dict[el] += 1
        else:
            temp_dict[el] = 1
    return f'Чаще всего встречается число {max(temp_dict, key=temp_dict.get)}, ' \
           f'оно появилось в массиве {max(temp_dict.values())} раз(а)'


def func_4():
    cache = {}
    m = 0
    num = 0
    for i in array:
        if i in cache:
            count = cache[i]
        else:
            count = array.count(i)
            cache[i] = count
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


print(func_3())
print(func_4())

print(
    timeit(
        'func_3()',
        globals=globals(),
        number=1000000))

print(
    timeit(
        'func_4()',
        globals=globals(),
        number=1000000))
"""
Написал функцию func_3 (использовал словари)
Написал функцию func_4 (использовал мемоизацию)

Они не быстрее func_1 и func_2 на данном наборе данных, однако на 
array = [1, 3, 1, 3, 4, 5, 1, 1, 3, 1, 3, 4, 5, 1, 1, 3, 1, 3, 4, 5, 1, 1, 3, 1, 3, 4, 5, 1, 1, 3, 5, 6, 7, 8, 9, 4, 3,
1, 3, 5, 6, 3,1, 3, 4, 5, 1]

результаты сильно меняются:
func_1  37.0729937
func_2  42.1867849
func_3  9.14028300000001
func_4  13.089951

Думаю что на произвольных данных func_3 и func_4 будут более эффективны первыых двух
"""