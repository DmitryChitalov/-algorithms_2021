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
import random

array = [int(random.randrange(0,10)) for _ in range(100)]
#array = [1, 3, 1, 3, 4, 5, 1]


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

############################################################

def counter_num():
    '''
    Поиск по сортированному списку
    '''
    res = sorted([(i,array.count(i)) for i in set(array)],key=lambda t:t[1])[-1]
    return f'Чаще всего встречается число {res[0]}, ' \
           f'оно появилось в массиве {res[1]} раз(а)'

def max_count():
    res = max(array, key=array.count)
    return f'Чаще всего встречается число {res}, ' \
           f'оно появилось в массиве {array.count(res)} раз(а)'


print(f"counter_num: {counter_num()}")
print(f"max_count: {max_count()}")

print(f"func_1 time: {timeit('func_1()',setup='from __main__ import func_1,array',number=1000)}")
print(f"func_2 time: {timeit('func_2()',setup='from __main__ import func_2,array',number=1000)}")
print(f"counter_num() time: {timeit('counter_num()',setup='from __main__ import counter_num,array',number=1000)}")
print(f"max_count() time: {timeit('max_count()',setup='from __main__ import max_count,array',number=1000)}")
##########################################################################

'''


Для 100 элементов:

func_1 time: 0.24799100000000002
func_2 time: 0.19747110000000007
counter_num() time: 0.031702600000000025
max_count() time: 0.19539099999999998

Для 1000 элементов:

func_1 time: 15.1299451
func_2 time: 14.521449000000002
counter_num() time: 0.16786860000000203
max_count() time: 14.425566200000002

Из замеров следует что функция counter_num() рализованная 
через встроенную функцию (sorted() алгоритм Timsort) наиболее эффективна 
'''