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
    max_num = max(array, key=array.count)
    return f"Чаще всего встречается число {max_num}, оно появилось в массиве {array.count(max_num)} раз(а)"

print(func_3())

print(timeit("func_1()", globals = globals()))
print(timeit("func_2()", globals = globals()))
print(timeit("func_3()", globals = globals()))

# Быстрее всего выполнился вариант с использованием встроенной функцкции max, т.к. встроенные функции оптимизированы и чаще всего работают быстрее
# Второй вариант работает дольше всех, т.к. в нём создаётся ещё один массив и в нём ищется максимальное число