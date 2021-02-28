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
from collections import namedtuple, defaultdict


# В этой функции defaultdict используется на случай того, если пользователь введёт меньше цифр, чем нужно.
def input_income():
    income = input('Введи поквартальный доход через пробел ').split(' ')
    incomes_dict = defaultdict(int)
    for j in range(1, len(income) + 1):
        try:
            incomes_dict[j] = int(income[j - 1])
        except ValueError:
            print('Неверный формат данных')
            return input_income()
    return incomes_dict


num_of_firms = int(input('Ввведите количество фирм '))
firms_list = []
for i in range(num_of_firms):
    firm_tuple = namedtuple(input('Введине название '), 'quart_1 quart_2 quart_3 quart_4')
    incomes = input_income()
    firm = firm_tuple(
        quart_1=incomes[1],
        quart_2=incomes[2],
        quart_3=incomes[3],
        quart_4=incomes[4]
    )
    firms_list.append(firm)
average_income = sum(sum(x) for x in firms_list) / num_of_firms
print(f'\nСредняя годовая прибыль всех предприятий {"%.2f" % average_income}')
for i in firms_list:
    if sum(i) > average_income:
        print(f'У {type(i).__name__} доход {sum(i)} - выше среднего')
    elif sum(i) < average_income:
        print(f'У {type(i).__name__} доход {sum(i)} - ниже среднего')
    else:
        print(f'У {type(i).__name__} доход {sum(i)} - равен среднему')




