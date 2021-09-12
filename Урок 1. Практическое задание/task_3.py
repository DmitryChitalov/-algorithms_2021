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

companies = {
    'Samsung Electronics': 221579,
    'China National Petroleum': 364100,
    'UnitedHealth Group': 226247,
    'Saudi Aramco': 329800,
    'Volkswagen': 275200,
    'Amazon.com': 232887,
    'Royal Dutch Shell': 311600,
    'Toyota': 280500,
    'BP': 278400,
    'Walmart': 524000,
    'Sinopec Group': 369200,
    'Exxon Mobil': 265700,
    'Apple': 265595,
    'State Grid': 387000,
    'Berkshire Hathaway': 247837}


# O(n log n)
def top_companies_sort(dict):
    lst = []                            # O(1)
    dict2 = {}                          # O(1)
    for key, value in dict.items():     # O(n)
        lst.append(value)               # O(1)
    lst2 = sorted(lst)                  # O(n log n)
    for key, value in dict.items():     # O(n)
        if value in lst2[-3:]:          # O(n)
            dict2[key] = value          # O(1)
    return dict2                        # O(1)


# Та же самая процедура, только метод sorted() заменен на max, как следствие процедура стала работать быстрее,
# а значит эффективнее.
# O(n)
def top_companies_max(dict):
    lst = []                            # O(1)
    dict2 = {}                          # O(1)
    for key, value in dict.items():     # O(n)
        lst.append(value)               # O(1)
    for _ in range(3):                  # O(1)
        lst.remove(max(lst))            # O(n)
    for key, value in dict.items():     # O(n)
        if value not in lst:            # O(n)
            dict2[key] = value          # O(1)
    return dict2                        # O(1)


print(top_companies_sort(companies))
print(top_companies_max(companies))
