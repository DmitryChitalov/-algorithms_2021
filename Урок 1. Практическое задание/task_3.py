"""
Задание 3.

Для этой задачи:
1) придумайте 2-3 решения (не менее двух) разной!! сложности
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.

Задание творческое. Здесь нет жестких требований к выполнению.
"""

import heapq
from operator import itemgetter

storage = {
    'company_1': 12232200,
    'company_2': 245000,
    'company_3': 74250,
    'company_4': 24610,
    'company_5': 8443100,
    'company_6': 323500,
    'company_7': 4425700
}


def search_max_1(my_dict):  # Итого: O(n^2)
    sorted_dict = {}
    sorted_values = sorted(my_dict.values(), reverse=True)[:3]
    for i in sorted_values:
        for k in my_dict.keys():
            if my_dict[k] == i:
                sorted_dict[k] = my_dict[k]
                break
    return sorted_dict


def search_max_2(my_dict):  # Итого: O(n log n)
    sorted_tuples = sorted(my_dict.items(), key=lambda item: item[1], reverse=True)[:3]
    sorted_dict = {k: i for k, i in sorted_tuples}
    return sorted_dict


def search_max_3(my_dict):  # Итого: O(n log n)
    sorted_tuples = sorted(my_dict.items(), key=itemgetter(1), reverse=True)[:3]
    sorted_dict = {k: i for k, i in sorted_tuples}
    return sorted_dict


def search_max_4(my_dict):  # # Итого: O(n log n)
    n = 3
    sorted_tuples = heapq.nlargest(n, my_dict.items(), key=itemgetter(1))
    sorted_dict = dict(sorted_tuples)
    return sorted_dict


def search_max_5(my_dict):  # Итого: O(n^2)
    my_list = list(my_dict.items())
    for k in range(len(my_list) - 1, -1, -1):
        swapped = False
        for i in range(k):
            if my_list[i][1] < my_list[i + 1][1]:
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
                swapped = True
        if not swapped:
            break
    sorted_dict = dict(my_list[:3])
    return sorted_dict


print('Три компании с наибольшей годовой прибылью:')
print(f'Первое решение: {search_max_1(storage)}')
print(f'Второе решение: {search_max_2(storage)}')
print(f'Третье решение: {search_max_3(storage)}')
print(f'Четвертое решение: {search_max_4(storage)}')
print(f'Пятое решение: {search_max_5(storage)}')

# Первое и пятое решение считаю не эффективными, потому что они квадратичные,
# а остальные (линейно-логарифмические) считаю нормальным решением
