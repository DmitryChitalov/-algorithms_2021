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


from collections import namedtuple


def enter_number(quarter):
    try:
        val = abs(int(input(f'Please enter profit {quarter} quarter\n')))
    except ValueError:
        print("Error: you've entered incorrect value")
        return enter_number(quarter)
    return val


def profit():
    cnt = 1
    number = []
    for i in range(4):
        number.append(enter_number(cnt))
        cnt += 1
    return number


def cnt_company():
    try:
        cnt = abs(int(input('Enter the number of companies to calculate profit\n')))
    except ValueError:
        print("Error: you've entered incorrect value")
        return cnt_company()
    return cnt


def company():
    cnt = cnt_company()
    cases = {}
    avr_profit = 0
    for i in range(cnt):
        name = input('Please enter name of company\n')
        profit_firm = profit()
        companies = namedtuple(f'{name}', 'first, second, third, fourth')
        case = companies(first=profit_firm[0], second=profit_firm[1], third=profit_firm[2], fourth=profit_firm[3])
        cases[name] = case
    for i in cases.values():
        avr_profit += sum(i)
    avr_profit /= cnt
    print(f'Average profit of companies: {avr_profit}')
    for key, val in cases.items():
        if sum(val) > avr_profit:
            print(f'Companies with above average profit: {key}')
    for key, val in cases.items():
        if sum(val) < avr_profit:
            print(f'Companies with below average profit: {key}')


company()
