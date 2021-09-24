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

base_company = {
    'Romashka': 100000,
    'Astra': 150000,
    'Rose': 125000,
    'Pion': -10000,
    'Tulpan': 300000,
    'Сhrysanthemum': 600000
}


def profit_of_three(base_com):  # O(N**2)
    lst_profit = [i for i in base_com.values()]  # O(N)
    n = len(lst_profit) - 1  # O(N) --> O(1)
    for i in lst_profit:  # O(N)
        for j in range(0, n):  # O(N**2) --> O(N), записал итог работы 2х циклов
            if lst_profit[j] > lst_profit[j + 1]:  # O(1)
                temp = lst_profit[j]  # O(1)
                lst_profit[j] = lst_profit[j + 1]  # O(1)
                lst_profit[j + 1] = temp  # O(1)
        n -= 1  # O(1)

    # print(lst_profit)
    # print(lst_profit[:-4:-1])

    lst_company = []
    for k, v in base_company.items():
        if v in lst_profit[:-4:-1]:
            lst_company.append(k)

    return lst_company


def profit_of_three_2(base_com):  # O(NLogN)

    lst_profit = [i for i in base_com.values()]  # O(N)
    lst_profit.sort(reverse=True)  # O(NLogN)
    lst_company = [k for k, v in base_company.items() if v in lst_profit[:3]]  # O(N)

    return lst_company


print(profit_of_three(base_company))

print('*' * 20)

print(profit_of_three_2(base_company))

'''
Решение вторым способом будет быстрее так, как его сложноть в нотации "О-большое" равна
NLogN, сложность первого способа N**2 ("пузырьковая сортировка"),
 что занимает значительно больше времени.
'''
