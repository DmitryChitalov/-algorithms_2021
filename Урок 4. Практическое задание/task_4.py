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
    num = max(array, key=lambda x: array.count(x))
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {array.count(num)} раз(а)'


def func_4():
    cnt = Counter(array)
    num = max(cnt, key=cnt.get)
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {cnt.get(num)} раз(а)'


def func_5():
    cnt = {}
    for i in set(array):
        cnt[i] = 0
        for j in array:
            if i == j:
                cnt[i] += 1
    num = max(cnt, key=cnt.get)
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {cnt.get(num)} раз(а)'


print(func_1())
print(func_2())
print(func_3())
print(func_4())
print(func_5())

print(timeit("func_1()", globals=globals(), number=100000))
print(timeit("func_2()", globals=globals(), number=100000))
print(timeit("func_3()", globals=globals(), number=100000))
print(timeit("func_4()", globals=globals(), number=100000))
print(timeit("func_5()", globals=globals(), number=100000))

# Функции 3 и 4 самые лаконичные, но используемые встроенные функции задачу не ускоряют, лишь функция 3 показывает
# идентичные результаты с функцией 2. Самая быстрая - функция 1, с наименьшим числом сложных вызовов. Функция 5 быстрее
# аналогичной функции 4, но не использует collections.Counter()
