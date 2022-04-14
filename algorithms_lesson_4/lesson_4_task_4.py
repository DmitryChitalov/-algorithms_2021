from collections import Counter
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


def func_3(array):
    return f'Чаще всего встречается число {max(a for a in array if array.count(a) == max(map(array.count, array)))}, ' \
           f'оно появилось в массиве {max(map(array.count, array))} раз(а)'


def func_4():
    result = max(array, key=array.count)
    return f'Чаще всего встречается число {result}, оно появилось в массиве {array.count(result)} раз(а)'


print(func_1())
print(func_2())
print(func_3(array))
print(func_4())
print('#######################################################################')

print(f'Time for func_1 is {timeit("func_1()", globals=globals())} seconds')
print(f'Time for func_2 is {timeit("func_2()", globals=globals())} seconds')
print(f'Time for func_3 is {timeit("func_3(array)", globals=globals())} seconds')
print(f'Time for func_4 is {timeit("func_4()", globals=globals())} seconds')

'''
Чаще всего встречается число 1, оно появилось в массиве 3 раз(а)
Чаще всего встречается число 1, оно появилось в массиве 3 раз(а)
Чаще всего встречается число 1, оно появилось в массиве 3 раз(а)
Чаще всего встречается число 1, оно появилось в массиве 3 раз
#######################################################################
Time for func_1 is 2.5835666 seconds
Time for func_2 is 3.787106 seconds
Time for func_3 is 17.4165689 seconds
Time for func_4 is 2.546348000000002 seconds
Вывод: наиболее эффективно первое решение. Попытка оптимизации алгоритма не удалась, хотя решения 3 и 4 более лаконичны. 
'''
