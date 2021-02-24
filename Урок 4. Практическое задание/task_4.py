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
    elem = max(zip((array.count(i) for i in set(array)), set(array)))
    return f'Чаще всего встречается число {elem[1]}, ' \
           f'оно появилось в массиве {elem[0]} раз(а)'


t_1 = timeit('func_1', setup='from __main__ import func_1', number=1000000)
print('func_1 meter often number', t_1, 'msec')
print()
t_2 = timeit('func_2', setup='from __main__ import func_2', number=1000000)
print('func_2 meter often number', t_2, 'msec')
print()
t_3 = timeit('func_3', setup='from __main__ import func_3', number=1000000)
print('func_3 meter often number', t_3, 'msec')


"""
Результаты теста на моём пк:
func_1 meter often number 0.022395121999579715 msec
func_2 meter often number 0.014730562001204817 msec
func_3 meter often number 0.011786991002736613 msec

Как мы видим что оптимизация кода и ускорение работы удалось.
Первое место по скорости func_3 так как использование встроенных функций это
наиболее быстрый выбор.
Второе место по скорости func_2 так как используется функция append она будет
всегда среднем по скорости решением для списков.
Третье место func_1 так как в цикле for используется ещё и выполнение условия,
а это повышает сложность и время выполнения алгоритма.
"""
