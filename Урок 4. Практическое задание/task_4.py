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
from random import randint


#array = [1, 1, 3, 1, 3, 4, 4, 4, 4, 4, 5, 1]
arr_1 = [randint(0, 9) for i in range(10)]
arr_2 = [randint(0, 9) for i in range(100)]
arr_3 = [randint(0, 9) for i in range(1000)]
print(arr_1)
print(arr_2)
print(arr_3)


def func_1(array):  # сложность - O(N^2)
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2(array):  # сложность - O(N^2)
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def func_3(array):  # сложность - O(N)
    cache = {}
    for num in array:
        if num in cache:
            cache[num] += 1
        else:
            cache[num] = 1
    keys = list(cache.keys())
    values = list(cache.values())
    max_count = values.index(max(values))
    max_num = keys[max_count]
    return f'Чаще всего встречается число {max_num}, ' \
           f'оно появилось в массиве {values[max_count]} раз(а)'


print(func_1(arr_1))
print(func_2(arr_1))
print(func_3(arr_1))
print('Массив из 10 эл-тов:')
print('1 функция:', timeit('func_1(arr_1)', globals=globals(), number=10000))
print('2 функция:', timeit('func_2(arr_1)', globals=globals(), number=10000))
print('3 функция:', timeit('func_3(arr_1)', globals=globals(), number=10000))
print('Массив из 100 эл-тов:')
print('1 функция:', timeit('func_1(arr_2)', globals=globals(), number=10000))
print('2 функция:', timeit('func_2(arr_2)', globals=globals(), number=10000))
print('3 функция:', timeit('func_3(arr_2)', globals=globals(), number=10000))
print('Массив из 1000 эл-тов:')
print('1 функция:', timeit('func_1(arr_3)', globals=globals(), number=10000))
print('2 функция:', timeit('func_2(arr_3)', globals=globals(), number=10000))
print('3 функция:', timeit('func_3(arr_3)', globals=globals(), number=10000))

'''
Массив из 10 эл-тов:
1 функция: 0.017991200000000002
2 функция: 0.0243702
3 функция: 0.0176722
Массив из 100 эл-тов:
1 функция: 0.9729201999999999
2 функция: 1.0175169000000002
3 функция: 0.09427610000000008
Массив из 1000 эл-тов:
1 функция: 90.0322089
2 функция: 90.37662
3 функция: 0.8478375999999912

При малых длинах входного массива моя функция показывает сопоставимое время выполнения.
Ожидаемо при увеличении кол-ва данных время выполнения растет на порядки медленее.
'''