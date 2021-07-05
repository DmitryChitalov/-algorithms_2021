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


# лаконично
def func_3():
    return f'Чаще всего встречается число {max(array, key=array.count)}, ' \
           f'оно появилось в массиве {array.count(max(array, key=array.count))} раз(а)'


# лаконично-2
def func_4():
    c = (Counter(array)).most_common(1)
    return f'Чаще всего встречается число {c[0][0]}, ' \
           f'оно появилось в массиве {c[0][1]} раз(а)'


print(func_1())
print(func_2())
print(func_3())
print(func_4())
print(func_1.__name__, timeit('func_1()', globals=globals(), number=20000))
print(func_2.__name__, timeit('func_2()', globals=globals(), number=20000))
print(func_3.__name__, timeit('func_3()', globals=globals(), number=20000))
print(func_4.__name__, timeit('func_4()', globals=globals(), number=20000))

# func_1 0.019907700000000004
# func_2 0.0273066
# func_3 0.0352397
# func_4 0.0459508

# Увы я не придумал как ускорить код. Две написанные функции хоть и лаконичны,
# но не быстродейственны.
