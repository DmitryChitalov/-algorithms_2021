"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.

Без аналитики задание считается не принятым
"""

from timeit import timeit, repeat, default_timer

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
    elem = sorted([item for item in array], key=lambda x: array.count(x), reverse=True)[0]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {array.count(elem)} раз(а)'


def func_4():
    elem = max(array, key=array.count)
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {array.count(elem)} раз(а)'


print(func_1())
print(func_2())
print(func_3())
print(func_4())


t1 = min(repeat('func_1()', 'from __main__ import func_1', default_timer, 5, 10000))
t2 = min(repeat('func_2()', 'from __main__ import func_2', default_timer, 5, 10000))
t3 = min(repeat('func_3()', 'from __main__ import func_3', default_timer, 5, 10000))
t4 = min(repeat('func_4()', 'from __main__ import func_4', default_timer, 5, 10000))

print(f"Из func_1 и func_2 быстрее выполняется функция --- > {'func_1' if t1 < t2 else 'func_2'}")

print(f"Время выполнения функции func_1 равно:\t{t1}")
print(f"Время выполнения функции func_2 равно:\t{t2}")
print(f"Время выполнения функции func_3 равно:\t{t3}")
print(f"Время выполнения функции func_4 равно:\t{t4}")

'''
func_2 медленне func_1 потому что в ней создается и заполняется новый массив и после того как он заполнится 
осуществляется пробег по новому массиву для того чтобы выбрать максимальное значение.
func_3 (написал сам) получилась самой дедленной потому что в ней есть сортировка, так как это O(n log n) то она 
получается самой медленной из всех.
func_4 самая быстрая потому что по каунту сразу выбирается максимальное значение.
'''
