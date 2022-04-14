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


list_info = {'Циско':843,
          'Гуугл':5874,
          'Яндекс':1260,
          'АМД':5420,
          'Румба': 321}


# Вариант 1. O(n log n)

val_list = sorted(list_info, key=list_info.get, reverse=True)[:3]  # O(n log n)
for e in val_list:  # O(n) - линейная
    print(e, ":", list_info[e])


# Вариант 2. Сложность O(n^2)

s_val = sorted(list_info.values(), reverse=True)  # O(n log n)
s_list_info = {}
j = 0
for i in s_val:  # O(n)
    for k in list_info.keys():  # O(n)
        if list_info[k] == i and j < 3:
            s_list_info[k] = list_info[k]
            j += 1
            break
