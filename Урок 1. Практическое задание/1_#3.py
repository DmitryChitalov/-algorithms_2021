import time

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

company = {
    'Walmart': 524000000, 'BP': 278400000,
    'State Grid': 387000000, 'Volkswagen': 275200000,
    'Sinopec Group': 369000000, 'Apple': 265595000,
    'Toyota': 280500000, 'Lukoil': 119145000
}


# 1 вариант
# сложность логорифмическая O(n log n)


def key_func(item):
    return item[1]  # O(1)


best_companies = {}  # O(1)
i = 0  # O(1)
for k, v in sorted(company.items(), key=key_func, reverse=True):  # O(n + n log n)
    if i < 3:  # O(len(i)
        best_companies.setdefault(k, v)  # O(1)
    i += 1  # O(1)

print(best_companies)  # O(1)

# 2 вариант
# Сложность квадратичная O (n**2)

global max_value  # O(1)
global key_max_value  # O(1)

best_companies_2 = {}  # O(1)
while len(best_companies_2) < 3:  # O(n)
    max_value = 0  # O(1)
    for key, value in company.items():  # O(n)
        if max_value < value:  # O(len(max_value))
            max_value = value  # O(1)
            key_max_value = key  # O(1)
    max_value = company.pop(key_max_value)  # O(1)
    best_companies_2.setdefault(key_max_value, max_value)  # O(1)

print(best_companies_2)  # O(1)

# Вывод: эффективнее будет 1 вариант, т.к. функция выполнятся быстрее
# благодаря функции sorted() логорифмической сложности O(n log n)
