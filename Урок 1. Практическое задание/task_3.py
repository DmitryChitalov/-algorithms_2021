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
company = {
    'BMW': 567,
    'AUDI': 40,
    'W_group': 987,
    'Ford': -79,
    'VAZ': 38,
    'Tesla': 500
    }                                                                 # O(1)

# Общая # O(N log N)
sorted_dict = {}                                                      # O(1)
sorted_keys_2 = sorted(company, key=company.get, reverse=True)[:3]    # O(N log N)
for w in sorted_keys_2:                                               # O(N)
    sorted_dict[w] = company[w]                                       # O(1)
print(sorted_dict)


company2 = {
    'Sber': 1567,
    'VTB': 40,
    'Rosbank': 87,
    'Tinkoff': 790
    }                                                     # O(1)

# Общая O(n**3)
sort_list_values = []                                     # O(1)
for i in range(len(company2.values())):                   # O(n)
    maximum = 0                                           # O(1)
    for s in company2.values():                           # O(n)
        if s > maximum and s not in sort_list_values:     # O(n)
            maximum = s                                   # O(1)
    sort_list_values.append(maximum)                      # O(1)

sorted_name_2 = {}                                        # O(1)
for i in sort_list_values[:3]:                            # O(n)
    for j in company2.keys():                             # O(n)
        if company2[j] == i:                              # O(1)
            sorted_name_2[j] = company2[j]                # O(1)
print(sorted_name_2)                                      # O(n)

"""
Первый алгоритм лучше т.к. линейно-логарифмический быстрее кубического
"""