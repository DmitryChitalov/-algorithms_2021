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

# Сложность квадратичная O(n^2)
def max_profit_1(cmp_pr):
    profit = {}                                             # O(1) - константная
    for i in range(3):                                      # O(1) - константная
        max_val = 0                                         # O(1) - константная
        for k, v in cmp_pr.items():                         # O(n) - линейная
            if (v > max_val) and (k not in profit.keys()):  # O(n) - линейная
                max_val = v                                 # O(1) - константная
                key = k                                     # O(1) - константная
        profit[key] = max_val                               # O(1) - константная
    return profit                                           # O(1) - константная

# Сложность линейная O(n)
def max_profit_2(cmp_pr):
    cmp_pr = cmp_pr.copy()                                  # O(1) - константная
    profit = {}                                             # O(1) - константная
    for i in range(3):                                      # O(1) - константная
        max_val = 0                                         # O(1) - константная
        for k, v in cmp_pr.items():                         # O(n) - константная
            if v > max_val:                                 # O(1) - константная
                max_val = v                                 # O(1) - константная
                key = k                                     # O(1) - константная
        profit[key] = max_val                               # O(1) - константная
        cmp_pr.pop(key)                                     # O(1) - константная
    return profit                                           # O(1) - константная

company_profit = {'York Jonk Pola': 4.6, 'Carbon Mailedle Ale': 2.7, 'Blue Spot':8.3, 'Reieck Mechanical': 6.5,
                  'Suso Scientific': 2.7, 'Texent': 1.2, 'White Star Appliance': 3.3, 'Parekh Industries': 7.1,
                  'Ancplus': 5.2, 'Fosters Technology': 3.8, 'Onsite Glassworks': 4.9, 'Fastec': 5.2,
                  'Chippe Engineers': 4.9, 'Synergy Analytik':2.1, 'Asap': 7.4, 'Servpro Of Minneapolis': 3.4,
                  'Gas Valve Welding': 3.3, 'Malota Metal': 7.2, 'Avocado Technology': 4.9, 'Tech Tools':2.3}

print(max_profit_1(company_profit))
print(max_profit_2(company_profit))

# сделайте вывод, какое решение эффективнее и почему
'''
Решение max_profit_2 эффективнее чем max_profit_1, потому что сложность решения max_profit_2 - линейная O(n),
а max_profit_1 - квадратичная O(n^2). Время выполнения функции с линейной сложностью меньше, чем с квадратичной. 
'''
