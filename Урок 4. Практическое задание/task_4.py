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
import collections

# array = [1, 3, 1, 3, 4, 5, 1]

array = list(range(10000000))


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
    print(collections.Counter(array).most_common(1))


print(timeit('func_1', globals=globals()))
print(timeit('func_2', globals=globals()))
print(timeit('func_3', globals=globals()))

"""
интереса ради я увеличила массив, чтобы проследить за ассимптотикой
однако обе функции и при малых размерах массива, и при больших
показывают схожие результаты во времени, далее я добавила свою функцию,
используя модуль collections. Не скажу, что он показал лучший результат.
Но и не худший

0.027733899999999978
0.027584199999999948
0.02766370000000007

0.06227079999999996
0.044057799999999925
0.041028799999999976

0.05520170000000002
0.06711820000000007
0.07013290000000005

"""
