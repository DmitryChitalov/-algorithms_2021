﻿"""
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

def top3_1(my_dict):							# O(N^2)
    my_list = {}
    for i in range (3):
        max_el = 0
        max_company = ""
        for j in my_dict:
          if my_dict.get(j) > max_el:
             max_el = my_dict.get(j)
             max_company = j
        my_list[max_company] = my_dict.pop(max_company)
    return my_list

def top3_2(my_dict):                            # O(N*logN)
    my_list = list(my_dict.items())
    my_list.sort(key=lambda i: i[1], reverse=True)
    return my_list[:3]

companies = {"Microsoft": 1000000, "Apple": 2000000, "Газпром": 150000000, "Amazon": 300, "Роснефть": 4000000000, "Рога и копыта": 15000000000}
print(top3_1(companies))

companies = {"Microsoft": 1000000, "Apple": 2000000, "Газпром": 150000000, "Amazon": 300, "Роснефть": 4000000000, "Рога и копыта": 15000000000}
print(top3_2(companies))

# Первое решение имеет сложность О(N^2), т.к. применяется 2 вложенных цикла
# Второе решение имеет сложность O(N*logN), т.к. использует функцию sort
# Второе решение более эффективное, т.к. алгоритм с линейно-логарифмической сложностью быстрее, чем алгоритм с квадратичной сложностью