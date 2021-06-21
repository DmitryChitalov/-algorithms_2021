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


def profit_max1(dicts_company):
    """
    O(n)
    """
    top_profit1 = 0
    top_profit2 = 0
    top_profit3 = 0
    top_key2 = ''
    top_key1 = ''
    for key, value in dicts_company.items():
        if top_profit1 < value:
            top_key3, top_profit3 = top_key2, top_profit2
            top_key2, top_profit2 = top_key1, top_profit1
            top_key1, top_profit1 = key, value
        elif top_profit2 < value:
            top_key3, top_profit3 = top_key2, top_profit2
            top_key2, top_profit2 = key, value
        elif top_profit3 < value:
            top_key3, top_profit3 = key, value
    print(f'Лидирующие компании по дохода: \n#1 {top_key1} : {top_profit1}'
          f'\n#2 {top_key2} : {top_profit2}'
          f'\n#3 {top_key3} : {top_profit3}')






dict_company = {
    'x5': 4343434,
    'ford': 8235982,
    'apple': 121451251544,
    'microsoft': 2382058,
    'dns': 328,
}


profit_max1(dict_company)

print("\n-----------------------------------\n")











