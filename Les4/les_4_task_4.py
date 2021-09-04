import timeit
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
    return max(set(array), key=array.count)


print(f"Анализ функции 1 через timeit: {timeit.timeit('func_1()', setup='from __main__ import func_1', number=10000)}")
print(f"Анализ функции 2 через timeit: {timeit.timeit('func_2()', setup='from __main__ import func_2', number=10000)}")
print(f"Анализ функции 3 через timeit: {timeit.timeit('func_3()', setup='from __main__ import func_3', number=10000)}")

"""Задача ускоренна"""
