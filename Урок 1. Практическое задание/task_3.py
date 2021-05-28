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


from copy import copy


def top_company(dict_obj):  # O(N)
    dict_top_company = {}
    for n in range(3):
        max_value = 0
        max_subj = ''
        for i in dict_obj:
            if dict_obj[i] > max_value:
                max_value = dict_obj[i]
                max_subj = i
        dict_top_company[max_subj] = dict_obj.pop(max_subj)
    return dict_top_company


def top_company_2(dict_obj):  # O(N)
    dict_top_company = {}
    for _ in range(3):
        temp = [key for key, value in dict_obj.items() if value == max(dict_obj.values())][0]
        dict_top_company[temp] = dict_obj.pop(temp)
    return dict_top_company


Dict_Company = {'a': 100, 'b': 150, 'c': 90, 'd': 120, 'e': 80, 'f': 146}
print(f'Топ 3 компании v.1 - {top_company(copy(Dict_Company))}')
print(f'Топ 3 компании v.2 - {top_company_2(copy(Dict_Company))}')

# Лучшим решением является второй вариант так как он более аккуратно составлен (не такой большой)
