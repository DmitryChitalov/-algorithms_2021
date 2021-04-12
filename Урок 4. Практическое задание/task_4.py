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


#  используем словарь для хранения расчетов и поиска в нем максимального значения
def func_3():
    d = {x: array.count(x) for x in set(array)}
    elem = max(d, key=lambda k: d[k])
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {d[elem]} раз(а)'


#  используем сортировку над словарем
def func_4():
    d = sorted([(i, array.count(i)) for i in set(array)], key=lambda t:t[1])[-1]
    return f'Чаще всего встречается число {d[0]}, ' \
           f'оно появилось в массиве {d[1]} раз(а)'

#  используем max сразу над списком кортежей
def func_5():
    d = max([(array.count(i), i) for i in set(array)])
    return f'Чаще всего встречается число {d[1]}, ' \
           f'оно появилось в массиве {d[0]} раз(а)'


print(func_1())
print(func_2())
print(func_3())
print(func_4())
print(func_5())

print('func_1',
      round(
          timeit(
              'func_1()',
              globals=globals(),
              number=3000000)
          , 4),
      'seconds')

print('func_2',
      round(
          timeit(
              'func_2()',
              globals=globals(),
              number=3000000)
          , 4),
      'seconds')

print('func_3',
      round(
          timeit(
              'func_3()',
              globals=globals(),
              number=3000000)
          , 4),
      'seconds')

print('func_4',
      round(
          timeit(
              'func_4()',
              globals=globals(),
              number=3000000)
          , 4),
      'seconds')

print('func_5',
      round(
          timeit(
              'func_5()',
              globals=globals(),
              number=3000000)
          , 4),
      'seconds')
"""
func_1 4.2598 seconds
func_2 6.0176 seconds
func_3 6.5278 seconds
func_4 6.1196 seconds
func_5 5.2431 seconds
ВЫВОД:
Реализации func_1 быстрее, чем func_2, т.к. код второй функции более "громоздкий", т.к. содержит дополниельные операции
со списком, в то время как первая функция использует только простой оператор "if..." в дополнение к операции count.
Функции func_3 и func_4, несмотря на то, что содержат меньше операций count за счет предварительного построения 
множества, не показали улучшение в быстродействии, вероятно, за счет дополнительной сортировки по данным в словаре.
Реализация func_5 оказалась быстрее func_2, func_3, func_4 за счет меньшего количества операций для поиска максимального 
значения. Но все равно самый оптимальный вариант по скорости - это функция func_1, т.к. она имеет наименьшее количество 
"лишних" действий в коде.
"""
