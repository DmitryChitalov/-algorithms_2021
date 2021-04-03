"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.

Без аналитики задание считается не принятым
"""
from timeit import timeit
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
    total = max(array, key=array.count)
    total_count = array.count(total)
    return f'Чаще всего встречается число {total}, ' \
           f'оно появилось в массиве {total_count} раз(а)'


print(f'1) {timeit("func_1()", "from __main__ import func_1", number=1000)}')  # -> 0.0013683999999999988
print(f'2) {timeit("func_2()", "from __main__ import func_2", number=1000)}')  # -> 0.0018441000000000013
print(f'3) {timeit("func_3()", "from __main__ import func_3", number=1000)}')  # -> 0.001180500000000001

"""
func_1 - самый медленный из-за перебора и сравнения
func_2 - быстрее, так как убрали сравнение
func_3 - самый быстрый из-за использования строенных функций. Изначально не хотел сохранять в переменные значения, 
в результате чего моя функция проигрывала, так как были повторные расчеты. После добавления переменных скорость
увеличилась
"""
