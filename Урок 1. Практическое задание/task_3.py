#!/usr/bin/env python3

import random

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

company = {f'Company {i}': random.randint(10000, 30000) for i in range(1, 101)}


def get_maximum_profit_company_v1(company: map) -> map:
    ''' O (n log n) '''
    return {i[0] : i[1] for i in sorted(company.items(), key=lambda x: x[1], reverse=True)[:3]}


def get_maximum_profit_company_v2(company: map) -> map:
    ''' O (n) '''

    temp = [('', 0), ('', 0), ('', 0)]

    for key, value in company.items():
        if value > temp[0][1]:
            temp[2], temp[1] = temp[1], temp[0]
            temp[0] = (key, value)
        elif value > temp[1][1]:
            temp[2] = temp[1]
            temp[1] = (key, value)
        elif value > temp[2][1]:
            temp[2] = (key, value)

    return {i[0] : i[1] for i in temp if i[0] != ''}


def main():
    ''' Вариант 2 лучше т.к. имеет меньшую алгоритмическую сложность '''
    print(get_maximum_profit_company_v1(company.copy()))
    print(get_maximum_profit_company_v2(company.copy()))


if __name__ == '__main__':
    main()
