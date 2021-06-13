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


def func_3(user_array):
    new_array = {}
    for el in user_array:
        if not new_array.get(el):
            count2 = user_array.count(el)
            new_array[el] = count2
    max_el = max(new_array, key=lambda x: new_array[x])
    return f'Чаще всего встречается число {max_el}, ' \
           f'оно появилось в массиве {new_array[max_el]} раз(а)'


print(func_1())
print(func_2())
print(func_3(array))

print(timeit("func_1()", globals=globals(), number=100))
print(timeit("func_2()", globals=globals(), number=100))
print(timeit("func_3(array)", globals=globals(), number=100))

"""
Запуск 1:
0.0002176999999999943
0.00026480000000000253
0.00022330000000000266

Запуск 2:
0.00021469999999999823
0.0003029999999999977
0.0002129999999999979

Запуск 3:
0.00016269999999999826
0.0003339999999999975
0.00044750000000000345

Исходя из замеров нескольких запусков, можно сделать вывод о том, что первая реализация является самой эффективной,
а вторая и третья выполняются примерно в одно время, хотя вторая оказывается быстрее чаще, чем третья. Ускорить задачу 
не получилось.
"""