from collections import namedtuple

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

Firm_pattern = namedtuple('Company', ['name', 'profit_1', 'profit_2', 'profit_3', 'profit_4'])


def main():
    firms = []
    while True:
        number_of_companies = input('Enter the number of companies: ')
        try:
            number_of_companies = int(number_of_companies)
            break
        except ValueError:
            print(f'You only have to enter one number!\n')
    for i in range(1, number_of_companies + 1):
        name = input('Enter company name: ')
        if name in [firm.name for firm in firms]:
            print(f'The firm already exists.\n')
            continue
        try:
            total_profit = input('Enter the profit of the company for 4 quarters, separated by a space: ').split()
            firm = Firm_pattern(name,
                                float(total_profit[0]),
                                float(total_profit[1]),
                                float(total_profit[2]),
                                float(total_profit[3]))
        except ValueError:
            print(f'You must enter numeric values!\n')
            continue
        except IndexError:
            print(f'You must enter 4 values!\n')
            continue
        firms.append(firm)
    return avg(firms)


def avg(firms):
    total = 0
    for firm in firms:
        total += sum(firm[1:])
    return output(total / len(firms), firms)


def output(avg_val, firms):
    above = [firm.name for firm in firms if avg_val > sum(firm[1:])]
    print(len(firms[0])-1)
    below = [firm.name for firm in firms if avg_val < sum(firm[1:])]
    return f'Average annual profit of all firms: {avg_val}\n' \
           f'Firms with above average profits: {above}\n' \
           f'Firms with below average profits: {below}\n'


print(main())
