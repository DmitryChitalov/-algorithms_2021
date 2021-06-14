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

annual_profit = {
    'ООО Альянс': 5000000,
    'ООО Вектор': 100000,
    'ООО Феникс': 2000000,
    'ООО Орион': 6000000,
    'ООО Лидер': 1000000,
    'ООО Партнер': 800000,
    'ООО Спектр': 600000,
    'ООО Прогресс': 4000000
}

#вариант 1:
def max_profit_1(dict_obj):
    dict_copy = dict_obj.copy()
    max_1 = dict_copy.popitem()
    for j in range(len(dict_copy)):
        temp_val = dict_copy.popitem()
        if temp_val[1] > max_1[1]:
            max_1 = temp_val
    dict_copy = dict_obj.copy()
    dict_copy.pop(max_1[0])
    max_2 = dict_copy.popitem()
    for j in range(len(dict_copy)):
        temp_val = dict_copy.popitem()
        if temp_val[1] > max_2[1]:
            max_2 = temp_val
    dict_copy = dict_obj.copy()
    dict_copy.pop(max_1[0])
    dict_copy.pop(max_2[0])
    max_3 = dict_copy.popitem()
    for j in range(len(dict_copy)):
        temp_val = dict_copy.popitem()
        if temp_val[1] > max_3[1]:
            max_3 = temp_val
    return (max_1, max_2, max_3)
#сложность О(N). Решение более эффективное, при условии обработки большого объема данных.

#вариант 2
def max_profit_2(dict_obj):
    list_dict = list(dict_obj.items())
    list_dict.sort(reverse=True, key=lambda i: i[1])
    return list_dict[0:3]
#сложность О(NlogN).
