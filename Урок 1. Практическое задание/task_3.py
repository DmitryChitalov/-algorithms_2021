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
company_list = {'Google': 31231, 'apple': 21424, 'microsoft': 24242, 'hp': 11245, 'samsung': 13342}
# Сортировка словаря, O(n^2)


def dict_sort(unsorted_dict):
    unsorted_dict = list(dict.items(unsorted_dict))
    for comp_el_2 in range(len(unsorted_dict)):    # o(n^2)
        for comp_el_3 in range(len(unsorted_dict) - comp_el_2 - 1):
            if unsorted_dict[comp_el_3][1] > unsorted_dict[comp_el_3 + 1][1]:
                unsorted_dict[comp_el_3 + 1], unsorted_dict[comp_el_3] = unsorted_dict[comp_el_3], \
                                                                         unsorted_dict[comp_el_3 + 1]
    reversed_list = list(reversed(unsorted_dict))
    return reversed_list
# Скрипт 1 O(n), если не учитывать операцию сортировки словаря или O(n^2) если она учитывается.


def max_profit_3(comp_list):
    sorted_list = dict_sort(comp_list)   # o(n^2)
    max_profit_list = []
    start = 0
    end = len(sorted_list)
    status = True
    while status is True:
        middle_num = round((start + end) / 2)
        if len(max_profit_list) == 2:
            status = False
        if len(sorted_list) <= 2:
            if sorted_list[0][1] < sorted_list[1][1]:
                max_profit_list.append(sorted_list[1])
                status = False
            else:
                max_profit_list.append(sorted_list[0])
                status = False
        if sorted_list[middle_num][1] < sorted_list[middle_num - 1][1]:
            max_profit_list.append(sorted_list[0])
            sorted_list.pop(0)

    return max_profit_list


print(max_profit_3(company_list))
# Скрипт 2, O(n), если не учитывать операцию сортировки словаря или O(n^2) если она учитывается.


def max_profit_2(comp_list):
    max_profit_list = []
    sorted_list = dict_sort(comp_list)  # O(n^2)
    for el in sorted_list:  # O(n)
        max_profit_list.append(el)
        if len(max_profit_list) == 3:
            return max_profit_list


print(max_profit_2(company_list))


# Скрипт 2 лучше, чем скрипт 1, нет обращения к индексам, код более понятный.
