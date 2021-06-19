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
    result = max([(array.count(i), i) for i in set(array)])
    return f'Чаще всего встречается число {result[1]}, оно появилось в массиве {result[0]} раз(а)'


def func_4():
    dig, cnt = Counter(array).most_common(1)[0]
    return f'Чаще всего встречается число {dig}, оно появилось в массиве {cnt} раз(а)'


print(func_1())
print(func_2())
print(func_3())
print(func_4())

print('Функция func_1 -', timeit("func_1()", globals=globals(), number=100000))
print('Функция func_2 -', timeit("func_2()", globals=globals(), number=100000))
print('Функция func_3 -', timeit("func_3()", globals=globals(), number=100000))
print('Функция func_4 -', timeit("func_4()", globals=globals(), number=100000))

# придумал пару функций не самых быстрых, но лаконичнее предложенных
# самой медленной оказалась функция func_4 через класс Counter, видимо потому что наследник коллекций
# зато самый лаконичный код
# вторая по скорости и лаконичности получилась функция func_3, через list comprehension и встроенные функции
# самой быстрой осталась func_1

