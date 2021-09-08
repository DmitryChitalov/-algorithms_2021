"""
1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections.

Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Фирма_1
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235

Введите название предприятия: Фирма_2
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34

Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Фирма_1

Предприятия, с прибылью ниже среднего значения: Фирма_2
"""

# name tuple
# defaultdict
from collections import defaultdict

def parce_value(list):
    if len(list) <= 4:
        for i in list:
            if not i.isdigit():
                print("Ошбика")
                input_info()
                # break
        # print("Верный ввод прибыли.")

# def analis(dict_comp_info):
#     dict_comp_middle = defaultdict(int)
#     for key, value in dict_comp_info.items():
#         summ = 0
#         for elem in value:
#             middle_value = summ + elem
#         dict_comp_middle[key] = middle_value
#     print("средняя прибыль (за год для всех предприятий)", dict_comp_middle)


def input_info():
    comp_num = input("Введите количество предприятий для расчета прибыли:")
    if comp_num.isdigit():
        comp_num = int(comp_num)
        dict_comp_info = defaultdict(int)
        dict_comp_middle = {}
        for _ in range(comp_num):
            key = input("Введите название предприятия:")
            value = input("Через пробел введите прибыль данного предприятия \nза каждый квартал(Всего 4 квартала): ").split(' ')
            # print(value)
            parce_value(value)
            dict_comp_info[key] = value
            summ = 0
            for elem in value:
                summ = summ + int(elem)
            dict_comp_middle[key] = summ / 4

        print("dict_comp_info", dict_comp_info)
        print("dict_comp_middle", dict_comp_middle)
        middle_val_all = 0
        for val_year_one_comp in dict_comp_middle.values():
            middle_val_all = middle_val_all + val_year_one_comp
        middle_val_all = middle_val_all / comp_num
        print("Средняя прибыль (за год для всех предприятий): ", middle_val_all)

        list_above, list_lower = [], []
        for key, value in dict_comp_middle.items():
            list_above.append(key) if value > middle_val_all else list_lower.append(key)
        print("Предприятия, чья прибыль выше средней:", list_above)
        print("Предприятия, чья прибыль ниже средней:", list_lower)

    else:
        print("Некорректный ввод! Повторите ввод.")
        return input_info()

input_info()

