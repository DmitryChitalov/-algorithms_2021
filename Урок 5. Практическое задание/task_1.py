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


class MyError(Exception):
    def __init__(self, text):
        self.text = text


def middle_profit():
    list_of_firms = []
    sum_profit = 0
    try:
        number_of_firms = int(input('Введите количество предприятий для расчета прибыли: '))
        if number_of_firms <= 0:
            raise MyError('Количество фирм не может принимать отрицательные значения!')

        for firm in range(number_of_firms):
            name = input('Введите название предприятия: ')
            if name.isdigit():
                raise MyError('Название фирм не может состоять из цифр! Повторите ввод.')
            profit = input('Через пробел введите прибыль данного предприятия \nза каждый квартал (всего 4 квартала): ').split()
            while len(profit) < 4 or not [el for el in profit if el.isdigit()]:
                print('Необходимо ввести данные за все 4 квартала числами через пробел')
                profit = input('Через пробел введите прибыль данного предприятия '
                               '\nза каждый квартал (всего 4 квартала): ').split()

            Profit_quartals = namedtuple('по_кварталам', 'кв_1 кв_2 кв_3 кв_4')
            quartals = Profit_quartals(*profit)
            mid_profit = round(sum(map(int, profit)) / 4, 2)
            sum_profit += mid_profit
            Firms = namedtuple(name, 'прибыль средняя_прибыль')
            firm_i = Firms(quartals, mid_profit)
            list_of_firms.append(firm_i)
        total_middle_profit = round(sum_profit / number_of_firms, 2)

    except ValueError:
        print('Некорректный ввод!')
        middle_profit()
    except MyError as m:
        print(m)
        middle_profit()
    except Exception:
        print('Некорректные данные')

    else:
        print()
        print(f'Средняя годовая прибыль всех предприятий: {total_middle_profit}')

        higher_middle_firms = []
        lower_middle_firms = []
        for el in list_of_firms:
            if el.средняя_прибыль >= total_middle_profit:
                higher_middle_firms.append(el)
            else:
                lower_middle_firms.append(el)

        print()
        print('Предприятия с прибылью выше среднего значения: ')
        for el in higher_middle_firms:
            print(el)

        print()
        print('Предприятия с прибылью ниже среднего значения: ')
        for el in lower_middle_firms:
            print(el)


middle_profit()

