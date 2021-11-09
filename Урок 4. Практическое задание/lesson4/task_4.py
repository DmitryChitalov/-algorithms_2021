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
    return f'Чаще всего встречается число {max(array, key=array.count)}, ' \
           f'оно появилось в массиве {array.count(max(array, key=array.count))} раз(а)'


print(func_1())
print(func_2())
print(func_3())


print(timeit('func_1()', globals=globals(), number=1000000))
print(timeit('func_2()', globals=globals(), number=1000000))
print(timeit('func_3()', globals=globals(), number=1000000))

'''
Вывод
Выполение первой функции заняло меньше всего времени, 
несмотря на отсутсвие в коде встроеной функции,
Остальные функции выполнены в 1,5 и 2 раза дольше.
'''
