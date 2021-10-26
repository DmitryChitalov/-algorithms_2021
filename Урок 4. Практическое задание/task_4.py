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
from collections import Counter

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
    a_set = set(array)
    elem = None  # наиболее часто встречаемое значение
    max_2 = 0  # его количество, в цикле перебираются элементы (item) множества
    for item in a_set:
        qty = array.count(item)  # переменной qty присваивается количество случаев item в списке array
        if qty > max_2:  # Если это количество больше максимального,
            max_2 = qty  # то заменяем на него максимальное,
            elem = item  # запоминаем само значение
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


print(func_1())
t1 = Timer("func_1()", "from __main__ import func_1")
print("list func_1 ", t1.timeit(number=1000), "milliseconds")

print(func_2())
t2 = Timer("func_2()", "from __main__ import func_2")
print("list func_2 ", t2.timeit(number=1000), "milliseconds")

print(func_3())
t3 = Timer("func_3()", "from __main__ import func_3")
print("list func_3 ", t3.timeit(number=1000), "milliseconds")

'''
Вывод: 
    func_3 - работает быстрее всех, т.к использует множества
Чаще всего встречается число 1, оно появилось в массиве 3 раз(а)
list func_1  0.001902900000000006 milliseconds
Чаще всего встречается число 1, оно появилось в массиве 3 раз(а)
list func_2  0.0029677999999999996 milliseconds
Чаще всего встречается число 1, оно появилось в массиве 3 раз(а)
list func_3  0.0016129000000000004 milliseconds
'''