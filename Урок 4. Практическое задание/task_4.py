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
    m = max(array, key=array.count)
    return f'Чаще всего встречается число {m}, ' \
           f'оно появилось в массиве {array.count(m)} раз(а)'



print(func_1(),'- ', timeit("func_1()", "from __main__ import func_1"), "seconds")
print(func_2(),'- ', timeit("func_2()", "from __main__ import func_2"), "seconds")
print(func_3(),'- ', timeit("func_3()", "from __main__ import func_3"), "seconds")

""" Результаты таковы:
Чаще всего встречается число 1, оно появилось в массиве 3 раз(а) -  1.8887033 seconds
Чаще всего встречается число 1, оно появилось в массиве 3 раз(а) -  2.6018870000000005 seconds
Чаще всего встречается число 1, оно появилось в массиве 3 раз(а) -  1.7654854999999996 seconds

Самая медленная функция - func_2, причина - метод append, 1-ая и 3-ая - результаты одинаковые, но func_3 более
лаконичная и короткая.   
"""

