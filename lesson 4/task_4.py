"""
Задание 4.
Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.
Сделайте профилировку каждого алгоритма через timeit
Попытайтесь написать третью версию, которая будет самой быстрой и по возможности самой лаконичной.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
Без аналитики задание считается не принятым!
"""
import random
import timeit
import cProfile

array = [random.randint(0, 10) for el in range(10)]

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
    max_3 = max(array, key=lambda i: array.count(i))
    return f'Чаще всего встречается число {max_3}, ' \
           f'оно появилось в массиве {array.count(max_3)} раз(а)'
def func_4():
    max_4 = max(array, key=array.count)
    return f'Чаще всего встречается число {max_4}, ' \
           f'оно появилось в массиве {array.count(max_4)} раз(а)'
print(func_1())
print(func_2())
print(func_3())
print(func_4())

print(
    timeit.timeit(
        "func_1()",
        globals=globals(),
        number=1000000))
print(
    timeit.timeit(
        "func_2()",
        globals=globals(),
        number=1000000))

print(
    timeit.timeit(
        "func_3()",
        globals=globals(),
        number=1000000))

print(
    timeit.timeit(
        "func_4()",
        globals=globals(),
        number=1000000))

cProfile.run('func_1()')
cProfile.run('func_2()')
cProfile.run('func_3()')
cProfile.run('func_4()')
"""
Лаконичность у func_3 появилась, но быстрее сделать не вышло.
Лучший вариант func_4.
"""