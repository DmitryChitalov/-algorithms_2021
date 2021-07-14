"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой и по возможности самой лаконичной.
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


def func_3():
    help_array = array[:]
    array.sort(key=lambda x:help_array.count(x))
    num =array[len(array)-1]
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {array.count(num)} раз(а)'





print(f'func_1 {timeit("func_1", globals=globals(), number=1000000)} sec')
print(f'func_2 {timeit("func_2", globals=globals(), number=1000000)} sec')
print(f'func_3 {timeit("func_3", globals=globals(), number=1000000)} sec')



print(func_1())
print(func_2())
print(func_3())

"""
1 замер
func_1 0.0769237 sec
func_2 0.10368179999999996 sec
func_3 0.0803008 sec

2 замер
func_1 0.11417079999999999 sec
func_2 0.10553549999999998 sec
func_3 0.07968409999999998 sec

3 замер
func_1 0.12520790000000004 sec
func_2 0.1333585 sec
func_3 0.1104018 sec

4 замер
func_1 0.1131658 sec
func_2 0.07750470000000001 sec
func_3 0.09476669999999998 sec

5 замер
func_1 0.1252431 sec
func_2 0.07156839999999998 sec
func_3 0.10795450000000001 sec

6 замер
func_1 0.1427121 sec
func_2 0.09637460000000003 sec
func_3 0.11389640000000006 sec

7 замер
func_1 0.08017650000000001 sec
func_2 0.0991801 sec
func_3 0.10890690000000003 sec

8 замер
func_1 0.11434100000000001 sec
func_2 0.11058989999999999 sec
func_3 0.06547720000000001 sec

9 замер
func_1 0.0933416 sec
func_2 0.09415079999999998 sec
func_3 0.07462229999999997 sec

10 замер
func_1 0.09074360000000001 sec
func_2 0.06606010000000001 sec
func_3 0.08806740000000002 sec

В 4 замерах из 10 мой вариант оказался быстрее обоех функций.
в 6 - быстрее func_1
в 5 - быстрее func_2
"""