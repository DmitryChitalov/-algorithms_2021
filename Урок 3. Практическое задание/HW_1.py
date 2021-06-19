from Time_delta import time_delta
from time import time

"""
Заполнение списка
"""


@time_delta
def list_fill_1(n, num_list=[]):  # Заполнение циклом O(1)
    for el in range(n):  # O(1)
        num_list.append(el)  # Добваление в конец O(1)
    return num_list[-1], len(num_list), 'list_fill_1'  # Проверка на правильность заполнения


# print(list_fill_1(100))  # Время выполнения: 0.0
# print(list_fill_1(10000))  # Время выполнения: 0.0

@time_delta
def list_fill_2(n, num_list=[]):  # Заполнение циклом O(n)
    for el in range(n):  # O(1)
        num_list.insert(0, el)  # Добавленние в начало O(n)
    return num_list[0], len(num_list), 'list_fill_2'


# print(list_fill_2(100))  # Время выполнения: 0.0
# print(list_fill_2(10000))  # Время выполнения: 0.02692699432373047


def list_fill_recur(n, num_list=[]):  # Заполнение рекурсией O(n!)
    if n >= 0:  # O(1)
        num_list.append(n)  # O(1)
        return list_fill_recur(n - 1)  # O(n!)
    else:
        return num_list[0], len(num_list), 'list_fill_recur'  # Проверка на заполнение


"""
Рекурсия постоянно вызываает декоратор и ломает алгоритм.
Легчайшее решение - сделать отсечки вручную
"""

# start = time()
# print(list_fill_recur(100))
# stop = time()
# print(f'Время выполнения: {stop - start}')  # Время выполнения: 0.5078815460205078
# start = time()
# print(list_fill_recur(10000))
# stop = time()
# print(f'Время выполнения: {stop - start}')  # Время выполнения: 4.4651646484641603

""" Заполнение словаря
"""


@time_delta
def dict_fill_1(n, num_dict={}):  # Заполнение циклом O(1)
    for el in range(n):
        num_dict[el] = el
    return num_dict.get(n - 1), 'dict_fill_1'


# print(dict_fill_1(100))  # Время выполнения: 0.0
# print(dict_fill_1(10000))  # Время выполнения: 0.0009953975677490234


def dict_fill_recur(n, num_dict={}):
    if n >= 0:
        num_dict[n] = n
        return dict_fill_recur(n - 1)
    else:
        return num_dict[0], 'dict_fill_recur'


start = time()
print(dict_fill_recur(100))
stop = time()
print(f'Время выполнения: {stop - start}')  # Время выполнения: 0.0
start = time()
# print(dict_fill_recur(10000))
stop = time()
print(f'Время выполнения: {stop - start}')  # Время выполнения: 7.6465432168035160


"""
ИТОГ: 
1)чем сложнее функция, тем дольше она выполняется, что доказывает правильно определенно Онотацию
2)словарь наполняется немного дольше списка при использовании одинакового метода наполнения
"""
