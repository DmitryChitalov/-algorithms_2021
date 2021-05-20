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
from typing import List

companies = {"Сбербанк": 13060,
             "Saudi Aramco": 88211,
             "Merck": 9843,
             "Роснефть": 10944,
             "Газпром": 18593,
             "Alphabet": 34343}  # O(len(...))


# Вариант 1

def top_three_best_1(companies_dict):

    for el in range(len(companies_dict)):
        lowest_value_index = el
        for subel in range(el + 1, len(companies_dict)):
            if companies_dict[subel][1] > companies_dict[lowest_value_index][1]:
                lowest_value_index = subel
        companies_dict[el], companies_dict[lowest_value_index] = companies_dict[lowest_value_index], companies_dict[el]
    return companies_dict[:3]


top_three_companies = list(companies.items())
for i in top_three_best_1(top_three_companies):
    print(f"Фирма {i[0]} имеет прибыль ${i[1]} мллд.")

"""
Общая сложность решения - O(n^2), так как один цикл сложностью O(n) вложен в другой 
цикл сложностью O(n), а остальные строки решения имеют константную сложность.
"""

# Вариант 2


def top_three_best_2(companies_dict_2):
    top_company = {}

    for el in range(3):
        max_value = max(companies_dict_2.items(), key=lambda k_v: k_v[1])
        del companies_dict_2[max_value[0]]
        top_company[max_value[0]] = max_value[1]
    return top_company


print(top_three_best_2(companies))

"""
Общая сложность решения - O(n)
"""

# Вариант 3


def get_key(d, value):
    for k, v in d.items():  # O(n)
        if v == value:  # O(n)
            return k  # O(1)


companies_copy = companies.copy()  # O(1)
first_profit = max(companies_copy, key=companies_copy.get)
print(get_key(companies_copy, companies_copy.get(first_profit)), companies_copy.get(first_profit))  # O(1)
del companies_copy[first_profit]  # O(1)
second_profit = max(companies_copy, key=companies_copy.get)
print(get_key(companies_copy, companies_copy.get(second_profit)), companies_copy.get(second_profit))  # O(1)
del companies_copy[second_profit]  # O(1)
third_profit = max(companies_copy, key=companies_copy.get)
print(get_key(companies_copy, companies_copy.get(third_profit)), companies_copy.get(third_profit))  # O(1)

"""
Общая сложность решения - O(n). Таким образом, второе и третье решения являются более эффективными, так как имеют
наименьшую сложность.
"""
