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


def func_3():
    most_frequent = max(array, key=array.count)
    return f'Чаще всего встречается число {most_frequent}, ' \
           f'оно появилось в массиве {array.count(most_frequent)} раз(а)'


def func_4():
    tpl_most_frequent = Counter(array).most_common(1)[0]
    return f'Чаще всего встречается число {tpl_most_frequent[0]}, ' \
           f'оно появилось в массиве {tpl_most_frequent[1]} раз(а)'



print(func_1())
print(func_2())
print(func_3())
print(func_4())

# Измерения
TEST_COUNT = 10_000
print("Выполнение функции func_1 занимает: ", timeit("func_1()", globals=globals(), number=TEST_COUNT), " сек.")
print("Выполнение функции func_2 занимает: ", timeit("func_2()", globals=globals(), number=TEST_COUNT), " сек.")
print("Выполнение функции func_3 занимает: ", timeit("func_3()", globals=globals(), number=TEST_COUNT), " сек.")
print("Выполнение функции func_4 занимает: ", timeit("func_4()", globals=globals(), number=TEST_COUNT), " сек.")


"""
Самым локаничным получился вариант 3-й вариант функции. По скорости он оказался чуть хуже классического цикла.
Поскольку max() создает словарь, а это требует дополнительного времени. 
Самым худшим, неожиданно, оказался Counter из модуля collections.
"""
"""
Чаще всего встречается число 1, оно появилось в массиве 3 раз(а)
Чаще всего встречается число 1, оно появилось в массиве 3 раз(а)
Чаще всего встречается число 1, оно появилось в массиве 3 раз(а)
Чаще всего встречается число 1, оно появилось в массиве 3 раз(а)
Выполнение функции func_1 занимает:  0.010054499999999997  сек.
Выполнение функции func_2 занимает:  0.013664799999999998  сек.
Выполнение функции func_3 занимает:  0.012641300000000001  сек.
Выполнение функции func_4 занимает:  0.026102099999999996  сек.
"""
