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

# def func_3():
#     dict = {}
#     for i in array:
#         dict[i] = array.count(i)
#     for k, v in dict.items():
#         if v == max(dict.values()):
#             return f'Чаще всего встречается число {k}, ' \
#            f'оно появилось в массиве {v} раз(а)'

def func_3():
    for i in array:
        return f'Чаще всего встречается число {i}, ' \
           f'оно появилось в массиве {max(i, array.count(i))} раз(а)'





print(func_1())
print(func_2())
print(func_3())
# print(timeit("func_1()", "from __main__ import func_1"))
# print(timeit("func_2()", "from __main__ import func_2"))
# print(timeit("func_3()", "from __main__ import func_3"))

"""
func_1 - сложность O(n)
func_2 - наверное тут O(n) + O(n) = 2 O(n). И эта двойка тут как раз немного увеличивает время исполнения функции
func_3 - цикл без присваиваний переменных или сравнений. Все делает функция max
"""