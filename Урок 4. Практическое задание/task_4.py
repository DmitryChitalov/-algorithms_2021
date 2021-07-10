"""
Задание 4.
Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.
Сделайте профилировку каждого алгоритма через timeit
Попытайтесь написать третью версию, которая будет самой быстрой и по возможности самой лаконичной.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
Без аналитики задание считается не принятым!
"""
from timeit import timeit
from collections import Counter

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
    n = Counter(array).most_common(1)[0]
    return f'Чаще всего встречается число {n[0]}, ' \
           f'оно появилось в массиве {n[1]} раз(а)'


print(func_1())
print(func_2())
print(func_3())

print('1: ', timeit('func_1', globals=globals()))
print('2: ', timeit('func_2', globals=globals()))
print('3: ', timeit('func_3', globals=globals()))

'''
1:  0.0176186
2:  0.0167821
3:  0.01577139999999999

Третий вариант через Counter работает немного быстрее остальных, что видно по замерам.
Однако при запуске кода несколько раз замеры выдают разные значения,
и иногда 3 вариант не выходит самым быстродейственным. 
Честно говоря, так и не поняла, как решить данную проблему.
'''