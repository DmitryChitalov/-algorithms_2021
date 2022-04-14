"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой и по возможности самой лаконичной.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.

Без аналитики задание считается не принятым!
"""

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


print(func_1())
print(func_2())
# В словаре сохраняем частоту элемента как значение, его кол-во как значение
# По ключу(нашему числу) делаем + 1 в значение, если снова находим его в массиве
def func_3():
    my_dict = {}
    count, item = 0, ''
    for i in array:
        my_dict[i] = my_dict.get(i, 0) + 1
        if my_dict[i] >= count:
            count, item = my_dict[i], i
    print(my_dict)
    return f'Чаще всего встречается число {item}, ' \
           f'оно появилось в массиве {count} раз(а)'


def func_4():
    num = max(set(array), key=array.count)
    count = array.count(max(set(array), key=array.count))
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {count} раз(а)'


print(func_1())
print(func_2())
print(func_3())
print(func_4())

print(timeit.timeit(
    'func_1()',
    globals=globals(),
    number=10000
))

print(timeit.timeit(
    'func_2()',
    globals=globals(),
    number=10000
))

print(timeit.timeit(
    'func_3()',
    globals=globals(),
    number=10000
))

print(timeit.timeit(
    'func_4()',
    globals=globals(),
    number=10000
))

# 1: 0.4119513
# 2: 0.44372690000000004
# 3: 0.11191029999999991
# 4: 0.16496540000000004
#
# Я расширил массив для получения более наглядных чисел в замерах
# Функция 3, где использую словарь выполняется быстрее всех, так как операции со словарями имеют наименьшую сложность
# Функция 4 выполняется дольше функции 3, но быстрее остальных, так как работает через встроенную функцию max
# 4 функция получилась самой лаконичной
# В 1 функции имеем циклы, а во 2 используем цикл и встроенную функцию max + создаём новый массив. Наверное, поэтому 1 функция чуть быстрее
