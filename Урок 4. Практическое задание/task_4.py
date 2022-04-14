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
from timeit import timeit

array = [1, 3, 1, 3, 4, 5, 1, 3, 3]


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


def func_counter():
    cnt = Counter(array).most_common(1)
    return f'Чаще всего встречается число {cnt[0][0]}, оно появилось в ' \
           f'массиве {cnt[0][1]} раз(а)'


def func_max_key():
    num = max(array, key=lambda i: array.count(i))
    return f'Чаще всего встречается число {num}'


print(func_1())
print('время выполнения функции func_1', timeit('func_1()', globals=globals(),
                                                number=100000))
print(func_2())
print('время выполнения функции func_2', timeit('func_2()', globals=globals(),
                                                number=100000))
print(func_counter())
print('время выполнения функции func_counter', timeit('func_counter()',
                                                      globals=globals(),
                                                      number=100000))
print(func_max_key())
print('время выполнения функции func_max_key', timeit('func_max_key()',
                                                      globals=globals(),
                                                      number=100000))

'''
1. Замеры показали, что самая быстрая функция это перебор циклом for с поиском
наибольшего числа вхождений (.count).Время - 0.15315789999999999.
2. Вторая функция (перебор элементов, заполнение списка и поиск наибольшего 
числа вхождений по индексу через функцию max оказалась медленнее первой, 
(причина - много действий), но быстрее предложенных collections.Counter и 
max (с key).
3. Функция max с key повела себя чуть медленнее, чем вторая функция.
4. Использование collections.Counter показало самый медленный результат.
Вывод: Предложить более эффективную функцию не удалось. 
'''
