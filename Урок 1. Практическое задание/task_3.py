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


def func_1(in_dict):
    """O(n*log(n))"""
    return {k: v for k, v in sorted(in_dict.items(), key=lambda item: item[1], reverse=True)[0:3]}  # O(n*log(n))


def func_2(in_dict):
    """O(n*log(n))"""
    counter = 0                                                 # O(1)
    out_dict = {}                                               # O(1)

    for k in sorted(in_dict, key=in_dict.get, reverse=True):    # O(n*log(n))
        out_dict[k] = in_dict[k]                                # O(1)
        counter += 1                                            # O(1)
        if counter == 3:                                        # O(1)
            return out_dict                                     # O(1)


def func_3(in_dict):
    """O(n^2)"""
    companies_max_profit = {}                                       # O(1)

    for _ in range(3):                                              # O(3)
        max_profit = 0                                              # O(1)

        for item in in_dict.items():                                # O(n)
            if max_profit < item[1]:                                # O(1)
                company = item[0]                                   # O(1)
                max_profit = item[1]                                # O(1)

        companies_max_profit[company] = in_dict.pop(company)        # O(1)

    return companies_max_profit                                     # O(1)


if __name__ == '__main__':
    companies = {1: 32534, 2: 2353431, 3: 32142, 4: 3245642, 5: 657534, 6: 7867437, 7: 3245642}
    print(func_1(companies))
    print(func_2(companies))
    print(func_3(companies))
