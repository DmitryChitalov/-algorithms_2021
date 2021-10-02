"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой и по возможности самой лаконичной.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.

Без аналитики задание считается не принятым!
"""


from collections import Counter
import timeit


array = [1, 3, 1, 3, 4, 5, 1, 4, 6]


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
    return max(array, key=array.count)


def func_4():
    return Counter(array).most_common(1)


# Сложность в O нотации вроде бы одинаковая, но из-за разной реализации и скорости тоже разные.
# В первом варианте мы используем if и присваивание в переменные, что является быстрыми операциями.
# Во втором мы используем список для записи, что незначительно, но, все таки, замедляет программу.
# В моем третьем варианте используется параметр функции max() работает быстро.
# Последний вариант с Counter слишком медленный.


if __name__ == '__main__':
    a1 = timeit.timeit('func_1()', globals=globals(), number=1000000)
    a2 = timeit.timeit('func_2()', globals=globals(), number=1000000)
    a3 = timeit.timeit('func_3()', globals=globals(), number=1000000)
    a4 = timeit.timeit('func_4()', globals=globals(), number=1000000)
    print(a1, a2, a3, a4)  # 2.2842565 2.8724534 1.7687995 3.498960200000001
