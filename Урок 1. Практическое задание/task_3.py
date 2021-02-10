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

companies = [
    {"name": "Google", "profit": 9},
    {"name": "GeekBrains", "profit": 2},
    {"name": "Apple", "profit": 1},
    {"name": "Tesla", "profit": 1},
    {"name": "X5", "profit": 1},
    {"name": "Yandex", "profit": 1},
    {"name": "Microsoft", "profit": 1}
]


def find_richest_company1(companies, count=3):
    """
    Сложность: O(N log N)
    """
    return sorted(companies, key=lambda k: k['profit'], reverse=True)[0:count]


def find_richest_company2(companies, count=3):
    """
    Сложность: O(N ** 3)
    """
    top_companies = []
    for companie in companies:  # O(N)
        profit = companie['profit']  # O(1)
        if len(top_companies) < count:  # O(1)
            top_companies.append(companie)  # O(1)
        else:
            for top_companie in top_companies:  # O(N)
                if profit > top_companie['profit']:  # O(1)
                    top_companies.remove(top_companie)  # O(N)
                    top_companies.append(companie)  # O(1)
                    break

    return top_companies


print(companies)
print(find_richest_company1(companies))
print(find_richest_company2(companies))

# первый вариант круче, т.к. имеет сложность N log N и при увеличении количества N будет выполняться гораздо быстрее
