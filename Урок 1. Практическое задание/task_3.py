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


def find_max_earning_1(my_companies):
    """
    Сложность: O(N).
    Эффективно, так как используется только один проход по словарю
    """
    max_earning = None  # O(1)
    company_name = None  # O(1)
    for item, value in my_companies.items():  # O(N)
        if max_earning is None:  # O(1)
            max_earning = value  # O(1)
            company_name = item  # O(1)
        if value > max_earning:  # O(1)
            max_earning = value  # O(1)
            company_name = item  # O(1)
    return company_name, max_earning  # O(1)


def find_max_earning_2(my_companies):
    """
    Сложность: O(N^2).
    Неэффективно, так как pop в отличие от списка занимает O(N)
    """
    max_earning = None  # O(1)
    company_name = None  # O(1)
    for _ in range(len(my_companies)):  # O(N)
        item = my_companies.pop()  # O(N)
        if max_earning is None or item[1] > max_earning:  # O(1)
            max_earning = item[1]  # O(1)
            company_name = item[0]  # O(1)
    return company_name, max_earning  # O(1)


companies = {'company 1': 100, 'company 2': 10000, 'company 3': -100000, 'company 4': 100}
print(find_max_earning_1(companies))
companies = [['company 1', 100], ['company 2', 10000], ['company 3', -100000], ['company 4', 100]]
print(find_max_earning_2(companies))
