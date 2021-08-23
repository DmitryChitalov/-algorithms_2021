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
    'Walmart': 14.2,
    'Sinopec Group': 5.8,
    'State Grid Corporation of China': 8.1,
    'China National Petroleum': 2.2,
    'Royal Dutch Shell': 15.8,
    'Saudi Aramco': 11.8,
    'Volkswagen': 14.0,
    'BP': 9.3,
    'Amazon': 11.5,
    'Toyota': 19.5
}  # billion $


def max_profit_1(some_company):  # O(n^2)
    top_three = {}
    sort_dict = sorted(some_company.values())
    for i in sort_dict:
        for j in some_company.keys():
            if some_company[j] == i:
                top_three[j] = some_company[j]
    return list(reversed(top_three.items()))[0:3]


def max_profit_2(some_company):  # O(n log n)
    sort_dict = sorted(some_company.items(), key=lambda j: j[1], reverse=True)
    return sort_dict[0:3]


print(max_profit_1(company))
print(max_profit_2(company))

"""
Вывод: второе решение эффективнее т.к имеет меньшую сложность
и более локанично.
"""
