"""
Задание 4.
Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.
Сделайте профилировку каждого алгоритма через timeit
Попытайтесь написать третью версию, которая будет самой быстрой и по возможности самой лаконичной.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
Без аналитики задание считается не принятым!
"""
from timeit import Timer
from random import random


array = [int(random()*5) for i in range(10)]
print(array)


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

    array_set = set(array) # список в множество в нем все элементы уникальны
    most_common = None # самое частое значение
    qnty_most_common = 0 # его количество

    # в цикле перебираются элементы (item) множества
    for item in array_set:
        # переменной qty присваивается количество случаев item в списке array
        now_num = array.count(item)
        if now_num > qnty_most_common:
            qnty_most_common = now_num
            most_common = item
    return f'Чаще всего встречается число {most_common}, ' \
           f'оно появилось в массиве {qnty_most_common} раз(а)'

print(func_1())
print(func_2())
print(func_3())

t1 = Timer("func_1()", globals=globals())
print("func_1 ", t1.timeit(number=1000), "seconds")

t2 = Timer("func_2()", globals=globals())
print("func_2 ", t2.timeit(number=1000), "seconds")

t3 = Timer("func_3()", globals=globals())
print("func_3 ", t3.timeit(number=1000), "seconds")

"""
func_1  0.0034829999785870314 seconds
func_2  0.004688199958764017 seconds
func_3  0.0020847999840043485 seconds
"""

"""
Список сделал рандомно генерируемым а то ваш можно было просто .set() посчитать 
задаччу получилось ускорить, код занимает больше строк но более понятный
если в списке есть два значения которые встречаются одинаковое количество раз
то будет показано только одно из них
"""