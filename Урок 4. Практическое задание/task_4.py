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
    m, num, j = 0, 0, 0
    ar_set = set(array)
    for i in ar_set:
        count = array.count(i)
        if count > m:
            num, m = i, count
            del array[j]
            j += 1
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


array = [1, 3, 1, 3, 4, 5, 1]
print(func_1())
print(func_2())
print(func_3())
t1 = Timer("func_1()", "from __main__ import func_1, array")
print(f'Суммарное время 10000 запусков func_1 {t1.timeit(number=10000) * 1000:.3f} мсек')
print('*' * 6)
t2 = Timer("func_2()", "from __main__ import func_2, array")
print(f'Суммарное время 10000 запусков func_2 {t2.timeit(number=10000) * 1000:.3f} мсек')
print('*' * 6)
t3 = Timer("func_3()", "from __main__ import func_3, array")
print(f'Суммарное время 10000 запусков func_3 {t3.timeit(number=10000) * 1000:.3f} мсек')
'''
в func_3 алгоритме лучшее время
за счёт уменьшения числа циклов подсчёта - используя множество вместо списка
и сокрашения елементов для подсчёта - удаления елемента после подсчёта из списка
'''
