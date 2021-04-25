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

array = [1, 3, 1, 3, 4, 5, 1, 3, 4, 3]


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
    my_set = set(array)
    most_common = 0
    most_common_count = 0
    for el in my_set:
        count = array.count(el)
        if count > most_common_count:
            most_common_count = count
            most_common = el
    return f'Чаще всего встречается число {most_common},' \
           f'оно появилось в массиве {most_common_count} раз(а)'

def func_4():
    num = max(array, key=array.count)
    return f'Чаще всего встречается число {num},' \
           f'оно появилось в массиве {array.count(num)} раз(а)'

print(func_1())
print(func_2())
print(func_3())
print(func_4())

print(timeit('func_1()', globals=globals(), number=10000))
print(timeit('func_2()', globals=globals(), number=10000))
print(timeit('func_3()', globals=globals(), number=10000))
print(timeit('func_4()', globals=globals(), number=10000))

"""
Время выполнения функций
0.055017399999999994
0.09815039999999997
0.02936749999999999
0.03845449999999995
Анализ:
Самый медленный вариант №2. Создается второй список со счетчиком элементов, 
из него выбирается максимально значение
Самый быстрый вариант №3. Создается кортеж из списка, элементы списка поочердно сравниваются
со значениями из кортежа.
"""
