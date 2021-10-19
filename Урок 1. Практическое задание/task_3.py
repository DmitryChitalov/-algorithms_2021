"""
Задание 3.

Для этой задачи:
1) придумайте 2-3 решения (не менее двух)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.

Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
"""

from collections import Counter

# список в формате ("имя компании" : доход), упрощённо
list_company = {'A': 1, 'B': 11, 'C': 26, 'D': 43, 'E': 14, 'F': 29, 'G': 34, 'H': 49}


def search_through_count(lst):    # вариант первый. Сложность линейная  O(n)
    count = Counter(lst)    # O(n)
    return count.most_common(3)    # O(1)


def search_in_cycles(lst):    # второй вариант. Сложность линейная  O(n)
    checklist_company = []    # O(1)
    finance_company = []    # O(1)
    quantity_company = 3    # O(1)
    for i, j in lst.items():    # O(n)
        checklist_company.append(i)    # O(1)
        finance_company.append(j)    # O(1)
    while quantity_company > 0:    # O(1)
        maximum_finance_company = max(finance_company)    # O(n)
        quantity_company = quantity_company - 1    # O(1)
        print(checklist_company.pop(finance_company.index(maximum_finance_company)),
              finance_company.pop(finance_company.index(maximum_finance_company)))


print(*search_through_count(list_company))
search_in_cycles(list_company)

""" Сложность первого и второго вариантов одинакова.
первая функция проще (минимум кода, легче читать)
"""