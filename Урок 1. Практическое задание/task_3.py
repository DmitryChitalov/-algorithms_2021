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


def get_richest_firms_1(income_dict):
    """
        Получает в качестве аргумента словарь
        Возвращает список, состоящий из кортежей компаний и их наибольшей годовой прибыли (3 штуки)
        Сложность алгоритма: O(N log N) логарифмическая - наиболее эффект-ный алгоритм при малом количестве данных
    """
    firms_and_salary = [(key, value) for key, value in income_dict.items()]  # O(N) + O(N)
    firms_and_salary.sort(key=lambda value: value[1], reverse=True)  # O(N log N)
    return firms_and_salary[:3]


def get_richest_firms_2(income_dict):
    """
        Получает в качестве аргумента словарь
        Возвращает список, состоящий из кортежей компаний и их наибольшей годовой прибыли (3 штуки)
        Сложность алгоритма: O(N^2) - квадратичная  (сортировка методом выбора)
    """
    richest_firms = [(key, value) for key, value in income_dict.items()]  # O(N) + O(N)
    for pos in range(len(richest_firms) - 1):  # O(N)
        for k in range(pos + 1, len(richest_firms)):  # O(N)
            if richest_firms[k][1] < richest_firms[pos][1]:  # сравниваем значения из словарей
                richest_firms[k], richest_firms[pos] = richest_firms[pos], richest_firms[k]  # O(1)
    richest_firms.reverse()  # O(N)
    return richest_firms[:3]


def get_richest_firms_3(income_dict):
    """
         Получает в качестве аргумента словарь
         Возвращает список, состоящий из кортежей компаний и их наибольшей годово
         Сложность алгоритма: O(N) линейная - наиболее эффект-ный алгоритм при большом количестве данных
    """
    richest_firms = []
    for i in range(3):  # возьмём три цикла, возвращающих по кортежу "фирма - макс. выручка"
        rich_firm_name = ''
        random_firm_salary = [float(value) for value in income_dict.values()][0]
        for key, value in income_dict.items():
            if float(value) > random_firm_salary:
                random_firm_salary = value
                rich_firm_name = key
        if random_firm_salary == [float(value) for value in income_dict.values()][0]:  # здесь проверяем не осталось ли
            # то же значение, что и перед циклом (можно оптимизировать)
            rich_firm_name = [key for key in income_dict.keys()][0]
        richest_firms.append((rich_firm_name, income_dict.pop(rich_firm_name)))
    return richest_firms


dict_values = {
    "Hleb'i'drova": 1500,
    'IvRoshe': 5000,
    'RichardGir': -80000,
    'Samuel': -523600,
    'MohnatiyMoh': -123320
}

print(get_richest_firms_1(dict_values))
print(get_richest_firms_2(dict_values))
print(get_richest_firms_3(dict_values))
