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
# Вариант №1. Cложность: O(N*logN)
def max_3_1(in_dict):
    list_v = sorted(in_dict.items(), key=lambda i: i[1], reverse=True)[:3]  #O(N*logN)
    for company in list_v:                                                  #O(N)
            print(f'{company[0]} : {company[1]}')

# Вариант №2. Cложность: O(n)
def max_3_2(in_dict):
    top_company = {}                                                                           # O(1)
    temp_dict = dict(in_dict)                                                                  # O(1)
    for i in range(3):                                                                         # O(n)
        top = max(temp_dict.items(), key=lambda val: val[1])                                   # O(n)
        top_company[top[0]] = top[1]                                                           # O(1)
        del temp_dict[top[0]]                                                                  # O(1)
    for company, profit in top_company.items():                                                # O(n)
        print(f'{company} : {profit}')

enterprises = {
    'enterprise_1': 22,
    'enterprise_2': 305,
    'enterprise_3': 208,
    'enterprise_4': 156,
    'enterprise_5': 365
}

max_3_1(enterprises)
max_3_2(enterprises)

# Второй вариант более оптимальный, поскольку при линейной сложности время выполнения
# меньше зависит от количества данных чем у линейно-логарифмической