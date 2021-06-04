"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.

Без аналитики задание считается не принятым!
"""
"""
func_3 - написание функции в одно строчку оказалось не столь эффективным и использование в ней лямбда-функции 
привело лишь к увеличению времени выполнения функции
func_4 - показала самые быстрые результаты за счёт функции set. Обращаясь к списку с готовыми внесёнными значениями
функция set выполняет меньшее количество итераций
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
    elem = max(array, key=lambda k: array.count(k))
    count = array.count(elem)
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {count} раз(а)'


def func_4():
    m = 0
    num = 0
    for i in set(array):
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


print(timeit('func_1()', globals=globals()))
print(timeit('func_2()', globals=globals()))
print(timeit('func_3()', globals=globals()))
print(timeit('func_4()', globals=globals()))
# print(func_1())
# print(func_2())
# print(func_3())
# print(func_4())

