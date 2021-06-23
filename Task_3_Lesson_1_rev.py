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

comp_rep = {
    'company_1': 1000,
    'company_2': 200,
    'company_3': 3000,
    'company_4': 400,
    'company_5': 500,
    'company_6': 600
}

# вариант 1
# сложность  O(n^2)

sorted_values = sorted(comp_rep.values())                              # О(1)
sorted_dict = {}                                                       # О(1)

for i in sorted_values:                                                # O(n)
    for k in comp_rep.keys():                                          # O(n)
        if comp_rep[k] == i:                                           # О(1)
            sorted_dict[k] = comp_rep[k]                               # О(1)
            break                                                      # О(1)

sorted_list = list(sorted_dict)                                        # O(n)
print(sorted_list[-1], sorted_list[-2], sorted_list[-3])               # О(1)
print('*' * 30)                                                        # О(1)

# вариант 2
# сложность  O(n log n)

sorted_keys = sorted(comp_rep, key=comp_rep.get, reverse=True)         # O(n log n)
print(*sorted_keys[:3])                                                # О(1)
print('*' * 30)                                                        # О(1)


# вариант 3
# сложность О(n)
def three_max_profit(lst):
    set_max = {}                                                        # О(1)
    lst_dict = dict(lst)                                                # O(n)
    for i in range(3):                                                  # O(n)
        maximum = max(lst_dict.items(), key=lambda k_v: k_v[1])         # O(n)
        del lst_dict[maximum[0]]                                        # О(1)
        set_max[maximum[0]] = maximum[1]                                # О(1)
    return set_max.keys()                                               # О(1)


print(*three_max_profit(comp_rep))                                      # О(1)

# Вывод: решение 3 эффективнее, т.к. имеет минимальную сложность O(n)
# и решает задачу без изменения исходного словаря
