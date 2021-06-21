"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.

Без аналитики задание считается не принятым!
"""
from timeit import timeit
from cProfile import run

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
    max_count = max([(array.count(i), i) for i in set(array)])
    return f'Чаще всего встречается число {max_count[1]}, ' \
           f'оно появилось в массиве {max_count[0]} раз(а)'


print(timeit("func_1()", number=2500000, globals=globals()))
run('func_1()')

print(timeit("func_2()", number=2500000, globals=globals()))
run('func_2()')

print(timeit("func_3()", number=2500000, globals=globals()))
run('func_3()')

print(func_1())
print(func_2())
print(func_3())

# Для убедительности увеличил число повторений кода в 2.5 раза от стандарта, сделал следующие выводы:
# Из всех функций самая быстрая - функция 1
# Функция 2 немного медленнее чем моя Функция 3
