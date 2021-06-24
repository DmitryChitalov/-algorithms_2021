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


print(func_1())
print(func_2())

def func_3():
    freq_el = array[([array.count(el) for el in array]).index(max([array.count(el) for el in array]))]
    return f'Чаще всего встречается число {freq_el}, оно появилось в массиве {array.count(freq_el)} раз(а)'

print(func_3())

def func_4():
    m = max(list(map((lambda el: array.count(el)), array)))
    for el in array:
        if array.count(el) == m:
            return f'Чаще всего встречается число {el}, оно появилось в массиве {m} раз(а)'


print(func_4())

print(timeit("func_1()", setup="from __main__ import func_1", number=1000000))
print(timeit("func_2()", setup="from __main__ import func_2", number=1000000))
print(timeit("func_3()", setup="from __main__ import func_3", number=1000000))
print(timeit("func_4()", setup="from __main__ import func_4", number=1000000))

# вариант 3 получился "провальным" - он дольше остальных значительно, поочти вдвое
# дольше первого варианта,  из-за использования затратного метода index, 2-х кратного
# использования list comprehension, max, count - все в одной строке.
# вариант 4 чуть лучше, но также далек от идеала из-за использования таих встроенных функций и методов,
# как max, list, map, lambda.
# Таким образом, оптимизация мне не удалась: желание написать сложный код в минимальное колчнство строк
# дал противоположные результаты для времени выполнения кода из-за использования вложенных
# одни в другие методов и функций, что привело к худшим вариантам доминирующей сложности