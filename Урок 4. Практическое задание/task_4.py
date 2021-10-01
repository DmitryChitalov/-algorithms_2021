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
from collections import Counter

array = [1, 2, 3, 3, 4, 5, 6, 7, 8, 9, 3, 1, 3, 4, 5, 1, 3, 3, 3]
array2 = array * 3

def func_1(array):
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2(array):
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def func_3(array):
    my_dict = {}
    for i in array:
        my_dict[i] = my_dict.get(i, 0) + 1
    num = max(my_dict, key=lambda x: my_dict[x])
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {my_dict[num]} раз(а)'


def func_4(array):
    b = Counter(array).most_common(1)
    return f'Чаще всего встречается число {b[0][0]}, ' \
           f'оно появилось в массиве {b[0][1]} раз(а)'

def func_5(array):
    num = max(array, key=array.count)
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {array.count(num)} раз(а)'

print(func_1(array))
print(func_2(array))
print(func_3(array))
print(func_4(array))
print(func_5(array))

print(f'1 тест, {len(array)} элементов.')
print('func_1', timeit("func_1(array)",setup='from __main__ import func_1, array',number=10000))
# от 0.0375511 до 0.0407031
print('func_2',timeit("func_2(array)",setup='from __main__ import func_2, array',number=10000))
# от 0.0483795 до 0.0493379
print('func_3',timeit("func_3(array)",setup='from __main__ import func_3, array',number=10000))
# 0.0257253 до 0.0289777
print('func_4',timeit("func_4(array)",setup='from __main__ import func_4, array',number=10000))
# 0.0278236 до 0.0291915
print('func_5',timeit("func_5(array)",setup='from __main__ import func_5, array',number=10000))
# от 0.0390369 до 0.0414316
"""
Было проведено 2 теста с разным количеством входящих данных.
Первый тест с списком из 19 эелментов (array).
Чаще всего наиболее быстро с задачей справляется функция func_3, использующая для подсчета количества вхождений 
элементов словарь, однако иногда func_4 исполнялась быстрее.
На втором месте по скорости функция func_4, использующая встроенную библиотеку collections модуль Counter.
На третьем месте func_5, изпользующая max() c ключом по количетсву элементов в массиве. "max(array, key=array.count)."
На четвертом func_1, за один перебор определяющая элемент, встречающийся наибольшее число раз.
На последнем месте func_2, создающая новый список, и заполняющая его количеством встречающихся элементов. Ее время самое
большое, так как она создает второй список таких же размеров, как и входящий, при больших значениях списка время
увеличилось бы еще сильнее.
"""
print(f'2 тест, {len(array2)} элементов.')
print('func_1', timeit("func_1(array2)",setup='from __main__ import func_1, array2',number=10000))
# от 0.252400 до 0.2637329
print('func_2',timeit("func_2(array2)",setup='from __main__ import func_2, array2',number=10000))
# от 0.2701134 до 0.2847007
print('func_3',timeit("func_3(array2)",setup='from __main__ import func_3, array2',number=10000))
# 0.04591129 до 0.0518132
print('func_4',timeit("func_4(array2)",setup='from __main__ import func_4, array2',number=10000))
# 0.0357803 до 0.0376197
print('func_5',timeit("func_5(array2)",setup='from __main__ import func_5, array2',number=10000))
# 0.2559017 до 0.2655741
"""
Второй тест с списком из 57 эелментов (array2).
На первое место по скорости вышла функция func_4 с заметным отрывом. Импортированный модуль, специализированный
для решения таких задач, справляетя быстрее вручную написанных функций.
На втором месте по скорости функция func_3, на создание и перебор словаря тратится меньше времени,чем перебор по списку.
На третьем месте все так же func_5. Встроенный в python метод подсчета опять опережает вручную созданные функции, однако 
проигрывает функциям, основанным на словаре и collections.
На четвертом месте func_1, за один перебор определяющая элемент, встречающийся наибольшее число раз.
На последнем месте остается func_2.
"""
