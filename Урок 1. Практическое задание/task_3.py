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

def top3_1(dict_comp_profit):
    # Сложность: O(n^2).
    lst_profit = list(dict_comp_profit.values())                    # O(n)
    lst_profit.sort(reverse=True)                                   # O(n log n)
    dict_comp_profit_sort = dict()                                  # O(1)
    for i in lst_profit:                                            # O(n)
        for k in dict_comp_profit.keys():                           # O(n)
            if dict_comp_profit[k] == i:                            # O(1)
                dict_comp_profit_sort[k] = dict_comp_profit[k]      # O(1)
    j = 0                                                           # O(1)
    for k, v in dict_comp_profit_sort.items():                      # O(n)
        print(k, v)                                                 # O(1)
        j += 1                                                      # O(1)
        if j == 3:                                                  # O(1)
            break


def top3_2(dict_comp_profit):
    # Сложность: O(n^2).
    profits = list(dict_comp_profit.values())   # O(n)
    max_profit = profits[0]                     # O(1)
    top3 = [max_profit]                         # O(1)
    for i in range(3):                          # O(1)
        for val in profits:                     # O(n)
            if val > max_profit:                # O(1)
                top3.remove(max_profit)         # O(1)
                max_profit = val                # O(1)
                top3.append(max_profit)         # O(1)
        if len(top3) < 3:                       # O(1)
            profits.remove(max_profit)          # O(n)
            max_profit = profits[0]             # O(1)
            top3.append(max_profit)             # O(1)

    for profit in top3:                         # O(1)
        for k, v in dict_comp_profit.items():   # O(n)
            if profit == v:                     # O(1)
                print(k, v)                     # O(1)


'''Второе решение эффективнее, не смотря на схожую сложность, ввиду большинства действий с константной сложностью.'''

annual_profit = {"VAZ": 2000,
                 "GAZ": 1500,
                 "UAZ": 1400,
                 "BMW": 4000,
                 "Opel": 1600,
                 "Audi": 2900
                 }

top3_1(annual_profit)
print('#########')
top3_2(annual_profit)
