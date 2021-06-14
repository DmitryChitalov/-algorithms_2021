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


def best_company_1(my_dict):                                    # 9 + (n log n) + 3 + 1 = O(n log n)
    list_from_company = list(my_dict.items())                   # O(len(dict)) = 9
    list_from_company.sort(key=lambda x: x[1], reverse=True)    # O(n log n)
    for i in range(3):                                          # O(3)
        print(f'{i + 1} company is "{list_from_company[i][0]}" with profit = {list_from_company[i][1]}')  # O(1)


def best_company_2(my_dict):                   # 9 + 3 + 1 + n^2 = O(n^2)
    list_from_company = list(my_dict.items())  # O(len(dict)) = 9
    for i in range(3):                         # O(3)
        print(f'{i + 1} company is '           # O(1 + n * n)
              f'{list_from_company.pop(list_from_company.index(max(list_from_company, key=lambda val: val[1])))}')


def best_company_3(my_dict):                     # 9 + 1 + 3 + 1 + n^2 + 1 = O(n^2) просто с более красивым выводом
    list_from_company = list(my_dict.items())    # O(len(dict)) = 9
    list_of_top_companies = []                   # O(1)
    for i in range(3):                           # O(3)
        list_of_top_companies.append\
                (list_from_company.pop(
                    list_from_company.index(max(list_from_company, key=lambda val: val[1]))))     # O(1 + n * n)
        print(f'{i + 1} company is "{list_of_top_companies[i][0]}" with profit = {list_of_top_companies[i][1]}')  # O(1)


companies = {
    'alpha ': 3000,
    'bravo': 300,
    'charlie': 6000,
    'delta': 2550,
    'echo': 4385,
    'foxtrot': 99,
    'golf': 75,
    'hotel': 5937,
    'india': 6418
}

best_company_1(companies)
best_company_2(companies)
best_company_3(companies)

"""
Наиболее эффективным решением задачи является функция best_company_1, т.к.асимптотическая сложность 
для данного решения равняется O(n log n). Решения 2 и 3 использовать не рекомендуется 
из-за их высокой асимпотической сложности.
"""