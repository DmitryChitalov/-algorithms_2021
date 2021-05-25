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

companies = {
    'Toyota': 280000000,
    'Royal Dutch Shell': 311600000,
    'Exxon Mobil': 265700000,
    'Walmart': 524000000,
    'Saudi Aramco': 329800000,
    'BP': 278400000,
    'Volkswagen': 27520000,
    'ПАО ГАЗПРОМ НЕФТЬ': 23911764
}


# Вариант первый.
def company_sort_1(company_dict: dict):
    """
    Сложность: O (N log N)
    """
    result_1 = sorted(company_dict.items(), key=lambda x: x[1], reverse=True)[:3]  # O(N log N)
    return result_1     # O(1)


# Вариант второй
def company_sort_2(company_dict: dict):
    """
    Сложность: O (N log N)
    """
    companies_list = list(company_dict.items())             # O(N)
    companies_list.sort(key=lambda x: x[1], reverse=True)   # O(N log N)
    result = companies_list[:3]                             # O(N)
    return result                                           # O(1)


def company_sort_3(company_dict: dict):
    """
    Сложность: O (N), т.к. в первом цикле мы знаем кол-во выполнений - 3 раза
    """
    copied_dict = company_dict.copy()
    result = []
    for i in range(3):
        company_name = ''
        max_value = 0
        for key, value in copied_dict.items():                        # O(N)
            if value > max_value:                                     # O(1)
                company_name = key
                max_value = value
        result.append((company_name, copied_dict.pop(company_name)))  # O(N)
    return result


print(company_sort_1(companies))
print(company_sort_2(companies))
print(company_sort_3(companies))

"""
Если я не ошибся с расчетами, то выходит, что предпочитетльнее третий способ, так как его сложность меньше, 
чем у первых двух.
"""