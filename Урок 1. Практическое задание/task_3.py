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
import random


def get_companies_ver01(max_count):                 # O(N) - линейная сложность

    comp_dict = {'Компания № ' + str(i + 1): random.randint(0, 10000) for i in range(max_count)}    # O(len(lst))
    print('Список компаний: ', comp_dict)           # O(len(lst))

    print('3 компании с максимальной прибылью:')
    for i in range(1, 4):                           # O(1)
        max_profit = 0                              # O(1)
        name_company = ''                           # O(1)

        for el in comp_dict.items():                # O(len(lst))
            if el[1] > max_profit:                  # O(1)
                max_profit = el[1]                  # O(1)
                name_company = el[0]                # O(1)

        print(f'{i} место: {name_company}, {max_profit}')   # O(1)
        comp_dict.pop(name_company)                         # O(1)


def get_companies_ver02(max_count):                 # O(N) - линейная сложность

    comp_lst = ['Компания № ' + str(i + 1) for i in range(max_count)]   # O(N)
    profit_lst = [random.randint(0, 10000) for i in range(max_count)]   # O(N)

    print(comp_lst)                                 # O(N)
    print(profit_lst)                               # O(N)

    print('3 компании с максимальной прибылью:')
    for i in range(1, 4):
        max_profit = 0                              # O(1)
        name_company = ''                           # O(1)
        id_company = 0                              # O(1)

        for j in range(len(profit_lst)):            # O(N)
            if profit_lst[j] > max_profit:          # O(1)
                max_profit = profit_lst[j]          # O(1)
                name_company = comp_lst[j]          # O(1)
                id_company = j

        print(f'{i} место: {name_company}, {max_profit}')   # O(1)
        comp_lst.pop(id_company)                            # O(N)
        profit_lst.pop(id_company)                          # O(N)


get_companies_ver01(20)
get_companies_ver02(20)

# В приведенных примерах сложность линейная, зависит от количества элементов в словаре/списке.
# Тем не менее при использовании словаря скорость выполнения будет выше, так как меньшее количество
# операций имеет сложность O(N)
