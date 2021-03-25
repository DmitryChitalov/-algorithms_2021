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


def form_info_about_fim(firm_number):
    while True:
        try:
            profit = input('Через пробел введите прибыль данного предприятия за каждый квартал (всего 4 квартала): ')
            profit = profit.split()

            if len(profit) != 4:
                raise Exception
            elif True:
                for i in range(len(profit)):
                    profit[i] = float(profit[i])
                break

        except ValueError:
            print('Необходимо вводить лишь целые или дробные числа!!!')
        except Exception:
            print('Необходимо ввести 4 числа через пробел!')

    ntuple_obj = namedtuple(f'firm_{firm_number + 1}', 'quarter_1 quarter_2 quarter_3 quarter_4')
    return ntuple_obj(quarter_1=profit[0], quarter_2=profit[1], quarter_3=profit[2], quarter_4=profit[3])


def get_total_profit(firms_quarter_profit):
    profit = 0
    for value in firms_quarter_profit:
        profit += sum(value)

    profit /= len(firms_quarter_profit)
    return profit


def get_profit_statistics(firms_avg_prof_dict_items, tot_prof):
    firms_with_smaller_tot_profit = []
    firms_with_bigger_tot_profit = []
    for key, value in firms_avg_prof_dict_items:
        if value < tot_prof:
            firms_with_smaller_tot_profit.append(key)
        else:
            firms_with_bigger_tot_profit.append(key)

    return ', '.join(firms_with_bigger_tot_profit), ', '.join(firms_with_smaller_tot_profit)


while True:
    try:
        count = int(input('Введите количество предприятий: '))
        if count:
            break
    except ValueError:
        print('Введите целое число!!!')
        count = False

firms_info = {input('Введите название предприятия: '): form_info_about_fim(i) for i in range(count)}
firms_avg_profit = {key: sum(value) for key, value in firms_info.items()}

total_profit = get_total_profit(firms_info.values())
print(f'Средняя годовая прибыль всех предприятий: {total_profit}')

bigger_prof, smaller_prof = get_profit_statistics(firms_avg_profit.items(), total_profit)
print(f'Предприятия, с прибылью выше среднего значения:  {bigger_prof}')
print(f'Предприятия, с прибылью ниже среднего значения:  {smaller_prof}')