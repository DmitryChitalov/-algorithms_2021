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

company1 = {'first' : 100}
company2 = {'second' : 400}
company3 = {'third' : 200}
company4 = {'fourth' : 1050}
all_company = [company1,company2,company3,company4]


"""Pешение"""        # T = 1 + 1 + 1n**2 + nLogn + 1 + 1n**3 + 1 =      O(n**3)
"""Это решение мне кажется менее эфективным поскольку: O(n**2) < O(n**3)"""

# max_income = []                         #O(1)
# income = []                             #O(1)
#
# for i in all_company:                   # O(n)
#     for key, values in i.items():           # O(n)
#         income.append(values)                   # O(1)
# income.sort(reverse=True)               #O(nLogn)
# income = income[0:3]                    # O(1)
#
# for i in all_company:                   # O(n)
#     for key, values in i.items():           # O(n)
#         if values in income:                    # O(n)
#             max_income.append(i)        # O(1)
# print(max_income)                       # O(1)


"""Pешение"""       # T = 1 + 1 + 1 + 1n**2 + 3n**2 + 2n + 1 =      O(n**2)
"""Это решение мне кажется эфективнее поскольку: O(n**2) < O(n**3)"""
max_income = []                                #O(1)
max_val = []                                   #O(1)
income = []                                    #O(1)


for i in all_company:                          #O(n)
    for key,values in i.items():                    #O(n)
        income.append(values)                            #O(1)

for i in range(3):                             #O(n)
    max_value = max(income)                         #O(n)
    max_val.append(income.index(max_value))         #O(1) + O(n)
    income[income.index(max_value)] = 0             #O(n)

for i in max_val:                              #O(n)
    max_income.append(all_company[i])               #O(1) + O(1)
print(max_income)                              #O(1)



