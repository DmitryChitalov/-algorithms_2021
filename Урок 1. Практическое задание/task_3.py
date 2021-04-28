from random import randint
from operator import itemgetter

"""
Задание 3.

Для этой задачи:
1) придумайте 2-3 решения (не менее двух)
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


# Способ 1

def max_values(dict_obj):  # O(n)
    dict_key = ''  # O(1)
    dict_value = 0  # O(1)
    for key, value in dict_obj.items():  # O(n)
        if value > dict_value:  # O(1)
            dict_key = key  # O(1)
            dict_value = value  # O(1)
    return dict_key, dict_value  # O(1)


def search_leaders(dict_obj):  # O(n)
    company = {}  # O(1)
    for i in range(3):  # O(n)
        key, value = max_values(dict_obj)  # O(n)
        company[key] = value  # O(1)
        dict_obj.pop(key)  # O(1)
    return company  # O(1)


company_arrived = {f'Company_{elem}': randint(100, 5000) for elem in range(10)}  # O(n)

# company_arrived = {'Samsung': 10000,
#                   'Apple': 20002,  # 2 место
#                   'Sony': 30000,  # 1 место
#                   'DEXP': 1000,
#                   'Huawei': 10001}  # 3 место


# print(search_leaders(company_arrived))

# Способ 2
leaders = sorted(company_arrived.items(), key=itemgetter(1))[-3:][::-1]  # O(Не могу оценить)
# (Отсортировал, сделал срез, зареверсил)

# print(f'{company_arrived}\n\n'
#       f'{search_leaders(company_arrived)}')  # O(n)
print(leaders)

#   Не могу точно сказать какой эфективнее по пречине того, что не знаю О(Способ 2),
# но как мне кажется Способ 2 так, как там используется полько сортирова, срез и перебор в обр. сторону.
