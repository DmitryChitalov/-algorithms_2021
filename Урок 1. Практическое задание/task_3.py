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

company_profit = {'Рога': 25000000, 'Копыта': 36000000, 'Газмяс': 5600000, 'Самовар': 365895412, 'Буревесник': 1235473,
                  'Паразит': 12345634546, 'Сухие ноги': 2500, 'Тусклые огни': 56547851, 'Зачемка': 65905468}


def max_profit(company):
    sorted_tup = sorted(company.items(), key=lambda x: x[1], reverse=True)[:3]       # O(NLogN)
    company_profit_top = dict(sorted_tup)                                            # O(N)
    for n, p in company_profit_top.items():                                          # O(N)
        print(n, p)                                                                  # O(1)


max_profit(company_profit)


"""
Сложность данного алгоритма - O(NLogN) + O(N) + O(N) + O(1) = O(N Log N)
"""


def max_profit_2(company):
    top_3 = {}                                                     # O(1)
    for i in range(3):                                             # O(1)
        max_val = max(company.values())                            # O(N)
        for k, v in company.items():                               # O(N)
            if v == max_val:                                       # O(1)
                top_3[k] = v                                       # O(1)
                del company[k]                                     # O(1)
                break
    print(top_3)                                                   # O(1)


max_profit_2(company_profit)

"""
Сложность данного алгоритма - O(1) + O(1) * (O(N) + O(N)*(O(1) + O(1) + O(1))) + O(1) = 
= 0(1) + O(1) * O(4N) + O(1) = O(4N)
"""

"""
Вывод: т.к., первый алгорить имеет сложность O(N Log N) - линейно-логарифмический, а второй O(4N), и, 
если я правильно понимаю цифру 4 можно отбросить, следовательно второй алгоритм имеет сложность O(N) - линейный.
Следовательно второй алгоритм должен выполняться быстрее, т.к. ленейные алгоритмы шустрее, чем линейно-логарифмические.
Ну это при условии, что я правильно все посчитал!)
"""