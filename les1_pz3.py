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

# Способ №1. Сложность O(n)


def get_max_value(temp_dict):       # O(n)
    """
    Возвращает максимальное значение (value) словаря
    """
    max_value = 0
    for k, v in temp_dict.items():  # O(n)
        if v > max_value:           # O(1)
            max_value = v           # O(1)
            value = v               # O(1)
            company = k             # O(1)
    return company, value           # O(1)


my_dict = dict(ABC=23000, Zebra=150000, Tetraedri=56900, Fifth_Element=1100230, Musical=12303, Butterfly=692300)


new_dict = {}                      # O(1)
for i in range(3):                 # O(1)
    k, v = get_max_value(my_dict)  # O(n)
    new_dict[k] = v                # O(1)
    my_dict.pop(k)                 # O(1)

print('Способ №1. Сложность O(n)')
for key, val in new_dict.items():
    print(f'{key}: {val}')


# Способ №2. Сложность O(n^2)

my_dict = dict(ABC=23000, Zebra=150000, Tetraedri=56900, Fifth_Element=1100230, Musical=12303, Butterfly=692300)

val_list = []

for v in my_dict.values():              # O(n)
    val_list.append(v)                  # O(n)

val_list.sort()                         # NlogN
val_list = val_list[-3:]                # O(n)

new_dict = {}                           # O(1)

for i in range(3):                      # O(1)
    for k, v in my_dict.items():        # O(n)
        if v in val_list:               # O(n)
            new_dict[k] = v             # O(1)

print('Способ №2. Сложность O(n^2)')
for key, val in new_dict.items():
    print(f'{key}: {val}')


''' 
Эффективнее решение №1, потому что стоимость его O(n), что ниже стоимости решения №2 со стоимостью O(n^2)
Хотя, конечно и его очень надо доработать
'''