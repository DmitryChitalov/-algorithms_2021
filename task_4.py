"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.

Без аналитики задание считается не принятым
"""
import timeit
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
    total = (max(array, key=array.count))
    total_n = array.count(total)
    return f'Чаще всего встречается число {total} '\
    f'оно появилось в массиве {total_n} раз(а)'



print(func_1())
print(func_2())
print(func_3())
print('1 -- ', timeit.timeit('func_1()', 'from __main__ import func_1', number=1000))
print('2 -- ', timeit.timeit('func_2()', 'from __main__ import func_2', number=1000))
print('3 -- ', timeit.timeit('func_3()', 'from __main__ import func_3', number=1000))

#1 --  0.0017514000000000002
#2 --  0.0020217000000000013
#3 --  0.001446900000000001
#в первых двух случаях происходят переборы и сравнение,
# в третьем варианте используется встроеная функция она по скорости чуть быстрее