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

company_list = {'Рога и Копыта': 1000000, 'Тру.Бо.О.Ж.О.П': 50000000, 'Шарашкина контора': 24443425, 'МММ': 76646879,
                'Братва и кольцо': 47858976, 'SpaceX': 999999999}
#############################################################################################
"""
Вариант 1
Сложность O(n^2)
"""

sorted_values = sorted(company_list.values(), reverse=True)
sorted_dict = {}

for i in sorted_values:
    for k in company_list.keys():
        if company_list[k] == i:
            sorted_dict[k] = company_list[k]
            break
k = 3
for name,profit in sorted_dict.items():
    print(f"{name} {profit}$")
    k -= 1
    if k == 0:
        break


#############################################################################################
"""
Вариант 2
Сложность O(n)
"""

import operator

top_companies_list = company_list.copy()
k = 3
while k > 0:
    name = max(top_companies_list.items(), key=operator.itemgetter(1))[0]
    profit = top_companies_list.pop(name)
    print(f'{name} {profit}')
    k -= 1
