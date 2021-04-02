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
    max_3 = max(set(array), key=array.count)
    return f'Чаще всего встречается число {max_3}, ' \
           f'оно появилось в массиве {array.count(max_3)} раз(а)'


def func_4():
    m = 0
    num = 0
    for n, val in enumerate(array):
        count = array.count(val)
        if count > m:
            m = count
            num = val
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_5():
    max_3 = list((map(array.count, array)))
    return f'Чаще всего встречается число {array[max_3.index(max(max_3))]}, ' \
           f'оно появилось в массиве {max(max_3)} раз(а)'


print(func_1())
print(func_2())
print(func_3())
print(func_4())
print(func_5())

print(timeit('func_1()', setup='from __main__ import func_1, array', number=1000000))
print(timeit('func_2()', setup='from __main__ import func_2, array', number=1000000))
print(timeit('func_3()', setup='from __main__ import func_3, array', number=1000000))
print(timeit('func_4()', setup='from __main__ import func_4, array', number=1000000))
print(timeit('func_5()', setup='from __main__ import func_5, array', number=1000000))

"""
АНАЛИТИКА
Результат программы
Чаще всего встречается число 1, оно появилось в массиве 3 раз(а)
Чаще всего встречается число 1, оно появилось в массиве 3 раз(а)
Чаще всего встречается число 1, оно появилось в массиве 3 раз(а)
Чаще всего встречается число 1, оно появилось в массиве 3 раз(а)

Результат профилировки с помощью timeit
1.926926481  самый быстрый вариант, проход по массиву и поиск макcимального значения (count) 

2.6272854779999997  самый медленый вариант, слишком длинно (создание списка из значений количества вхождений каждого 
элемента спсика, затем поиск максимального значения в этом массиве и затем вывод значения элемента по индексу 
максимального элемента из массива количества вхождений).

2.0176655330000006  мой вариант, использовал функцию max передав ей в качестве параметра множество из array и 
key = array.count. Время получилось сравнимым с первым вариантом.


2.235842377000001  попробовал изменить первый вариант, сделал перебор элементов через enumerate. 
улучшения во времени не получил. вариант по времени на третьем месте.


2.631284147999999  вариант решения в строку через map.

ИТОГ ускорить задачу не получилось. хотя на уроках говорят, что вариант с max должен быть быстрее. А мои измерения 
этого не подтверждают.  То же с map, должно быть быстрее, но получилось медленее, очень долгой получился вывод числа 
(максимальное количество вхождений находится быстро, а поиск элемента с максимальным количестовом вхождений долгий).
Задание выполнено.

"""
