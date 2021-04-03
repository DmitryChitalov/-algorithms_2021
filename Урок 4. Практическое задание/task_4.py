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
from collections import Counter
from statistics import mode
from random import randint

#array = [1, 3, 1, 3, 4, 5, 1]
array = [randint(-10, 10) for i in range(100)]


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
    return f'Чаще всего встречается число {max(set(array), key = array.count)}'


def func_4():
    occurence_count = Counter(array)
    return f'Чаще всего встречается число {occurence_count.most_common(1)[0][0]}'


def func_5():
    return f'Чаще всего встречается число {(mode(array))}'


print(func_1())
print("func_1", timeit.timeit("func_1()", globals=globals(), number=1000))
print(func_2())
print("func_2", timeit.timeit("func_2()", globals=globals(), number=1000))
print(func_3())
print("func_3", timeit.timeit("func_3()", globals=globals(), number=1000))
print(func_4())
print("func_4", timeit.timeit("func_4()", globals=globals(), number=1000))
print(func_5())
print("func_5", timeit.timeit("func_5()", globals=globals(), number=1000))

"""
из 5 вариантов решения первый остается самым быстрым, следующий по скорости вариант три,
далее варианты: 2, 5, 4. НО на массивах больших размеров картина меняется и наиболее быстрым
показывает себя метод 4 и 5 сильно обгоняя другие способы. следующий по эффективности способ 3.
1 и 2 способы показывают самую низкую эффективность.
"""
