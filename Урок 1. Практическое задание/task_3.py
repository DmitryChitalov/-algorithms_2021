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


def get_key(d, value):
    for k, v in d.items():  # O(n)
        if v == value:  # O(n)
            return k  # O(1)


companies = {"Сбербанк": 13060,
             "Saudi Aramco": 88211,
             "Merck": 9843,
             "Роснефть": 10944,
             "Газпром": 18593,
             "Alphabet": 34343}  # O(len(...))

# Вариант 1
list_of_companies = list(dict.values(companies))  # O(len(...))
list_of_companies.sort()  # O(nlogn)
print(get_key(companies, list_of_companies[-1]), list_of_companies[-1])  # O(1)
print(get_key(companies, list_of_companies[-2]), list_of_companies[-2])  # O(1)
print(get_key(companies, list_of_companies[-3]), list_of_companies[-3])  # O(1)

# Вариант 2
companies_copy = companies.copy()  # O(1)
first_profit = max(companies_copy, key=companies_copy.get)
print(get_key(companies_copy, companies_copy.get(first_profit)), companies_copy.get(first_profit))  # O(1)
del companies_copy[first_profit]  # O(1)
second_profit = max(companies_copy, key=companies_copy.get)
print(get_key(companies_copy, companies_copy.get(second_profit)), companies_copy.get(second_profit))
del companies_copy[second_profit]  # O(1)
third_profit = max(companies_copy, key=companies_copy.get)
print(get_key(companies_copy, companies_copy.get(third_profit)), companies_copy.get(third_profit))  # O(1)

"""
Вариант 1 кажется наиболее эффектиным, так как имеет меньше строк решения, однако 2 из них имеют сложность O(len(...)) 
и O(nlogn), которые имеют большое влияние на скорость выполнения операций. Вариант 2, хоть и состоит из большего числа
операций, является боллее эффективным, так как большинство операций имеют сложность O(1), что позволяет вывести 
результат быстрее
"""
