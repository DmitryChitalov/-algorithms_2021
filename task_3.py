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


def find_top_3_company_one(some_dict):
    return list({k: v for k, v in sorted(some_dict.items(), key=lambda item: item[1])[:-4:-1]}.keys())
    # some_dict.items()        O(1)
    # key=lambda item: item[1] O(1)
    # sorted()                 O(n log n)
    # for                      O(n)
    # k: v                     O(1)
    # [:-4:-1]                 O(n)
    # keys()                   O(1)
    # list()                   O(n)

    # По итогу, как я понимаю: O(n log n)


def find_top_3_company_two(some_dict):

    value_list = []                  # O(1)
    for el in some_dict.values():    # O(n)
        value_list.append(el)        # O(1)

    for i in range(len(value_list) - 1):                                             # O(n)
        for j in range(len(value_list) - i - 1):                                     # O(n)
            if value_list[j] < value_list[j + 1]:                                    # O(n)
                value_list[j], value_list[j + 1] = value_list[j + 1], value_list[j]  # O(n)

    result = []                         # O(1)
    for el in value_list:               # O(n)
        if len(result) == 3:            # O(1)
            break                       # O(1)
        for k, v in some_dict.items():  # O(n)
            if el == v:                 # O(1)
                result.append(k)        # O(1)

    return result  # O(1)

    # По итогу, как я понимаю: O(n^4)

    # Вывод: используйте встроенные функции и будет вам счастье.


if __name__ == '__main__':
    inf_for_company = {'Apple': 1000000, 'Xiaomi': 500000, 'Huawei': 250000, 'Oppo': 0, 'Samsung': 750000}
    print(find_top_3_company_one(inf_for_company))
    print(find_top_3_company_two(inf_for_company))
