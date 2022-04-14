"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой и по возможности самой лаконичной.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.

Без аналитики задание считается не принятым!
"""
from timeit import timeit, repeat, default_timer

ARRAY = [1, 3, 1, 3, 4, 5, 1]


def func_1():
    m = 0
    num = 0
    for i in ARRAY:
        count = ARRAY.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in ARRAY:
        count2 = ARRAY.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = ARRAY[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def func_3():
    number = max(set(ARRAY), key=ARRAY.count)
    return f'Чаще всего встречается число {number}, ' \
           f'оно появилось в массиве {ARRAY.count(number)} раз(а)'


print(func_1())
print(func_2())
print(func_3())
print('func_1 -', timeit('func_1()', globals=globals()))  # func_1 - 1.5493675280013122
print('func_2 -', timeit('func_1()', globals=globals()))  # func_2 - 1.5341149199994106
print('func_3 -', timeit('func_3()', globals=globals()))  # func_3 - 1.537923857998976

print('func_1 -', repeat('func_1()', default_timer, repeat=3, globals=globals()))
print('func_2 -', repeat('func_1()', default_timer, repeat=3, globals=globals()))
print('func_3 -', repeat('func_3()', default_timer, repeat=3, globals=globals()))

# func_1 - [1.5370922250003787, 1.5314240439984133, 1.5542775920002896]
# func_2 - [1.5232089599994652, 1.5135600980029267, 1.526224571000057]
# func_3 - [1.593124388000433, 1.5921677420010383, 1.6106559059990104]

# Как сделть быстрее я не придумал. Все алгоритмы на моем железе работают примерно
# одинаково, у меня нет этому обьясния, в разборе у вас вариант с max() явно быстрее
# может это изза того что у меня python 3.8 или ос Linux Ubuntu?
