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

company_list = {
    'A': 30265,
    'B': 1000,
    'C': 5500,
    'D': 77000,
    'E': 665952,
    'F': 6545,
    'G': 3025,
    'H': 5299,
    'I': 999,
    'J': 7892,
    'K': 12355,
    'L': 4000,
    'M': 3000
}

# 1 -й вариант Сложность O(N^2)
def first_search_largest_company(list_in):
    biggest_volume_list = {}  # O(1)
    for i in range(1, 4):  # O(N)
        max_key, max_value = list(list_in.items())[0]  # O(1)
        for j in range(len(list_in)):  # O(N) + O(N) = O(N^2)
            if max_value < list(list_in.items())[j][1]:  # O(N)
                max_key, max_value = list(list_in.items())[j]  # O(1)
        biggest_volume_list[max_key] = max_value  # O(1)
        del list_in[max_key]
    return biggest_volume_list


# 2 -й вариант Сложность O(log n)
def second_search_largest_company(list_in):
    biggest_volume_list = []
    sorted_tuple = sorted(list_in.items(), key=lambda max_value: max_value[1], reverse=True)  # O(log n)
    biggest_volume_list = dict(sorted_tuple[0:3])
    return biggest_volume_list


# 3 -й вариант Сложность O(N)
def third_search_largest_company(list_in):
    biggest_volume_list = {}
    for j in range(1, 4):
        kv = max(list(list_in.items()), key=lambda i: i[1])
        max_key, max_value = kv
        biggest_volume_list[max_key] = max_value  # O(1)
        list_in = dict(list_in)
        del list_in[max_key]
    return biggest_volume_list


list_for_calc = dict(list(company_list.items()))
print(first_search_largest_company(list_for_calc))

list_for_calc = dict(list(company_list.items()))
print(second_search_largest_company(list_for_calc))

list_for_calc = dict(list(company_list.items()))
print(third_search_largest_company(list_for_calc))
