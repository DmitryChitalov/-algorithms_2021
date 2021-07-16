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
import cProfile


array = [1, 3, 1, 3, 4, 5, 1, 5, 3, 1, 3, 4, 5, 1, 5, 3, 1, 3, 4, 5, 1, 5, 3, 1, 3, 4, 5, 1, 5, 3, 1, 3, 4, 5, 1, 5]
# array = [1, 3, 1, 3, 4, 5, 1]


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
    result_dict = {key: array.count(key) for key in frozenset(array)}
    max_key = max(result_dict, key=result_dict.get)
    return f'Чаще всего встречается число {max_key}, ' \
           f'оно появилось в массиве {result_dict[max_key]} раз(а)'


print(func_1())
print(func_2())
print(func_3())

print(f'{timeit.timeit("func_1()", globals=globals())}'
      f'{timeit.timeit("func_2()", globals=globals())}'
      f'{timeit.timeit("func_3()", globals=globals())}')

# Профилировка
cProfile.run('func_1()')
cProfile.run('func_2()')
cProfile.run('func_3()')



"""
Третья версия проигрывает первой на небольшом объеме данных, но с ростом списка, достигается колоссальное преимущество.
По результатам профилировки, третья функция показала себя лучше с точки хрения количества вызовов сторонних функций. Так же, 
в первой функции cumtime = 0.001 {built-in method builtins.exec}, у второй и третьей он = 0.000. Так что считаю, что
мне удалось написать более быструю и лаконичную функцию

Пример 1:

array = [1, 3, 1, 3, 4, 5, 1]

func_1() = 1.1075807
func_2() = 1.4614282
func_3() = 1.3343798999999996 

Пример 2:
array = [1, 3, 1, 3, 4, 5, 1, 5, 3, 1, 3, 4, 5, 1, 5, 3, 1, 3, 4, 5, 1, 5, 3, 1, 3, 4, 5, 1, 5, 3, 1, 3, 4, 5, 1, 5]

func_1() = 11.8137892
func_2() = 12.620194100000003
func_3() = 2.468512899999997 
"""