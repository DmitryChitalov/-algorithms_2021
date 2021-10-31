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

vocabulary_of_company_profits = {
    'Taxi': 5877,
    'Odopod': 1378,
    'Bonehook': 7856,
    'Big Spaceship': 4278,
    'Droga5': 1351,
}

# O(N Log N) -- С точки зрения простоты и экономии, этот код подходит лучше (надеюсь, что эти комментарии достаточны для ответа на 3 пункт задачи)

def function_O_n_log_n(max_value):
    sorted_dict = {k: v for k, v in sorted(max_value.items(), key=lambda item: item[1], reverse = True)[:3]}
    return sorted_dict

print(function_O_n_log_n(vocabulary_of_company_profits))

# O(n^2) -- это более сложный код (хотя он первый, до которого я додумалась)

def function_O_n_2(max_value):
    sorted_values = sorted(max_value.values(), reverse=True)
    sorted_dict = {}
    for i in sorted_values[:3]:
        for k in max_value.keys():
            if max_value[k] == i:
                sorted_dict[k] = max_value[k]
    return sorted_dict

print(function_O_n_2(vocabulary_of_company_profits))