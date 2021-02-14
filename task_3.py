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

"""def leaders (my_dict):                   
    my_list = my_dict.get(keys)
    def min_el1(my_list):
        min_value = my_list[0]
        for i in range(len(my_list)):
            if min_value > my_list[i]:
                min_value = my_list[i]
        return min_value
    return"""


def leaders1(my_dict):
    my_list = list(my_dict.values())  # O(1)
    my_list = sorted(my_list)  # O(n)
    leader_list = []  # O(1)
    for dict_key in my_dict.keys():  # O(n)
        if my_dict.get(dict_key) in my_list[len(my_list) - 1: len(my_list) - 4: -1]:  # O(n)
            leader_list.append(dict_key)  # O(1)
    return leader_list  # O(1)


""" Сложность первого способа O(n^2) """


def leaders2(my_dict):
    my_list = list(my_dict.values())  # O(1)
    leader_list = []  # O(1)
    for i in range(1, 4):  # O(1)
        for dict_key in my_dict.keys():  # O(n)
            if my_dict.get(dict_key) == max(my_list):  # O(1)
                leader_list.append(dict_key)  # O(1)
        my_list.remove(max(my_list))  # O(1)
    return leader_list  # O(1)


""" Сложность первого способа O(n) """

my_dict = {'ООО Меандр': 1230,
           'ЗАО Двери': 6500,
           'ИП Клюшкин': 5400,
           'ЗАО Заря': 2300,
           'OOO Blue box': 3700,
           'НП Профиль': 12400}
print(leaders1(my_dict))
print(leaders2(my_dict))

""" Вывод второй способ более оптимальный, поскольку при более простой реализации еще и выполняет функцию сортировки"""
