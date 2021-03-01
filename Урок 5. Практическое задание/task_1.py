"""
1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections

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

from collections import namedtuple
from numpy import mean


class NotEnough(Exception):
    pass


def mean_all(lst, num, sum_all=0):
    for firm in lst:
        sum_firm = firm.qr_1 + firm.qr_2 + firm.qr_3 + firm.qr_4
        sum_all += sum_firm

    return sum_all / num


def above_mean(lst, sum_mean, result=''):
    for firm in lst:
        sum_firm = firm.qr_1 + firm.qr_2 + firm.qr_3 + firm.qr_4
        if sum_firm > sum_mean:
            result = firm.name + ', ' + result
    if result[-2] == ',':
        result = result[:-2]

    return result


def lower_mean(lst, sum_mean, result=''):
    for firm in lst:
        sum_firm = firm.qr_1 + firm.qr_2 + firm.qr_3 + firm.qr_4
        if sum_firm < sum_mean:
            result = firm.name + ', ' + result
    if result[-2] == ',':
        result = result[:-2]

    return result


ENT = namedtuple('firm', 'name qr_1 qr_2 qr_3 qr_4')
list_firm = []
i = 0

try:
    num_ent = int(input('Введите колличество предприятий чтобы рассчитать прибыль: '))
    if num_ent == 1:
        raise NotEnough('Колличество предприятий должно быть больше 1!')

    while i < num_ent:
        i += 1
        name_ent = input(f'Введите название предприятия {i}: ')
        profit_ent = input('Через пробел введите прибыль данного предприятия\n'
                           'за каждый квартал(Всего 4 квартала): ')
        profit_ent = profit_ent.split(' ')
        if len(profit_ent) == 4:
            ENTERPRISE = ENT(
                name=name_ent,
                qr_1=int(profit_ent[0]),
                qr_2=int(profit_ent[1]),
                qr_3=int(profit_ent[2]),
                qr_4=int(profit_ent[3])
            )
        else:
            raise NotEnough('Нужно ввести 4 числа через пробел!')

        list_firm.append(ENTERPRISE)

    mean_prof = mean_all(list_firm, num_ent)
    print()
    print(f'Средняя годовая прибыль всех предприятий: {mean_prof} млрд')
    print(f'Предприятия, с прибылью выше среднего значения: {above_mean(list_firm, mean_prof)}')
    print(f'Предприятия, с прибылью ниже среднего значения: {lower_mean(list_firm, mean_prof)}')

except ValueError:
    print('Нужно ввести цифру, а вы ввели буквы или символы!')
except ZeroDivisionError:
    print('Колличество предприятий должно быть больше 1!')

'''
Пример компания и их прибыль в млрд:
Pepsico 14 30 48 70
The Coca-Cola Company 8 19 28 37 
Вимм-Билль-Данн 2 8 10 11
IDS Borjomi Group 5 9 10 13
'''
