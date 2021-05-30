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
firms_profit = {'Mountain guide': 30000,
                'Ice axe': 150000,
                'Climbing group': 70000,
                'Climbing technology': 45000,
                'Tourist advice': 200000,
                'Hypoxia and stew': 70000}

#Вариант 1
#Сложность O(n^2)
def top_profit_seeker_1(firms):
    top_firms = {}
    sorted_firm_value = sorted(firms.values(), reverse=True) #O(n Log n)

    for i in sorted_firm_value[0:3]: #O(n) + O(n)
        for k in firms.keys(): #O(n) + O(1)
            if firms[k] == i: #O(1)
                top_firms[k] = firms[k] #O(1)

    return top_firms #O(1)

print(top_profit_seeker_1(firms_profit))

#Вариант 2
#Сложность O(n)
def top_profit_seeker_2(firms):
    top_firms = {}
    firms_name = sorted(firms, key=firms.get, reverse=True) #O(n)

    for i in firms_name[0:3]: #O(n) + O(n)
        top_firms[i] = firms[i] #O(1)

    return top_firms #O(1)

print(top_profit_seeker_2(firms_profit))

#Общий вывод:
#Решение №2 лучше, так как:
#Меньшая алгоритимическая сложность
#Более короткое и читаемое решение