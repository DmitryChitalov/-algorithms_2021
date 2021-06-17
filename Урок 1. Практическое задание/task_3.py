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
from operator import itemgetter


# Решение № 1
def get_max_profit_1(company_lst):
    """
    Общая сложность: O(n log n)
    """
    return sorted(company_lst, key=itemgetter('profit'), reverse=True)[:3]


# Решение № 2
def get_max_profit_2(company_lst):
    """
    Общая сложность: O(n^2)
    """
    copy_company_lst = list(company_lst)                                                                 # O(n)
    for i in range(0, len(copy_company_lst) - 1):                                                        # O(n)
        for j in range(i + 1, len(copy_company_lst)):                                                    # O(n)
            if copy_company_lst[j]['profit'] > copy_company_lst[i]['profit']:                            # O(1)
                copy_company_lst[i], copy_company_lst[j] = copy_company_lst[j], copy_company_lst[i]      # O(1)
    return [i.get('company_name') for i in copy_company_lst[:3]]                                         # O(1)


# Проверка работы ф-ций
company_profits = [
    {'company_name': 'Apple', 'profit': 55.26},
    {'company_name': 'Looker', 'profit': 25.1},
    {'company_name': 'Adore', 'profit': 2.44},
    {'company_name': 'Bobble', 'profit': 16.2},
    {'company_name': 'Frozen', 'profit': 32.41},
    {'company_name': 'Legacy', 'profit': 15.1}
]
print(get_max_profit_2(company_profits))

"""
Первый способ эффективнее, поскольку алгоритм со сложностью O(n log n) 
отработает быстрее алгоритма со сложностью O(n^2) 
"""
