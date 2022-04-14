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

from operator import itemgetter

# Список компаний
companies = (("Walmart", 524000),
             ("Saudi Aramco", 329800),
             ("State Grid", 387000),
             ("Sinopec Group", 369200),
             ("BP", 278400),
             ("China National Petroleum", 364100),
             ("Royal Dutch Shell", 311600),
             ("Toyota", 280500),
             ("Volkswagen", 275200),
             ("Exxon Mobil", 265700),
             )


def most_profit_v1(cmp_lst: tuple):
    """
    Поиск трёх наиболее успешных компаний во множестве.

    Сложность: O(n)

    ВЫВОД: Этот алгоритм эффективнее, потому что, очевидно функция сортировки работает медленнее, чем однократный проход
        по массиву данных в цикле.

    :param cmp_lst: кортеж кортежей (название, годовая прибыль)
    :return: кортеж из 3-х 2-х элементных кортежей 3-х наиболее успешных компаний из представленных
    """
    most_profit = ["", 0], ["", 0], ["", 0]

    for company in cmp_lst:
        if company[1] > most_profit[0][1]:
            most_profit[2][0], most_profit[2][1] = most_profit[1][0], most_profit[1][1]
            most_profit[1][0], most_profit[1][1] = most_profit[0][0], most_profit[0][1]
            most_profit[0][0], most_profit[0][1] = company
        if most_profit[1][1] < company[1] < most_profit[0][1]:
            most_profit[2][0], most_profit[2][1] = most_profit[1][0], most_profit[1][1]
            most_profit[1][0], most_profit[1][1] = company
        if most_profit[2][1] < company[1] < most_profit[1][1]:
            most_profit[2][0], most_profit[2][1] = company

    return (most_profit[0][0], most_profit[0][1]), \
           (most_profit[1][0], most_profit[1][1]), \
           (most_profit[2][0], most_profit[2][1])


def most_profit_v2(cmp_lst: tuple):
    """
    Поиск трёх наиболее успешных компаний во множестве.

    Сложность: O(n log n)

    :param cmp_lst: кортеж кортежей (название, годовая прибыль)
    :return: кортеж из 3-х 2-х элементных кортежей 3-х наиболее успешных компаний из представленных
    """
    companies_lst = list(cmp_lst)
    companies_lst.sort(key=itemgetter(1), reverse=True)
    return companies_lst[0], companies_lst[1], companies_lst[2]


if __name__ == '__main__':
    print(most_profit_v1(companies))
    print(most_profit_v2(companies))
