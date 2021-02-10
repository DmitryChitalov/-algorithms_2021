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

my_dict = {"firm_1": 100, "firm_2": 100, "firm_3": 200,
           "firm_4": 400, "firm_5": 500, "firm_6": 100,
           "firm_7": 700, "firm_8": 800, "firm_9": 900}


# Сложность - O(n)
def three_minimals_1(input_dict):
    dict_of_minimals = {}
    for n in range(3):  # O(1)
        minimal = min(input_dict, key=input_dict.get)  # O(n)
        dict_of_minimals.setdefault(minimal, input_dict[minimal])  # O(1)
        input_dict.pop(minimal, None)  # O(1)
    return dict_of_minimals


# Сложность - O(n)
def three_minimals_2(input_dict):
    keys_list = list(input_dict.keys())  # O(1)
    values_list = list(input_dict.values())  # O(1)
    firms_list = []
    for _ in range(3):  # O(1)
        minimal_index = 0
        for n in range(len(values_list)):  # O(n)
            if values_list[n] < values_list[minimal_index]:  # O(1)
                minimal_index = n
        firms_list.append(keys_list[minimal_index])
        keys_list.pop(minimal_index)  # O(n)
        values_list.pop(minimal_index)  # O(n)
    return firms_list


"""Функция three_minimals_1 эффективнее, сложность меньше. 
Перебор идёт по элементам словаря. На выходе имеем словарь, как на входе"""
