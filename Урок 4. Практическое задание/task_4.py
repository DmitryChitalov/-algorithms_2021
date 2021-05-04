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
    symb_func = max(array, key=array.count)
    return f'Чаще всего встречается число {symb_func}, ' \
           f'оно появилось в массиве {array.count(symb_func)} раз(а)'

print(func_1())
print(func_2())
print(func_3())

print('func_1:', timeit('func_1()', globals=globals(), number=10000))
print('func_2:', timeit('func_2()', globals=globals(), number=10000))
print('func_3:', timeit('func_3()', globals=globals(), number=10000))

"""
Вывод:
Первый вариант работает быстрее второго, т.к. находит искомое за первый раш по списку. 
Второй затрачивает время на поиск макс элемента и на создание доп. списка
Третий вариант чуть лучше по производительности за счет встроенных фуккций. Ускорение получилось по 3му варианту

Детали ниже:
func_1: 0.018410800000000005
func_2: 0.022318899999999996
func_3: 0.017402200000000007
"""
