"""
Задание 4.
Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.
Сделайте профилировку каждого алгоритма через timeit
Попытайтесь написать третью версию, которая будет самой быстрой и по возможности самой лаконичной.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
Без аналитики задание считается не принятым!
"""
from collections import Counter
from timeit import *
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
    return Counter(array).most_common(1)


def func_4():
    word_count = {n: array.count(n) for n in set(array)}
    return max(word_count, key=word_count.get)




print(func_1())
print(func_2())
print(func_3()) # то есть цифра 1 трижды попадается
print(func_4())

print(min(repeat("func_1()", globals=globals(), timer=default_timer , number=100000)))
print(min(repeat("func_2()", globals=globals(), timer=default_timer , number=100000)))
print(min(repeat("func_3()", globals=globals(), timer=default_timer , number=100000)))
print(min(repeat("func_4()", globals=globals(), timer=default_timer , number=100000)))

# 4 функция на 2 месте по скорости