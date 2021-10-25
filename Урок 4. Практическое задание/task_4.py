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
    res = max(array, key=array.count)
    counter = array.count(res)
    return f'Чаще всего встречается число {res}, ' \
           f'оно появилось в массиве {counter} раз(а)'


print(f' Время выполнения func_1: {timeit("func_1()", globals=globals())} ', '\n'
      f' Результат: {func_1()}')    # 2.5003295999922557
print(f' Время выполнения func_2: {timeit("func_2()", globals=globals())} ', '\n'
      f' Результат: {func_2()}')    # 3.289282399986405
print(f' Время выполнения func_3: {timeit("func_3()", globals=globals())} ', '\n'
      f' Результат: {func_3()}')    # 2.586688099996536

"""самая быстрая функция по результатам timeit это func_1,
func_3 (написанная пользователем) уступает по времени не более 3,5-5%
--
пытаясь ускорить удалил из res = max(set(array), key=array.count)
set (хотя он там и изначально не особо был нужен)
следовательно - у меня не вышло создать функцию более быструю, чем есть в задании
"""