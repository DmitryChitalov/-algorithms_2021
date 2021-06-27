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
    elem = max(array, key=array.count)
    count = array.count(elem)
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {count} раз(а)'


print(func_1())
print(func_2())
print(func_3())

print(f"Время работы функции {func_1.__name__} составило {timeit('func_1', globals=globals())} сек.")
print(f"Время работы функции {func_2.__name__} составило {timeit('func_2', globals=globals())} сек.")
print(f"Время работы функции {func_3.__name__} составило {timeit('func_3', globals=globals())} сек.")

"""
Отчет из модуля профилирования timeit:
Время работы функции func_1 составило 0.0730176 сек.
Время работы функции func_2 составило 0.07358469999999998 сек.
Время работы функции func_3 составило 0.06716820000000001 сек.
Вывод исходя из данных модуля, видно что моя функция  - func_3, более быстрая чем две предедущие, ориентировачно на 8%
быстрее.
"""