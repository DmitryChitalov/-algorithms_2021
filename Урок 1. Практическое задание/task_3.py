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


def find_3_biggest_01(dict_source):
    dict_obj = dict_source.copy()
    leaders_list = []
    while len(leaders_list) < 3:
        max_profit = max(dict_obj.values())  # O(N)
        for j in dict_obj.keys():
            if dict_obj[j] == max_profit:
                leaders_list.append(j)
                dict_obj.pop(j)
                break
    return leaders_list


"""
Сложность первого алгоритма - O(N) (цикл for i in dict_obj.keys()).
"""


def find_3_biggest_02(dict_obj):
    leader_list = []
    sorted_profits = sorted(dict_obj.values(), reverse=True)  # O(NlogN)
    sorted_profits = sorted_profits[:3]
    for i in sorted_profits:
        for j in dict_obj.keys():
            if dict_obj[j] == i:
                leader_list.append(j)
    return leader_list


"""
Сложность второго алгоритма - O(NlogN) (sorted).
"""


def find_3_biggest_03(dict_source):
    dict_obj = dict_source.copy()
    leader_list = []
    while len(leader_list) < 3:
        for i in dict_obj.keys():  # O(N)
            if dict_obj[i] == max(dict_obj.values()):  # O(N)
                leader_list.append(i)
                dict_obj.pop(i)
                break
    return leader_list


"""
Сложность третьего алгоритма - O(N^2) (max внутри цикла for).

Самое эффективное решение - первое (общая сложность O(N)). Его сложность ниже остальных, а само решение не является
более громоздким.
"""


companies = {'Motorola': 50, 'Nokia': 43, 'Siemens': 105, 'Sony Ericsson': 32, 'Xiaomi': 500, 'IPhone': 2,
             'Yotaphone': 1, 'Vertu': 10000}
print(find_3_biggest_01(companies))
print(find_3_biggest_02(companies))
print(find_3_biggest_03(companies))
