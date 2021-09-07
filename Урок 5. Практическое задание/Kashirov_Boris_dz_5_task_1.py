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

# Namedtuple
from collections import namedtuple

MY_DICT = {}


def my_input():
    name = str(input('Введите наименование предприятия: ')).capitalize()
    if name in MY_DICT.keys():
        return'Повторять наименования предприятий нельзя!'
    quarter = str(input(f'Введите прибыль {name} через пробел: '))
    if quarter.count(' ') != 3:
        print('Данные по остальным/лишним периодам будут заменены на 0')
        quarter = quarter.split(' ')
        if len(quarter) < 4:
            while len(quarter) < 4:
                quarter.append('0')
        else:
            while len(quarter) > 4:
                quarter.pop()
    else:
        quarter = quarter.split(' ')
    return my_namedtuple(name, quarter, MY_DICT)


def my_namedtuple(c_name, money_as_lst, my_dict):
    print(c_name, money_as_lst)
    corp_namedtuple = namedtuple(f'{c_name}', 'q_1 q_2 q_3 q_4')
    quarters = corp_namedtuple(
        q_1=int(money_as_lst[0]),
        q_2=int(money_as_lst[1]),
        q_3=int(money_as_lst[2]),
        q_4=int(money_as_lst[3])
    )
    my_dict[c_name] = sum(quarters)
    return my_dict


number_of_corporation = int(input('Введите число предприятий: '))  # Указать число предприятий
for i in range(number_of_corporation):
    MY_DICT = my_input()
sum_res = sum(MY_DICT.values())
mid_res = sum(MY_DICT.values())/number_of_corporation
my_max_corp, my_min_corp = '', ''

for key, val in MY_DICT.items():
    if float(val) >= mid_res:
        my_max_corp += key + " "
    else:
        my_min_corp += key + " "

print(f'Общаяя годовая прибыль всех предпритяий: {sum_res}')
print(f'Средняя годовая прибыль всех предприятий: {mid_res:.02f}')
print(f'Предприятия, с прибылью выше среднего значения {my_max_corp} ')
print(f'Предприятия, с прибылью ниже среднего значения {my_min_corp} ')
