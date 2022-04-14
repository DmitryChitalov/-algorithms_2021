"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой и по возможности самой лаконичной.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.

Без аналитики задание считается не принятым!
"""
from collections import Counter, OrderedDict
from timeit import timeit

array = [1, 3, 1, 3, 4, 5, 1]


def func_1():  # 0.019444599999999996
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():  # 0.019044600000000002
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def func_3():  # Тут очевидно, на уроке говорилось о этой функции   0.0194137
    my_dict = Counter(array)
    mnum = max(array, key=my_dict.get)
    return f'Чаще всего встречается число {mnum}, ' \
           f'оно появилось в массиве {my_dict.get(mnum)} раз(а)'


def func_4():  # сгруппируем одинаковые элементы 0.01602780000000001
    m = [[n] * array.count(n) for i, n in enumerate(array) if array.index(n) == i]
    return f'Чаще всего встречается число {m[0][0]}, ' \
           f'оно появилось в массиве {len(m[0])} раз(а)'


def func_5():  # Улучшаем (3) 0.0161631
    return f'Чаще всего встречается число {Counter(array).most_common()[0][0]}, ' \
           f'оно появилось в массиве {Counter(array).most_common()[0][1]} раз(а)'


def func_6():  # ну и словарь, понятное дело 0.01700270000000001
    my_dict = {i: array.count(i) for i in array}
    m_num = max(my_dict, key=my_dict.get)
    return f'Чаще всего встречается число {m_num}, ' \
           f'оно появилось в массиве {my_dict[m_num]} раз(а)'


class OrdCount(Counter, OrderedDict):  # Попробуем ООП, суть та же, что в(4) просто интересно
    pass


def take_most(array):  # 5.4411231
    m_num = [[k] * v for k, v in OrdCount(array).items()]
    return f'Чаще всего встречается число {m_num[0][0]}, ' \
           f'оно появилось в массиве {len(m_num[0])} раз(а)'


# Итого, самым быстрым стал вариант (5). но и результаты (4), (6) - на том же примерно уровне. Это можно легко
# объяснить, функция Counter уже была оптимизирована разработчниками, а в (4) мы использовали быстрый lc + встроенный
# enumerate. Словарь - отрабатывает быстро, потому что там lc + значение по ключу, которое мы получаем с константной
# сложностью. Наиболее медленный в конкретной ситуации вариант с ООП, за счет создания экземпляра класса и обращений
# к нему
if __name__ == '__main__':
    print(func_1())
    print(timeit('func_1', globals=globals()))
    print('##################################################################')
    print(func_2())
    print(timeit('func_2', globals=globals()))
    print('##################################################################')
    print(func_3())
    print(timeit('func_3', globals=globals()))
    print('##################################################################')
    print(func_4())
    print(timeit('func_4', globals=globals()))
    print('##################################################################')
    print(func_5())
    print(timeit('func_5', globals=globals()))
    print('##################################################################')
    print(func_6())
    print(timeit('func_6', globals=globals()))
    print('##################################################################')
    print(take_most(array))
    print(timeit('take_most(array)', globals=globals()))
    print('##################################################################')
