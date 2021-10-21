"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой и по возможности самой лаконичной.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.

Без аналитики задание считается не принятым!
"""
import timeit


array = [1, 3, 1, 3, 3, 3, 3, 4, 5, 1, 4, 4, 4]


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
    max_2 = max(array, key=array.count)
    elem = array.count(max_2)
    return f'Чаще всего встречается число {max_2}, ' \
           f'оно появилось в массиве {elem} раз(а)'


print(func_1())
print(func_2())
print(func_3())


print(f'func_1 {timeit.timeit("func_1()", number=100000, globals=globals())}')
print(f'func_2 {timeit.timeit("func_2()", number=100000, globals=globals())}')
print(f'func_3 {timeit.timeit("func_3()", number=100000, globals=globals())}')


# Вариант 1 самый быстрый потому, что не формирует новый массив,
# но иногда внутренняя конструкция max быстрей видно из-за внутренней оптимизации. Вариант 1 создает дополнительные переменные, а функция 3 нет
