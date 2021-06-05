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
from collections import Counter
from numpy import bincount

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
    return Counter(array).most_common(1)[0][1]


def func_4():
    elems = {}
    for elem in array:
        elems[elem] = elems.get(elem, 0) + 1
    return elems


def func_5():
    return bincount(array).argmax()


def func_6():
    return max(array, key=array.count)


print(f'func_1(): {timeit("func_1()", globals=globals(), number=1000)}')
print(f'func_2(): {timeit("func_2()", globals=globals(), number=1000)}')
print(f'func_3(): {timeit("func_3()", globals=globals(), number=1000)}')
print(f'func_4(): {timeit("func_4()", globals=globals(), number=1000)}')
print(f'func_5(): {timeit("func_5()", globals=globals(), number=1000)}')
print(f'func_6(): {timeit("func_5()", globals=globals(), number=1000)}')

"""
func_1(): 0.0012367999999999824
func_2(): 0.0016064000000000078
func_3(): 0.0028065999999999924 - Collections
func_4(): 0.0007514000000000132 - словарь
func_5(): 0.0018859999999999988 - NumPy
func_6(): 0.0016964999999999897 - Max()
Самым быстрым решением оказалась реализация через словарь, близко к оригиналу располагается Max().
В словаре большинство опираций выполняется за константную сложность, встроенная же функция Max() 
сама по себе работает очень быстро.
"""
