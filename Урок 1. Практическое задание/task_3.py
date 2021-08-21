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

def three_best_company_1(company):
    """
    Решение 1
    Сложность: O(N log N)
    """
    three_best_company = []
    list_company = list(sorted(company.items(), key=lambda i: (i[1], i[0]), reverse=True)) #O(NlogN)
    for key in list_company:  # O(N)
        three_best_company.append(key[0])  # O(1)
    return three_best_company[:3]  # O(1)


def three_best_company_2(company):
    """
    Решение 2
    Сложность: O(N^2)
    """
    best_company = ""  # O(1)
    three_best_company = []  # O(1)
    for i in range(3):  # O(1)
        max_value = 0  # O(1)
        for key, value in company.items():  # O(N^2)
            if value > max_value and key not in three_best_company:  # O(N)
                max_value = value  # O(1)
                best_company = key  # O(1)
        three_best_company.append(best_company)  # O(1)
    return three_best_company  # O(1)


company = {'company_1': 123456,
           'company_2': 234567,
           'company_3': 345678,
           'company_4': 132645,
           'company_5': 213453,
           'company_6': 324132
           }

print(three_best_company_1(company))
print(three_best_company_2(company))
"""
Решение 2 эффективние, так как его сложность меньше чем в решение 1. Хотя визульно и кажется,
что решение 1 эффективние так как оно реализуется за меньшее кол-во строк кода.
"""
