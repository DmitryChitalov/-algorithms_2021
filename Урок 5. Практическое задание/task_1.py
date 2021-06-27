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


def average_profit(count):
    firms = []
    for i in range(int(count)):
        name = input(f'Введите название предприятия №{i + 1}: ')
        firm_name_and_profit = namedtuple(f'Firm_{i + 1}', 'firm_name first second third fourth average')

        # проверки на "вшивость"
        profit_is_int = False
        profit_to_int = []
        while profit_is_int is False:
            try:
                profit = input(f'Через пробел введите прибыль предприятия "{name}"\n'
                               f'за каждый квартал (Всего 4 квартала): ')
                print()
                profit_count = len(profit.split(" "))

                # проверка данных на число
                for j in range(profit_count):
                    profit_to_int.append(float(profit.split(" ")[j]))

            except ValueError:
                print("\n*** Введены некорректные данные! ***\n")
            else:
                # проверка на введение нужного количества данных
                if profit_count != 4:
                    print("\n*** Должны быть введены данные за 4 квартала! ***\n")
                else:
                    profit_is_int = True

        # Заполняем шаблоны
        temp_name = firm_name_and_profit(
            firm_name=name,
            first=profit_to_int[0],
            second=profit_to_int[1],
            third=profit_to_int[2],
            fourth=profit_to_int[3],
            average=sum(profit_to_int) / len(profit_to_int)
        )
        firms.append(temp_name)

    # расчёт средней прибыли
    average_total = 0
    for f in range(len(firms)):
        average_total += firms[f].average / len(firms)
    print(f'Средняя годовая прибыль всех предприятий: {average_total}')
    above_avg = {}
    below_avg = {}
    for _ in range(len(firms)):
        if firms[_].average >= average_total:
            above_avg[firms[_].firm_name] = firms[_].average
        elif firms[_].average < average_total:
            below_avg[firms[_].firm_name] = firms[_].average
    print('Предприятия с прибылью выше среднего значения:\n', *above_avg, '\n',
          'Предприятия с прибылью ниже среднего значения:\n', *below_avg, sep="")


number_of_firms = input('Введите количество предприятий для расчёта прибыли: ')

average_profit(number_of_firms)
