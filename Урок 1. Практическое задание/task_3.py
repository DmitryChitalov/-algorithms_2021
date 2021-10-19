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


# 1.  O(n^2)
def best_profit_1(company, n):
    sorted_dict = {}
    sorted_values = sorted(company.values(), reverse=True)[0:n]

    for i in sorted_values:
        for k in company.keys():
            if company[k] == i:
                sorted_dict[k] = company[k]
                break
    return sorted_dict


# 2. O(n log n)
def best_profit_2(company, n):
    sorted_dict = {}
    sorted_keys = sorted(company, key=company.get, reverse=True)[0:n]

    for w in sorted_keys:
        sorted_dict[w] = company[w]

    return sorted_dict


companies = {'Agricultural Bank of China': 31293,
             'Apple': 57411,
             'Saudi Aramco': 49287,
             'Berkshire Hathaway': 42521,
             'Alphabet': 40269,
             'SoftBank Group': 47053,
             'Industrial & Commercial Bank of China': 45783,
             'Microsoft': 44281,
             'China Construction Bank': 39283,
             'Facebook': 29146}

if __name__ == '__main__':
    print(best_profit_1(companies, 3))
    print(best_profit_2(companies, 3))

# второе решение эффективнее т.к. иммеет сложность O(n log n) которая меньше  O(n^2)
