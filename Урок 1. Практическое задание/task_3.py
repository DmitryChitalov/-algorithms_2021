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


def top_3_comp_var1(companies):
    # Сложность O(NlogN)

    top_companies = [(key, value) for key, value in companies.items()]  # O(N)
    top_companies.sort(key=lambda value: value[1], reverse=True)  # O(N log N)

    return top_companies[:3]


def top_3_comp_var2(companies):
    # Сложность O(N**2)

    profit = [value for value in companies.values()]  # O(N)

    profit.sort()  # O(NlogN)
    max_profit = profit[-3:]  # O(1)

    top_companies = []  # O(1)
    for name, value in companies.items():  # O(N)
        if value in max_profit:  # O(N)
            top_companies.append(name)  # O(1)

    return top_companies  # O(1)


companies_to_sort = {
    "SomeCompany1": 3453467,
    'SomeCompany2': 435567,
    'SomeCompany3': 44568,
    'SomeCompany4': 34545798,
    'SomeCompany5': 5675
}

print(top_3_comp_var1(companies_to_sort))
print(top_3_comp_var2(companies_to_sort))
