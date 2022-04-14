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
from operator import itemgetter

datab = {
    'mapple': 5000,
    'msoft': 2000,
    'fbook': 7000,
    'noogle': 5000
}


# первый вариант
# O(N)
def get_max(dict_in, count):
    maximum = [(k, dict_in[k]) for k in dict_in]  # O(1)
    maximum = sorted(maximum, key=itemgetter(1), reverse=True)  # O(N)
    print(dict(maximum[:count]))  # O(1)


# второй вариант
# O(N^2)
def get_max_2(dict_in):
    sorted_values = sorted(dict_in.values())  # O(N)
    sorted_dict = {}  # O(1)
    for i in sorted_values:  # O(N)
        for k in dict_in.keys():  # O(N)
            if dict_in[k] == i:  # O(1)
                sorted_dict[k] = dict_in[k]  # O(1)
                break  # O(1)
    for count, value in enumerate(reversed(sorted_dict)):  # O(N)
        if count >= 3:  # O(1)
            break  # O(1)
        print(value)  # O(1)


get_max(datab, 3)
get_max_2(datab)

# из-за цикла вложенного в цикл производительность второго решения ниже в несколько (550 по времени при тесте на словаре в 10 млн. комбинаций) раз
